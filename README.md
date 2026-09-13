# Rogelio Ruzcko Tobias

Minimal personal website hosted at https://ruzcko.github.io/ with GitHub Pages.

## Editing

The active page is `index.html`, with its portrait in `me.jpg`.
The page includes its styles and small interaction scripts. No Hugo, Node.js,
or package installation is required. Open `index.html` in a browser to preview.

## Publishing

Run `python3 scripts/build.py` to assemble `_site/`. Push to `main` to deploy
through GitHub Actions. The build includes redirects for the former publication
and experience pages, a sitemap, and robots.txt. Add `cv.pdf` when ready; the
current mockup includes a CV link but no PDF has been supplied.

The old Hugo content and configuration remain as reference material and are
not published. Publication folder names are used to preserve old URLs.
