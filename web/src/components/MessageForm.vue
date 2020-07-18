<template>
  <div class="component-message-form">
    <div class="h4 form-title">
      Drop me a line
    </div>
    <form class="message-form">
      <div class="form-group">
        <input v-model="objData.info" type="text" class="form-input" placeholder="Contact info (optional)">
      </div>
      <div class="form-group">
        <textarea v-model="objData.content" class="form-input" placeholder="Message" rows="8"></textarea>
      </div>
      <div class="form-actions">
        <button type="submit" class="btn btn-cta-i btn-fw"
          @click.prevent="handleSubmit">
          Send
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import types from '../store/types'

export default {
  name: 'MessageForm',

  data () {
    return {
      objData: {},
    }
  },

  computed: {
    ...mapState(['Message']),
  },

  methods: {
    handleSubmit () {
      if (this.objData.content) {
        this.Message.post('', this.objData)
          .then(() => {
            this[types.NOTIFY]({
              text: 'Sent &nbsp;👍',
              type: 'success',
              duration: 1200,
            })
            this.$emit('done')
          })
      }
    },

    ...mapMutations([types.NOTIFY]),
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"

.form-title
  margin-bottom 16px

.form-actions
  margin-bottom 16px

  .btn
    font-weight 600
    padding-top 12px
    padding-bottom 12px
    height auto
    font-size 18px
</style>
