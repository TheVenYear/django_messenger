import instance, {packResponse} from './instance';

const authAPI = {
  me: () => (
    packResponse(instance.get('me/'))
  ),
  login: (data) => (
    packResponse(instance.post('login/', data))
  ),
  logout: () => (
    packResponse(instance.delete('logout/'))
  )
}

export default authAPI;