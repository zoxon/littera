module.exports = ctx => {
  const cssNanoDefaults = {
    preset: "default"
  };
  const {
    env = "development",
    options: { minify = cssNanoDefaults }
  } = ctx;

  return {
    plugins: {
      autoprefixer: {
        flexbox: "no-2009",
        cascade: false,
        grid: true
      },
      "postcss-flexbugs-fixes": {},
      perfectionist: {
        cascade: false,
        colorCase: "lower",
        colorShorthand: true,
        format: "expanded",
        indentChar: " ",
        indentSize: 2,
        trimLeadingZero: false,
        trimTrailingZeros: true,
        zeroLengthNoUnit: true
      },
      cssnano: env === "production" ? minify : false,
      "postcss-reporter": {}
    }
  };
};
