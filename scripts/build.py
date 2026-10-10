"""Assemble the static site and preserve former Hugo entry points."""
from pathlib import Path
from html import escape
import shutil

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / '_site'

ASSETS = (
    'index.html', 'coffee-script.ttf', 'coffee-font-license.txt', 'portrait.jpg',
    'share.jpg', 'favicon.svg', 'weather-observatory.jpg', 's2rain.jpg',
    'precipitation-downscaling.jpg', 'di-lab.jpg', 'ai-deadlines.jpg',
    'apelyido.jpg', 'catalogo-1849.jpg',
)

# Slugs of the publication pages the old Hugo site published. They no longer
# exist as content folders, but the URLs are indexed, so each one still needs a
# redirect stub. Add a slug here only to keep an old URL alive.
PUBLICATIONS = (
    'ai-quality-management',
    'chest-xray-classification',
    'conidial-fungi-transfer-learning',
    'faster-rcnn-blood-cell-classification',
    'lettuce-life-stage-classification',
    'photosynthetic-growth-signature',
    'public-security-threat-detection',
    'samba',
    'smart-aquaponics-machine-learning',
)

OUT.mkdir(exist_ok=True)
for name in ASSETS:
    shutil.copy2(ROOT / name, OUT / name)
if (ROOT / 'cv.pdf').is_file():
    shutil.copy2(ROOT / 'cv.pdf', OUT / 'cv.pdf')

def redirect(route, target):
    folder = OUT / route
    folder.mkdir(parents=True, exist_ok=True)
    url = escape(target, quote=True)
    # search engines discard a canonical that carries a fragment, so the
    # canonical points at the page the fragment lives on
    canonical = 'https://ruzcko.com' + escape(target.split('#')[0] or '/', quote=True)
    (folder / 'index.html').write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Page moved</title><meta name="robots" content="noindex">'
        f'<meta http-equiv="refresh" content="0;url={url}">'
        f'<link rel="canonical" href="{canonical}">'
        f'<p>This page has moved. <a href="{url}">Continue to the website</a>.</p></html>',
        encoding='utf-8')

redirect('publications', '/#publications')
redirect('experience', '/#experience')
for slug in PUBLICATIONS:
    redirect('publications/' + slug, '/#publications')
(OUT / '.nojekyll').touch()
(OUT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://ruzcko.com/sitemap.xml\n')
(OUT / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    '<url><loc>https://ruzcko.com/</loc></url></urlset>')
print('Static site assembled in _site')
