import React from 'react';
import {Field} from 'redux-form';

const LoginForm = ({handleSubmit, login}) => {
  return (
    <form onSubmit={handleSubmit(data => {
      login(data);
    })}>
      <Field name='username' component='input'/>
      <Field name='password' component='input'/>
      <button type='submit'>Войти</button>
    </form>
  )
}

export default LoginForm;