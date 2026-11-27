# Littera brand

The logo of Littera: a solid square with a mirrored L cut out of it. The L is a letter of type in a printing press.
Use `guidelines.md` for the rules. Use this file to find the files and to understand the choices.

## What is here

| Path | What it is |
|---|---|
| `svg/` | The logo files: colour for light and dark grounds, pixel cuts, one colour, favicon, app icon. |
| `png/` | PNG exports: avatar 512, Apple touch icon 180, the symbol from 16 to 1024 px. |
| `favicon.ico` | Icon with 16, 32 and 48 px, from the pixel cut. |
| `readme-header-light.svg`, `readme-header-dark.svg` | The README header as an image, one file for each GitHub theme. |
| `social-preview.png`, `social-preview.svg` | The GitHub social preview, 1280 x 640 px. The SVG is the source. |
| `guidelines.md` | Usage rules. |
| `preview.html` | The logo in real contexts. Open it in a browser. |
| `previous/` | The logo before the redesign (`logo.svg`, `favicon.ico`). Kept, not used. |
| `scripts/` | `build_kit.py` builds `svg/`. The other scripts come from the `design` plugin (`design-logo`). |

## Quick use

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/readme-header-dark.svg">
  <img src="brand/readme-header-light.svg" width="520" alt="Littera: nano typographic framework">
</picture>
```

- **GitHub avatar:** upload `png/avatar-512.png`.
- **GitHub social preview:** upload `social-preview.png` by hand (Settings, General, Social preview). GitHub has no API for it.
- **Favicon:** `svg/favicon.svg` and `favicon.ico`. Link the SVG first: it follows the browser theme.

## Rebuild

Change a colour in the `PALETTE` block of `scripts/build_kit.py`, then run:

```bash
python3 scripts/build_kit.py
```

The PNG files, `favicon.ico`, the README headers, `preview.html` and the social preview come from the `design-logo` and `design-web-assets` skills.
`build_kit.py` needs only Python 3.

## Decisions (2026-11-27)

This is a redesign. The owner likes the old logo and asked to refine it, not to replace it.

**Kept from the old logo:** the dark block, the light mirrored serif L (a letter of type in a printing press), the colour of the old mark (`#212529`).

**Changed:**

- The container is a square, not a tall block (92 x 118).
- The letter is from EB Garamond SemiBold (SIL Open Font License 1.1), not the old outline. Its thin parts are 4.0 percent of the square, against 3.4 percent in the old logo,
  and the shape is clean and rebuilt in whole numbers.
- The letter is placed by eye, not by the box. In the old logo the letter stood 2.8 units left of the middle. Here it stands half way between the middle of its box and its centre of mass,
  and the margin above it is 44 percent of the free height.
- A pixel cut of the letter for 16, 32 and 48 px: the hairlines of the main cut are less than a pixel at these sizes.

**Colour:** Ink (`#212529` on light, `#e6e6e6` on dark), the token `--text-primary` of Littera. Blue, purple and a printer's red were offered. Ink keeps the old look.

**Not chosen, and why:**

| Concept | Reason |
|---|---|
| Slab or sans L in the old tall block, with the nick of a type sort | They change the character of the letter. The nick is lost at 16 px. |
| The type sort with its imprint, the sort in the chase | They explain the idea, but the mark gets wider or more complex, and the frame merges at 16 px. |
| A drop cap, a tt ligature, the word in a serif | A different idea. The ligature reads as a hash sign. |
| Other fonts (Libre Baskerville, Source Serif, Merriweather, DM Serif, Playfair, Roboto Slab) | Garamond was chosen for its warm, bookish character. Playfair and DM Serif have hairlines thinner than the old logo. |

## Move to the new mark (done)

The project uses the new mark. The old files are kept in `previous/`:

| File | Change |
|---|---|
| `logo.svg` | Replaced by the new square (`brand/svg/symbol-ink.svg`). |
| `favicon.ico` | Replaced by `brand/favicon.ico` (16, 32 and 48 px). |
| `README.md` | The logo image is 120 x 120 px, a square. |
| `index.html` | Links `brand/svg/favicon.svg`, which follows the browser theme, before `favicon.ico`. |

## Open checks

- Search for similar marks before public use. A letter in a square is a common shape.
- "Littera" is a common word in typography. Check the trademark separately.
- Check the favicon in a real browser tab, light and dark.
- Not tested: the shelf test next to other CSS frameworks for typography, the colour-blind view, the white version on photos, print.
- The mark has no wordmark. The README header and the social preview use plain system-font text, not outlines.
