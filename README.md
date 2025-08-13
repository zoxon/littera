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

[Live Demo](http://zoxon.github.io/littera/)

## 🚀 Core Features

- **Minimal & Lightweight**
  - Original size: ~5.8KB
  - Gzipped size: ~1.9KB
  - Zero dependencies
  - Vanilla CSS (no JavaScript)

- **Smart Defaults**
  - Works seamlessly with [normalize.css](https://github.com/necolas/normalize.css)
  - Beautiful typographic scale
  - Responsive design out of the box
  - System font stack for optimal performance

- **Modern CSS**
  - CSS Custom Properties for easy customization
  - Dark mode support via `prefers-color-scheme`
  - Logical properties for RTL/LTR support
  - Micro-interactions and transitions

## ⚡ Quickstart

Just include the CSS file in your project and override the default custom properties:

```html
<link href="./littera.css" rel="stylesheet" />

<!-- or -->

<style>
  @import url("./littera.css");
</style>
```

## Customization

### Typography

```css
:root {
  /* Font Families */
  --font-primary: "Helvetica Neue", sans-serif;
  --font-secondary: Georgia, serif;
  --font-monospace: "Courier New", monospace;

  /* Font Sizes */
  --font-size-base: 1rem; /* 16px */
  --font-size-h1: 2.5rem; /* 40px */
  --font-size-h2: 2rem; /* 32px */
  --font-size-h3: 1.75rem; /* 28px */
  --font-size-h4: 1.5rem; /* 24px */
  --font-size-h5: 1.25rem; /* 20px */
  --font-size-h6: 1rem; /* 16px */

  /* Line Height */
  --line-height-base: 1.618; /* Golden ratio */
}
```

### Color Scheme

```css
:root {
  /* Background Colors */
  --fill-primary: #ffffff;
  --fill-secondary: #f8f9fa;

  /* Text Colors */
  --text-primary: #212529;
  --text-accent-primary: #4263eb;
  --text-accent-secondary: #9c36b5;
  --text-accent-tertiary: #3b5bdb;
  --text-gray: #e9ecef;
  --text-gray-dark: #adb5bd;
}
```

## 📦 What's Included

- Complete typographic system
  - Headings (h1-h6)
  - Paragraphs and text elements
  - Lists (ordered, unordered, description)
  - Blockquotes and citations
- Code formatting
  - Syntax-highlighted code blocks
  - Inline code snippets
  - Pre-formatted text
- Interactive elements
  - Links with hover/focus states
  - Keyboard navigation support
  - Accessible focus indicators
- Layout components
  - Responsive tables
  - Figures and captions
  - Horizontal rules

## License

[The MIT License (MIT)](LICENSE)
