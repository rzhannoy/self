import axios from 'axios'

export default function (conf) {
  const resource = axios.create({
    baseURL: conf.apiUrl + 'post/',
    headers: conf.headers,
  })

  return resource
}
