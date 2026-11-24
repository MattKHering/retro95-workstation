# Retro95 Workstation

A browser-based recreation of the Windows 95 desktop, with vintage productivity tools, games, music and a persistent virtual file system. Built with HTML, CSS and JavaScript; no server database or build step is required.

## Features

- Start menu, taskbar, movable/resizable windows, Explorer, virtual drives and desktop shortcuts.
- Classic-style applications, games and simplified period software (113 registered program entries in the current build).
- Dad Rock CD Player with 18 video-linked tracks and local audio imports; music videos open in the vintage browser when embedding is allowed.
- Focus & Productivity: colored Sticky Notes and a shaded analog/digital Pomodoro timer.
- IndexedDB/browser storage, local profiles, backup/restore, portable disk exports, and supported external disk saving.
- ZIP, ISO9660 and FAT12 utilities; screensavers, desktop themes, CRT settings, and Windows 98/ME/2000/XP-inspired appearances.
- Installable PWA and offline shell; experimental v86 integration requires separately supplied runtime and licensed boot media.

## Run locally

Open `windows95.html` for the standalone desktop, or serve the repository for reliable origin-based storage and PWA support:

```sh
python -m http.server 8000
```

Open <http://localhost:8000/>. Install via your browser's app installation option where supported.

## Publish to GitHub Pages

1. Create an empty GitHub repository (suggested name: `retro95-workstation`). Use public visibility only if you want the source public and have appropriate rights to publish it.
2. Upload the contents of this directory to the `main` branch, including `.github/workflows/pages.yml` (or push using Git).
3. In repository **Settings → Pages**, select **GitHub Actions** as the publishing source.
4. In **Actions**, run **Deploy Retro95 to GitHub Pages** if the initial run did not deploy. Future pushes to `main` validate and deploy the site automatically.
5. Open the URL reported by the successful deployment, normally `https://YOUR-USERNAME.github.io/retro95-workstation/`.

GitHub Pages availability for private repositories depends on the account plan. See [GitHub's Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Project files

| File | Purpose |
| --- | --- |
| `windows95.html` | Complete desktop, application code and styles |
| `index.html` | Entry point redirecting to the standalone desktop |
| `retro95-manifest.json` | PWA metadata |
| `retro95-sw.js` | Scoped offline cache |
| `retro95-icon*.png` | PWA icons |
| `scripts/check.py` | JavaScript syntax and manifest asset validation |
| `.github/workflows/pages.yml` | Continuous GitHub Pages deployment |

## Data and privacy

Personal files, notes, settings and imported media live in browser storage or explicitly exported disk files, not in Git. Export a backup from the old desktop and restore it on the hosted version to migrate personal data. Hosting does not automatically sync data across devices. Browser storage is scoped to the origin; other projects under the same GitHub Pages hostname may share origin storage. Local profiles are not security boundaries. Keep backups, disk images and private data out of the public repository. Embedded online videos require internet access and are subject to provider rules.

## Development and validation

Edit `windows95.html` directly; this snapshot preserves the original standalone architecture. With Python 3 and Node.js installed, run `python scripts/check.py` before committing. The check validates syntax and required manifest assets, not full application behavior. No deployment or browser runtime test is claimed for this packaging change.

## Scope and rights

This is an unofficial recreation, not Microsoft Windows or a complete emulator. Some apps and games are simplified adaptations. No original Windows installation media, proprietary game executables, or commercial music audio is bundled. Windows and other product names identify the historical interfaces that inspired this project; no affiliation is implied. No new license has been assigned: review the rights to the project and any third-party assets before public distribution.

### Public deployment and desktop lock

Keep the source repository private. GitHub Pages from a private personal repository requires an eligible plan; choose GitHub Actions under Settings → Pages → Build and deployment, then run the deployment workflow. The deployed static assets are public, even if the Git repository is private. The shared startup password is only a simulated desktop lock; it is not authentication or access control. Never reuse a personal password or store sensitive data in this recreation. The application has a restrictive meta CSP, but this is not a security guarantee. GitHub Pages may share an origin with other projects. Use a dedicated origin if possible. Security hardening and deployment have not received a complete browser or penetration test.
