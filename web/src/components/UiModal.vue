<template>
  <div class="component-modal">
    <div v-if="isOpen" class="modal active" :class="[ size ]">
      <a href="#close" class="modal-overlay" aria-label="Close"
        @click.prevent="close"></a>
      <div class="modal-container">
        <div v-if="showHeader" class="modal-header">
          <a href="#close" class="btn btn-clear float-right" aria-label="Close"
            @click.prevent="close"></a>
        </div>
        <div class="modal-body">
          <slot name="content"></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UiModal',

  props: {
    isOpen: { type: Boolean },
    showHeader: { type: Boolean, default: true },
    size: { type: String, default: 'm' },
  },

  methods: {
    close () { this.$emit('close') },
  }
}
</script>

<style scoped lang="stylus">
.modal-container
  border-radius 6px

.modal-header
  padding-bottom 0

.modal-body
  padding-top 0px
</style>
