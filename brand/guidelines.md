# Littera logo guidelines

The logo is a solid square with a mirrored L cut out of it. The L is a letter of type: metal types are cast mirrored, so that they print upright.
The L is a hole, so the ground shows through it.

## Colours

The colours are the tokens of Littera in `src/root.css`.

| Use | Ground | Mark colour | Token | Contrast |
|---|---|---|---|---|
| Default | Light (`#ffffff`) | `#212529` | `--text-primary`, light theme | 15.4:1 |
| Default | Dark (`#1f262e`) | `#e6e6e6` | `--text-primary`, dark theme (`hsl(0, 0%, 90%)`) | 12.2:1 |
| App icon, avatar | Tile `#212529` | `#e6e6e6` | same | 12.4:1 |
| One colour, print | White | `#000000` | none | 21:1 |
| One colour, on a photo or a dark ground | Any dark | `#ffffff` | none | 15.4:1 on `#212529` |

The rule is short:

- **On a light ground the mark is `#212529` or black.**
- **On a dark ground the mark is `#e6e6e6` or white.**

The mark has one colour. The letter is a hole: do not fill it with another colour.

## Files

| File | Use |
|---|---|
| `svg/symbol-ink.svg` | Light grounds. |
| `svg/symbol-pale.svg` | Dark grounds. |
| `svg/symbol-white.svg`, `svg/symbol-black.svg` | One colour: photos, print. |
| `svg/symbol-pixel-ink.svg`, `svg/symbol-pixel-pale.svg` | Exactly 16, 32 or 48 px. Drawn on a 16 x 16 pixel grid: the edges are sharp. |
| `svg/favicon.svg`, `favicon.ico` | Browser tab. The mark is a tile already, so it has no extra tile. The SVG follows the browser theme. |
| `svg/app-icon.svg` | Full square tile with the letter L alone in pale (no second container). The platform rounds the corners. |
| `svg/app-icon-rounded.svg` | The same tile with rounded corners, for the README header only. |
| `png/avatar-512.png` | GitHub avatar. |
| `png/apple-touch-icon-180.png` | Apple touch icon. It has a solid ground on purpose. |
| `previous/` | The logo before the redesign. Do not use it. |

## Size and clear space

- Use the main cut from 40 px up.
- At exactly 16, 32 or 48 px (or a whole multiple) use the pixel cut. In the pixel cut the thin parts of the letter are one pixel thick,
  because the hairlines of the main cut are less than a pixel at these sizes. Do not show the pixel cut at other sizes, or large.
- Smallest size: 16 px.
- Clear space: keep free space of one quarter of the mark width on every side.

## Do not

- Do not unmirror the L. The mirror is the idea of the logo.
- Do not move the letter to the middle of its box. It is placed by eye: half way between the middle of its box and its centre of mass.
- Do not round the corners of the mark. Sharp corners are part of the shape.
- Do not fill the letter with a colour.
- Do not add a gradient, a shadow or an outline.
- Do not use a mark colour that is not in the table above.
- Do not put the name in a font and call it a wordmark. The logo has no wordmark.
