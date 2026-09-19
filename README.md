# Henry Smith — Engineering Portfolio

A responsive, static portfolio for robotics, controls, autonomy, embedded software, and aerospace research and internship opportunities. Built with plain HTML and a shared CSS stylesheet; hosted on GitHub Pages.

## Local preview and validation

From the repository root:

```bash
python3 scripts/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://localhost:8000. Stop the server with Ctrl+C.

There is no package manager, framework, JavaScript runtime, or compilation step. Development and production use the same HTML, CSS, and assets, so separate development/production build commands do not apply. The check script uses only Python's standard library and validates local links, fragments, relative paths, image alt text, page metadata, heading counts, and PDF headers.

## Pages and shared styling

- `index.html`: portrait, introduction, featured projects, current research, about, education, skills, resume, and contact.
- `projects.html`: all five project summaries and links to detailed work.
- `experience.html`: MAGICC, LLNL, RAD, and CMR experience, plus education and additional projects.
- `project-llnl-raft.html`: HITL architecture, hydrodynamic identification, measured results, and poster.
- `project-rad-ros.html`: dual-robot deployment, rotational stabilization, validation, limitations, and presentation.
- `project-mars-rover.html`: rover camera-image retrieval contribution.
- `project-light-following.html`: line-following embedded-C robot. The existing URL is retained for compatibility; its previous light-following/C++ description was corrected from the resume.
- `style.css`: design tokens, shared navigation, cards, typography, page layouts, and responsive rules.
- `assets/favicon.svg`: small HS site mark.

Navigation and footer markup are repeated in each HTML page so pages work without JavaScript or a build step. When changing shared links, update all seven pages and rerun the checker. The mobile navigation stays visible and wraps into a separate row; no menu script is needed.

## Authoritative content and assets

The three supplied PDFs were moved without modifying their contents:

| Original document | Website path |
| --- | --- |
| Henry Smith UAV Resume 2026.pdf | `assets/documents/henry-smith-resume.pdf` |
| Smith_Henry_smith600_internship_project_poster_PDF_to_share.pdf | `assets/documents/llnl-hitl-raft-poster.pdf` |
| Henry_Smith_Dual_Robot_Systems_Research_BYU.pdf | `assets/documents/byu-rad-lab-dual-robot-research.pdf` |

The RAD presentation supplied to the repository is a six-slide PDF, not the PPTX named in the brief. The site provides open and download links to that PDF. If a PPTX is added later, it can be offered as an additional download.

The resume governs dates, titles, education, skills, and project summaries. The poster and RAD presentation provide technical depth. rosVTOL is described as ongoing; the RAD page explicitly records reverse-motion instability and the wheel-motor failure that prevented a complete end-to-end demo. No unsupported RAD programming languages, Docker proficiency, publications, or completed rosVTOL flight tests were added. Contact links use the resume's BYU email and LinkedIn profile, plus the existing GitHub account.

`profile_picture.png` remains the original portrait. The website uses an optimized 720-pixel JPEG at `assets/profile/henry-smith-profile.jpg` (about 148 KB). WebP previews in `assets/images/` show the full LLNL poster and RAD validation slide; together they are about 440 KB. All source document text remains available in the linked PDFs.

## GitHub Pages deployment

The existing repository is `henrydsmith2002/henrydsmith2002.github.io` on branch `main`. There is no deployment workflow, Jekyll configuration, or build configuration checked into this repository. This implementation preserves the existing static-root layout and does not alter remote Pages settings.

Keep the existing GitHub Pages publishing configuration. For branch-based publishing, the source should be `main` and `/ (root)`. Repository settings cannot be established from local files alone; verify Settings → Pages before pushing if the site is not already publishing.

All functional page, stylesheet, image, and document URLs are relative, supporting both a user site and a repository subpath. The Open Graph portrait URL is intentionally absolute for social crawlers and points to the current user-site domain. Update that metadata on all pages if the public domain changes. No backend, environment variables, or third-party fonts are required.

## Validation performed

- Static checker: seven HTML pages, 110 local references, including document links and fragments.
- Chromium: all pages at 320, 390, 768, and 1440 pixels; no horizontal overflow, broken images, console errors, or failed page requests.
- Keyboard skip navigation and resume download verified.
- All three PDFs served successfully with PDF content types and valid content.
- Production-equivalent static copy checked under `/portfolio/` to exercise repository-subpath URLs.
- Desktop and mobile layouts visually inspected, including portrait treatment and project pages.

Before pushing, review the content and portrait crop, open all three documents, and confirm that the current role and contact links remain up to date. This is a local implementation; it has not been committed or deployed.

## Commit and publish

Review the changes first, then run:

```bash
python3 scripts/check_site.py
git diff --check
git status --short
git add -A
git commit -m "Refresh engineering portfolio with research projects and resume"
git push origin main
```
