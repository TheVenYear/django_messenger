import instance, {packResponse} from './instance';

const chatsAPI = (limit = 10, page = 1) => ({
  chats: packResponse(instance.get(`chats/chats?limit=${limit}&offset=${page}`)),
})

export default chatsAPI;