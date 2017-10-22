let webpack = require('webpack');
let path = require('path');
let BundleTracker = require('webpack-bundle-tracker');
let ExtractTextPlugin = require('extract-text-webpack-plugin');

let BUILD_DIR = path.resolve(__dirname, 'js');
let APP_DIR = path.resolve(__dirname, 'src/client/app');
// let SASS_DIR = path.resolve(__dirname, 'sass');

let config = {
  context: __dirname,
  entry: [
    'react-hot-loader/patch',
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/only-dev-server',
    // SASS_DIR + '/main.scss',
    APP_DIR + '/index.jsx',
  ],
  output: {
    path: BUILD_DIR,
    filename: '[name]-[hash].js',
    publicPath: 'http://localhost:3000/js'
  },
  devServer: {
    contentBase: BUILD_DIR,
    hot: true,
    port: 3000,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
      "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
    }
  },
  module: {
    rules:[{
      test: /\.jsx?/,
      include: APP_DIR,
      exclude: /node_modules/,
      use: {
        loader: 'babel-loader'
      }
    },
      { // scss loader for webpack
        test: /\.scss$/,
        use: [{
          loader: "style-loader"
        }, {
          loader: "css-loader"
        }, {
          loader: "sass-loader"
        }]
      }]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
    new BundleTracker({filename: './webpack-stats.json'})
  ],
};

module.exports = config;
