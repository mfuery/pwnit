var webpack = require('webpack');
var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');

var BUILD_DIR = path.resolve(__dirname, 'js');
var APP_DIR = path.resolve(__dirname, 'src/client/app');

var config = {
  context: __dirname,
  entry: APP_DIR + '/index.jsx',
  output: {
    path: BUILD_DIR,
    filename: '[name]-[hash].js'
  },
  module: {
    loaders: [
      {
        test: /\.jsx?/,
        include: APP_DIR,
        exclude: /node_modules/,
        loader: 'babel-loader'
      }
    ]
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],
};

module.exports = config;
