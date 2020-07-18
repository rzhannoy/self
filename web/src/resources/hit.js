import axios from 'axios'

export default function (conf) {
  const resource = axios.create({
    baseURL: conf.apiUrl + 'hit/',
    headers: conf.headers,
  })

  resource.APP_VISIT = 1
  resource.POST_VIEW = 2

  return resource
}
