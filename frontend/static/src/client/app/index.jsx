import React from 'react';
import ReactDom from 'react-dom';
import { AppContainer } from 'react-hot-loader';
import App from './containers/app.jsx';
import '../../../sass/main.scss';
import { BrowserRouter, Route, Switch } from 'react-router-dom'


const render = Component => {
  ReactDom.render(
    <AppContainer>
        <BrowserRouter>
          <Component/>
        </BrowserRouter>
    </AppContainer>,
    document.getElementById('app')
  )
};

render(App);

// Webpack Hot Module Replacement Api
if (module.hot) {
  module.hot.accept('./containers/app.jsx', () => render(App))
}