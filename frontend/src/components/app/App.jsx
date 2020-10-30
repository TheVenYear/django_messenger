import React, {useEffect} from 'react';
import authAPI from '../../api/auth_api';

const App = () => {
  useEffect(() => {
    authAPI.login({
      'username': 'admin',
      'password': 'admin'
    }).then(response => {
      console.log(response);
      authAPI.me().then(response => {
      console.log(response);
      authAPI.logout().then(response => {
        console.log(response);
      });
    });
    })

  }, [])
  return (
    <div className="App">
      <header>
        Hello world
      </header>
    </div>
  );
}

export default App;
