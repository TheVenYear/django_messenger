import {stopSubmit} from 'redux-form';

import authAPI from '../../api/auth_api';

const SET_USER = 'auth/SET_USER';

const initialState = {
  user: {},
}

const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_USER:
      return {...state, user: action.payload}

    default:
      return state;
  }
}

export default authReducer;

const setUserAC = data => ({
  type: SET_USER,
  payload: data
});

export const login = data => dispatch => {
  authAPI.login(data).then(response => {
    if (response.status === 200) {
      dispatch(setUserAC(response.data));
    }
    else if (response.status === 400) {
      console.log(response);
      dispatch(stopSubmit('login', {
        _error: response.data['non_field_errors'],
        username: response.data.username,
        password: response.data.password
      }))
    }
  });
}