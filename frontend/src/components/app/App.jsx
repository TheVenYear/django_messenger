import React from 'react';
import LoginFormContainer from '../LoginForm/LoginFormContainer';
import {connect} from 'react-redux';

const App = ({user}) => {
  return (
    <div className="App">
      <LoginFormContainer/>
    </div>
  );
}

const mapStateToProps = state => ({
  user: state.auth.user
})

export default connect(mapStateToProps, {})(App);
