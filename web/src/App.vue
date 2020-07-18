<template>
  <div id="app">
    <router-view/>
    <notifications position="top center" :width="notificationsWidth" :max="1"/>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import types from './store/types'

export default {
  name: 'App',

  created () {
    this[types.INIT_APP]()
  },

  computed: {
    notificationsWidth () {
      if (this.isMobile) {
        return '100%'
      } else {
        return '350px'
      }
    },
  },

  methods: {
    ...mapActions([types.INIT_APP]),
  },
}
</script>

<style src="spectre.css/dist/spectre.min.css"></style>
<style src="./app.styl" lang="stylus"></style>
