import {applyMiddleware, combineReducers, createStore} from 'redux';
import {reducer as formReducer} from 'redux-form';
import thunk from "redux-thunk";

const reducers = combineReducers({
  form: formReducer
});

const store = createStore(reducers, applyMiddleware(thunk));
export default store;