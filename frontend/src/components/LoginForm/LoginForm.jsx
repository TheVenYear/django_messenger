import React from 'react';
import {Field} from 'redux-form';
import {renderTextField} from '../../utils/renderers';
import {Button, FormLabel, Box} from '@material-ui/core';

const LoginForm = ({handleSubmit, login, error, user}) => {
  return (
    <form onSubmit={handleSubmit(data => {
      login(data);
    })}>
      <Box m={1}>
        <FormLabel>
          {user && <div>Вы вошли как {user.email}</div>}
          {!user && <div>Вы не вошли</div>}
        </FormLabel>
      </Box>
      <Box m={1}>
        <Field name='username' variant='outlined' component={renderTextField}/>
      </Box>
      <Box m={1}>
        <Field name='password' type='password' variant='outlined' component={renderTextField}/>
      </Box>
      <Box m={1}>
        <Button type='submit'>Войти</Button>
      </Box>
      {error && <FormLabel color='primary'>{error}</FormLabel>}
    </form>
  )
}

export default LoginForm;