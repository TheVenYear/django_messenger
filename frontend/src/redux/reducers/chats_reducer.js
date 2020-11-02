import {stopSubmit} from 'redux-form';

const initialState = {
  chats: null,
  count: null,
  next: null,
  previous: null
}

const chatsReducer = (state = initialState, action) => {
  switch (action.type) {
    default:
      return state;
  }
}

export default chatsReducer;