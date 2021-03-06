import React from 'react';
import ReactDOM from 'react-dom';
import './index.sass';
import App from './components/app/App';
import reportWebVitals from './report_web_vitals';
import {Provider} from 'react-redux';
import store from './redux/store';

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App/>
    </Provider>

  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
