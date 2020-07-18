<template>
  <div class="component-intro">
    <UiLayout>
      <template v-slot:content>
        <div class="wrapper-intro">
          <button @click="setStateProp({ prop: 'showIntro', val: false })"
            class="btn btn-link btn-close">✕</button>
          <h2 class="h2">
            Hi there 👋
          </h2>
          <div class="content-hero">
            I’m Nick, a software dev hacking together some apps and posting here in the free time.
            <a class="link-muted" href="">More.</a>
          </div>
        </div>
      </template>
    </UiLayout>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import types from '../store/types'

import UiLayout from './UiLayout'

export default {
  name: 'Intro',

  components: { UiLayout },

  data () {
    return {}
  },

  methods: {
    ...mapMutations([types.SET_STATE_PROP]),
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"

h2
  margin-bottom 15px

.wrapper-intro
  position relative

.component-intro
  padding-top 75px
  padding-bottom 100px

  +$mobile-only()
    padding 40px 0

.btn-close
  top 8px
  padding 5px 8px
  height auto
  font-size 20px
</style>
