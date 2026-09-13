"""Assemble the static site and preserve former Hugo entry points."""
from pathlib import Path
from html import escape
import shutil

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / '_site'
OUT.mkdir(exist_ok=True)
for name in ('index.html', 'me.jpg', 'favicon.svg'):
    shutil.copy2(ROOT / name, OUT / name)
if (ROOT / 'cv.pdf').is_file():
    shutil.copy2(ROOT / 'cv.pdf', OUT / 'cv.pdf')

def redirect(route, target):
    folder = OUT / route
    folder.mkdir(parents=True, exist_ok=True)
    url = escape(target, quote=True)
    (folder / 'index.html').write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Page moved</title><meta name="robots" content="noindex">'
        f'<meta http-equiv="refresh" content="0;url={url}">'
        f'<link rel="canonical" href="https://ruzcko.github.io{url}">'
        f'<p>This page has moved. <a href="{url}">Continue to the website</a>.</p></html>',
        encoding='utf-8')

redirect('publications', '/#publications')
redirect('experience', '/#experience')
for publication in (ROOT / 'content/publications').glob('*/index.md'):
    redirect('publications/' + publication.parent.name, '/#publications')
(OUT / '.nojekyll').touch()
(OUT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://ruzcko.github.io/sitemap.xml\n')
(OUT / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    '<url><loc>https://ruzcko.github.io/</loc></url></urlset>')
print('Static site assembled in _site')
