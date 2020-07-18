import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'

import appMixin from './mixins/appMixin'

import Notifications from 'vue-notification'
import VueMeta from 'vue-meta'

Vue.config.productionTip = false

Vue.mixin(appMixin)

Vue.use(Notifications)
Vue.use(VueMeta)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
