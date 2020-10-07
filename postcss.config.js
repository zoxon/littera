module.exports = (ctx) => {
  const config = {
    plugins: [
      require("postcss-import"),
      require("autoprefixer")({
        flexbox: "no-2009",
        cascade: false,
        grid: true,
      }),
      require("postcss-flexbugs-fixes"),
    ],
  };

  if (ctx.env === "production") {
    config.plugins.push(
      require("cssnano")({
        preset: "default",
      })
    );
  }

  config.plugins.push(require("postcss-reporter"));

  return config;
};
