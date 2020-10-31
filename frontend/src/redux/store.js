import {applyMiddleware, combineReducers, createStore} from 'redux';
import {reducer as formReducer} from 'redux-form';
import thunk from "redux-thunk";
import authReducer from './reducers/auth_reducer';

const reducers = combineReducers({
  form: formReducer,
  auth: authReducer
});

const store = createStore(reducers, applyMiddleware(thunk));
window.store = store;
export default store;