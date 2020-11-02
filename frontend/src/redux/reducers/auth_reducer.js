import {stopSubmit} from 'redux-form';

import authAPI from '../../api/auth_api';

const SET_USER = 'auth/SET_USER';

const initialState = {
  user: null,
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
    if (response['status_code'] === 200) {
      dispatch(setUserAC(response.data));
    }
    else if (response['status_code'] === 400) {
      dispatch(stopSubmit('login', {
        _error: response.messages['non_field_errors'],
        username: response.messages.username,
        password: response.messages.password
      }))
    }
  });
}