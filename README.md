<p align="center">
  <img src="./logo.svg" width="92" height="170" alt="Littera" />
</p>

<h1 align="center">
  Littera
</h1>

<p align="center">
  <em>Nano typographic framework</em>
</p>

## Demo

[zoxon.github.io/littera](http://zoxon.github.io/littera/)

## Core features

- Work with [normalize.css](https://github.com/necolas/normalize.css)
- ~2593 bytes (gzipped size: 991 bytes)
- Vanilla CSS with minimal [postcss](https://postcss.org/) plugins

## Quickstart

```html
<link href="./littera.css" rel="stylesheet" />

or

<style>
  @import url("./littera.css");
</style>
```

You can customize fonts and colors using following custom properties

### Font

- `--font-primary` - font family for all text
- `--font-monospace` - mono font family
- `--font-size-base` - base font size
- `--line-height` - base line height
- `--font-secondary` - headings font
- `--font-size-h1` - `<h1>` font size
- `--font-size-h2` - `<h2>` font size
- `--font-size-h3` - `<h3>` font size
- `--font-size-h4` - `<h4>` font size
- `--font-size-h5` - `<h5>` font size
- `--font-size-h6` - `<h6>` font size

### Fill

- `--fill-primary` - base background color
- `--fill-secondary` - secondary background color

### Text colors

- `--text-primary` - all text font color
- `--text-accent-primary` - font color for accent elements (like links, buttons etc.)
- `--text-accent-secondary` - secondary font color for accent elements
- `--text-accent-tertiary` - tertiary font color for accent elements
- `--text-gray` - light grey color
- `--text-gray-dark` - dark grey color

## License

[The MIT License (MIT)](LICENSE)
