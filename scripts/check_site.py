#!/usr/bin/env python3
"""Check static portfolio pages and local references using Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.references = []
        self.errors = []
        self.h1_count = 0
        self.has_description = False
        self.has_title = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.h1_count += 1
        if tag == 'title':
            self.has_title = True
        if tag == 'meta' and attrs.get('name') == 'description':
            self.has_description = bool(attrs.get('content'))
        if tag == 'img' and not attrs.get('alt'):
            self.errors.append('image lacks meaningful alt text')
        for attr in ('href', 'src'):
            if attrs.get(attr):
                self.references.append(attrs[attr])


def main():
    pages = {p.resolve(): Page(p) for p in ROOT.glob('*.html')}
    errors = []
    references = 0
    for path, page in pages.items():
        errors.extend(f'{path.name}: {error}' for error in page.errors)
        if page.h1_count != 1 or not page.has_title or not page.has_description:
            errors.append(f'{path.name}: expected one h1, title, and description')
        for reference in page.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            references += 1
            if url.path.startswith('/'):
                errors.append(f'{path.name}: root-relative link breaks subpath hosting: {reference}')
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(ROOT):
                errors.append(f'{path.name}: reference outside site: {reference}')
            elif not target.is_file():
                errors.append(f'{path.name}: missing asset/page: {reference}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.name}: missing anchor: {reference}')
    for doc in (ROOT / 'assets/documents').glob('*.pdf'):
        if not doc.read_bytes().startswith(b'%PDF-'):
            errors.append(f'{doc.name}: invalid PDF header')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} HTML pages; {references} local references; page metadata, headings, image alt text, anchors, and PDF headers.')
    print('All local URLs are relative and support GitHub Pages repository subpaths.')

if __name__ == '__main__':
    main()
