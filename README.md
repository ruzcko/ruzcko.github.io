# Rogelio Ruzcko Tobias

Minimal personal website hosted at https://ruzcko.com/ with GitHub Pages.

## Editing

The whole site is `index.html`, with its portrait in `portrait.jpg`. The page
carries its own styles and small interaction scripts — no framework, no web
fonts beyond `coffee-script.ttf`, no CDN, and nothing to install. Open
`index.html` in a browser to preview.

## Publishing

Run `python3 scripts/build.py` to assemble `_site/`. Push to `main` to deploy
through GitHub Actions. The build copies the published assets, writes a sitemap
and robots.txt, and generates redirect stubs for the former publication and
experience URLs. Add a new image to the `ASSETS` list in the script or it will
not be published; the old URLs kept alive live in `PUBLICATIONS`.

The site was previously generated with Hugo Blox. That scaffolding has been
removed — it is still in the git history if an old page is ever needed.

## Domain and recovery

The primary address is https://ruzcko.com. GitHub Pages handles redirects from
ruzcko.github.io and www.ruzcko.com. Cloudflare provides DNS, with DNS-only
GitHub Pages A records at the apex and a www CNAME to ruzcko.github.io.
The repository Pages publishing source is GitHub Actions.

Source and image assets are versioned in GitHub. To roll back a release, revert
the relevant commit on main and push; the deployment workflow republishes it.
