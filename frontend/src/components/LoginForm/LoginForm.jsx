import React from 'react';
import {Field} from 'redux-form';
import {renderTextField} from '../../utils/renderers';

const LoginForm = ({handleSubmit, login}) => {
  return (
    <form onSubmit={handleSubmit(data => {
      login(data);
    })}>
      <Field name='username' component={renderTextField}/>
      <Field name='password' component={renderTextField}/>
      <button type='submit'>Войти</button>
    </form>
  )
}

export default LoginForm;