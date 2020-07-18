import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home.vue'
import Post from './views/PostView.vue'
import Apps from './views/Apps.vue'
import Confirmation from './views/Confirmation.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,

  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else if (to.hash) {
      return { selector: to.hash }
    } else {
      return { x: 0, y: 0 }
    }
  },

  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/i/apps',
      name: 'apps',
      component: Apps,
    },
    {
      path: '/i/confirm',
      name: 'confirm',
      component: Confirmation,
    },
    {
      path: '/:slug',
      name: 'post',
      component: Post,
    },
  ],
})
