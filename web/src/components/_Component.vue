<template>
  <div class="component-">
    <UiLayout>
      <template v-slot:content>
      </template>
    </UiLayout>
  </div>
</template>

<script>
// import types from '../store/types'

import UiLayout from './UiLayout'

export default {
  name: '',

  components: { UiLayout },

  data () {
    return {}
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"
</style>
