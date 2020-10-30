import Axios from 'axios';

const instance = Axios.create({
  baseURL: 'api/v1/',
  withCredentials: true,
  validateStatus: status => status < 500
});

export const packResponse = (promise) => (
  promise.then(response => ({
    data: response.data,
    status: response.status
  }))
);

export default instance;