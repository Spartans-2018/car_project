const HtmlWebPackPlugin = require("html-webpack-plugin");

const HtmlWebpackPluginConfig = new HtmlWebPackPlugin({
  template: './src/index.html',
  filename: './index.html',
  inject: 'body'
});

module.exports = {
  devtool: 'eval-source-map',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        pathRewrite: { '^/api': '' }
      }
    }
  },
  entry: [
    './src/styles/app.css',
    './src/js/index.js'
  ],
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },

      {
        test: /\.html$/,
        use: [
          {
            loader: "html-loader"
          }
        ]
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.(png|jpg|gif)$/,
        use: [
          {
            loader: 'file-loader',
            options: {},
          },
        ],
      },

      {
        test: /node_modules/,
        use: [
          {
          loader: 'ify-loader',
          
          }
          ]
      },
      
    ],



  },

  plugins: [
    HtmlWebpackPluginConfig
  ]
};