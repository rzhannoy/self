<template>
  <div class="view-wrapper">
    <UiNavbar class="z1"/>
    <div class="view-content" :style="{ minHeight: `${this.layoutHeight}px` }">
      <slot name="content"></slot>
      <div class="view-end"></div>
    </div>
    <UiFooter/>
  </div>
</template>

<script>
import UiNavbar from '@/components/UiNavbar'
import UiFooter from '@/components/UiFooter'

export default {
  name: 'UiView',

  components: { UiNavbar, UiFooter },

  data () {
    return {
      layoutHeight: 0,
    }
  },

  created () {
    this.setLayoutHeight()
  },

  methods: {
    setLayoutHeight () {
      this.$nextTick(() => {
        const footerHeight = this.isMobile ? 65 : 74
        this.layoutHeight = window.innerHeight - footerHeight
      })
    },
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"

.view-content
  padding-top 80px

  +$mobile-only()
    padding-top 55px

.view-end
  padding-top 80px

  +$mobile-only()
    padding-top 50px
</style>
