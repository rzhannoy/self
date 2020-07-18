import Vue from 'vue'

import types from './types'

import PostResource from '../resources/post'
import HitResource from '../resources/hit'
import MessageResource from '../resources/message'
import SubscriberResource from '../resources/subscriber'

const DEFAULT_NOTIFY_DURATION = 3000

export default {
  [types.SET_STATE_PROP] (state, payload) {
    state[payload.prop] = payload.val
  },

  [types.INIT_HTTP] (state) {
    const hostname = document.location.hostname
    const mediaUrl = '/media/'
    let apiUrl

    apiUrl = 'http://127.0.0.1:8000/api/'
    // if (
    //   hostname.indexOf('localhost') > -1 ||
    //   hostname.indexOf('192.168') > -1
    // ) {
    //   apiUrl = 'http://127.0.0.1:8000/api/'
    // } else {
    //   apiUrl = 'https://api.runtheinc.com/api/'
    // }

    const headers = {}

    state.conf = { apiUrl, mediaUrl, headers }
  },

  [types.INIT_RESOURCES] (state) {
    state.Post = PostResource(state.conf)
    state.Hit = HitResource(state.conf)
    state.Message = MessageResource(state.conf)
    state.Subscriber = SubscriberResource(state.conf)
  },

  [types.NOTIFY] (state, payload) {
    Vue.notify({
      text: payload.text,
      type: payload.type,
      duration: payload.duration || DEFAULT_NOTIFY_DURATION,
    })
  },
}
