# Rogelio Ruzcko Tobias

Minimal personal website hosted at https://ruzcko.com/ with GitHub Pages.

## Editing

The active page is `index.html`, with its portrait in `me.jpg`.
The page includes its styles and small interaction scripts. No Hugo, Node.js,
or package installation is required. Open `index.html` in a browser to preview.

## Publishing

Run `python3 scripts/build.py` to assemble `_site/`. Push to `main` to deploy
through GitHub Actions. The build includes redirects for the former publication
and experience pages, a sitemap, and robots.txt. The CV button opens
`cv.pdf`, which is included in the published site.

The old Hugo content and configuration remain as reference material and are
not published. Publication folder names are used to preserve old URLs.

## Domain and recovery

The primary address is https://ruzcko.com. GitHub Pages handles redirects from
ruzcko.github.io and www.ruzcko.com. Cloudflare provides DNS, with DNS-only
GitHub Pages A records at the apex and a www CNAME to ruzcko.github.io.
The repository Pages publishing source is GitHub Actions.

Source and image assets are versioned in GitHub. To roll back a release, revert
the relevant commit on main and push; the deployment workflow republishes it.
