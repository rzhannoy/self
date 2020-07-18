const path = require('path')
const routes = require('./routes.json')
const PrerenderSPAPlugin = require('prerender-spa-plugin')

module.exports = {
  configureWebpack: {
    plugins: [
      new PrerenderSPAPlugin({
        staticDir: path.join(__dirname, 'dist'),
        outputDir: path.join(__dirname, 'dist_prerendered'),
        routes,
      })
    ],
  },
}
