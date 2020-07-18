import types from './types'

export default {
  [types.INIT_APP] ({ commit, dispatch, state }) {
    console.log('App: Initialized')
    commit(types.INIT_HTTP)
    commit(types.INIT_RESOURCES)
    dispatch(types.FETCH_POSTS)
    dispatch(types.RECORD_HIT, { type: state.Hit.APP_VISIT })
  },

  [types.FETCH_POSTS] ({ dispatch, commit, state }) {
    return new Promise((resolve, reject) => {
      state.Post.get()
        .then((res) => {
          commit(types.SET_STATE_PROP, {
            prop: 'posts',
            val: res.data.objects,
          })
        })
        .catch((error) => { handleError(error) })
    })
  },

  [types.RECORD_HIT] ({ state }, payload) {
    state.Hit.post('record/', payload)
  },
}

function handleError (error) {
  let data
  data = error.response || error
  data = data.data || data

  console.log('ERROR:', data)
}
