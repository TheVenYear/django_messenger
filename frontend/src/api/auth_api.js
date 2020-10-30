import instance, {packResponse} from './instance';

const authAPI = {
  me: () => (
    packResponse(instance.get('auth/me/'))
  ),
  login: (data) => (
    packResponse(instance.post('auth/login/', data))
  ),
  logout: () => (
    packResponse(instance.delete('auth/logout/'))
  )
}

export default authAPI;