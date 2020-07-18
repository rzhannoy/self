<template>
  <footer class="component-footer bc-grey-bg">
    <UiLayout>
      <template v-slot:content>
        <div class="c-grey">
          © 2020, rzhannoy.com
        </div>
      </template>
    </UiLayout>
  </footer>
</template>

<script>
import UiLayout from './UiLayout'

export default {
  name: 'UiFooter',

  components: { UiLayout },

  data () {
    return {}
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"

.component-footer
  padding 25px 0

  +$mobile-only()
    padding 16px 0 25px
</style>
