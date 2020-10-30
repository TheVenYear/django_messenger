import Axios from 'axios';
import Cookies from 'js-cookie';

const instance = Axios.create({
  baseURL: 'api/v1/',
  withCredentials: true,
  validateStatus: status => status < 500
});

instance.interceptors.request.use((request) => {
  request.headers['X-CSRFToken'] = Cookies.get('csrftoken');
  return request;
});

export const packResponse = (promise) => (
  promise.then(response => ({
    data: response.data,
    status: response.status
  }))
);

export default instance;