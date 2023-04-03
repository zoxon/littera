module.exports = (ctx) => {
  const config = {
    plugins: [require("postcss-import"), require("autoprefixer")],
  };

  if (ctx.env === "production") {
    config.plugins.push(
      require("cssnano")({
        preset: "default",
      })
    );
  }

  return config;
};
