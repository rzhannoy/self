<template>
  <div class="component-app-tile">
    <a href="https://devdb.io" class="tile-wrapper" target="_blank">
      <div class="h3 tile-title">
        devdb.io
      </div>
      <div class="tile-description">
        CV/LP builder for developers
      </div>
      <div class="tile-meta">
        248 users
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: 'AppTile',

  data () {
    return {}
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"

.tile-wrapper
  display inline-block
  background-color c-grey-bg
  padding 30px 80px
  border-radius 12px
  text-align left
  text-decoration none
  color c-black

  +$mobile-only()
    text-align center
    width 100%
    padding 25px 40px

  &:hover
    background-color c-primary-bg

.tile-description
  margin-top 16px

.tile-meta
  margin-top 8px
  color c-grey-dark
</style>
