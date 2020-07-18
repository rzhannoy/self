<template>
  <div class="component-layout container grid-xl">
    <div class="columns">
      <div class="column col-mx-auto"
        :class="[ colSize ]">
        <slot name="content"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UiLayout',

  props: {
    colSize: { type: String, default: 'col-8' },
  },

  data () {
    return {}
  },
}
</script>

<style scoped lang="stylus">
</style>
