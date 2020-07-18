import axios from 'axios'

export default function (conf) {
  const resource = axios.create({
    baseURL: conf.apiUrl + 'subscriber/',
    headers: conf.headers,
  })

  return resource
}
