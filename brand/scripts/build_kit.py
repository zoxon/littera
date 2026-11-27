#!/usr/bin/env python3
"""Build the Littera logo kit (square, mirrored L, colour Ink). Standard library only.

Edit the PALETTE block to change a colour, then run: python3 build_kit.py   (writes ../svg).
The colours are the tokens of Littera in `src/root.css` (`--text-primary`, light and dark theme).

The mark is a solid square with a mirrored L cut out of it. The L is a letter of type: types are cast mirrored, to print upright.
The outline of the letter is from EB Garamond SemiBold (SIL Open Font License 1.1, https://openfontlicense.org).
It was placed by eye, not by the box: the stem is on the right and the top left is empty, so the letter stands half way between
the middle of its box and its centre of mass, and the margin above it is 44 percent of the free height.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'svg'
PALETTE = {
  'ink': '#212529',      # --text-primary, light theme: the mark on light grounds (the colour of the old logo)
  'pale': '#e6e6e6',     # --text-primary, dark theme (hsl(0, 0%, 90%)): the mark on dark grounds
  'ground': '#212529',   # the ground of the tile
}

# Main cut on a 200 grid: the square and the letter as one path (even-odd), so the letter is a hole. Use it from 40 px up.
MAIN = 'M0 0H200V200H0ZM136.9 150.7L136.9 150.7Q138.8 150.7 139.8 150Q140.8 149.2 140.8 148.3L140.8 148.3Q140.8 147 139.6 146.2Q138.4 145.5 137.2 145.1L137.2 145.1Q131.1 143.6 128.2 141.3Q125.3 139 125.3 133.7L125.3 133.7L125.3 55.5Q125.3 51.6 126.3 49.6Q127.2 47.6 129.5 46.5Q131.8 45.3 136.2 44.5L136.2 44.5Q140.6 43.6 140.6 40.9L140.6 40.9Q140.6 39.9 139.5 39.3Q138.3 38.7 136.7 38.7L136.7 38.7Q132.5 38.7 128.7 38.9Q124.8 39.1 121.3 39.2Q117.7 39.4 114.1 39.4L114.1 39.4Q110.2 39.4 106.2 39.2Q102.2 39.1 98.1 38.9Q93.9 38.7 90 38.7L90 38.7Q88.3 38.7 87.3 39.3Q86.3 39.9 86.3 41.1L86.3 41.1Q86.3 42.5 87.4 43.2Q88.5 44 90.5 44.5L90.5 44.5Q97.1 46.2 100.3 48.2Q103.4 50.1 103.4 55L103.4 55L103.4 132.7Q103.4 137.6 101.2 139.9Q99 142.2 92.9 142.2L92.9 142.2L74.4 142.2Q70.5 142.2 67.2 140.9Q64 139.5 62 137.5L62 137.5Q58.9 134.7 56.9 131.7Q54.8 128.6 52.9 124.5L52.9 124.5Q51.8 122 50.7 120.6Q49.7 119.3 48.7 119.3L48.7 119.3Q47.5 119.3 47 120.4Q46.5 121.5 46.5 122.7L46.5 122.7Q46.5 122.8 46.7 123.7Q46.8 124.5 46.8 125.1L46.8 125.1Q48.2 130 49.1 133.6Q50.1 137.1 50.7 140.4Q51.2 143.8 51.8 147.7L51.8 147.7Q51.9 148.9 52.4 149.8Q52.9 150.7 54.5 150.7L54.5 150.7Q59.6 150.7 66.7 150.6Q73.8 150.4 81.8 150.3Q89.8 150.2 97.9 150Q106 149.9 113.1 149.9L113.1 149.9Q116.8 149.9 121.7 150Q126.5 150.2 130.8 150.5Q135 150.7 136.9 150.7Z'

# Pixel cut on a 16 x 16 grid for exactly 16, 32 and 48 px. Every coordinate is an integer, so every edge is sharp.
# The thin parts of the letter are one pixel, because a hairline of the main cut is less than a pixel at 16 px.
PIXEL = ('M0 0H16V16H0Z'
         'M6 3H12V4H10V13H3V10H4V12H8V4H6Z')

CRISP = ' shape-rendering="crispEdges"'


def svg(inner, root='', box='0 0 200 200'):
  return f'<svg xmlns="http://www.w3.org/2000/svg" {root}viewBox="{box}">{inner}</svg>\n'


def mark(d, colour, extra=''):
  return f'<path{extra} fill="{colour}" fill-rule="evenodd" d="{d}"/>'


def write(name, text):
  OUT.mkdir(parents=True, exist_ok=True)
  (OUT / name).write_text(text, encoding='utf-8')


ink, pale, ground = PALETTE['ink'], PALETTE['pale'], PALETTE['ground']
write('symbol-ink.svg', svg(f'<title>Littera</title>{mark(MAIN, ink)}'))
write('symbol-pale.svg', svg(f'<title>Littera</title>{mark(MAIN, pale)}'))
write('symbol-white.svg', svg(f'<title>Littera</title>{mark(MAIN, "#ffffff")}'))
write('symbol-black.svg', svg(f'<title>Littera</title>{mark(MAIN, "#000000")}'))
write('symbol-pixel-ink.svg', svg(f'<title>Littera</title>{mark(PIXEL, ink, CRISP)}', box='0 0 16 16'))
write('symbol-pixel-pale.svg', svg(f'<title>Littera</title>{mark(PIXEL, pale, CRISP)}', box='0 0 16 16'))
# Favicon: the mark is a tile already, so it has no extra tile. It follows the browser theme. The rules use #fav so they stay inside the file.
css = f'#fav path{{fill:{ink}}}@media (prefers-color-scheme:dark){{#fav path{{fill:{pale}}}}}'
write('favicon.svg', svg(f'<style>{css}</style><title>Littera</title>{mark(PIXEL, ink, CRISP)}', 'id="fav" ', '0 0 16 16'))
# App icon: a full square (the platform rounds the corners). The letter alone in pale on the tile, with no second container: the lines of the L
# have the weight of the other zoxon logos. The size and the centre are the result of `optical_fit.mjs` (optical size 0.39 of the tile).
# The rounded tile is for the README header only.
LETTER = MAIN[MAIN.index('M136.9'):]                  # the outline of the L: the hole of the block
tile = (f'<title>Littera</title><rect{{R}} width="200" height="200" fill="{ground}"/>'
        f'<g transform="translate(100 100) scale(0.82) translate(-100 -98.13)"><path fill="{pale}" d="{LETTER}"/></g>')
write('app-icon.svg', svg(tile.replace('{R}', '')))
write('app-icon-rounded.svg', svg(tile.replace('{R}', ' rx="44"')))
print('wrote the kit to', OUT)
