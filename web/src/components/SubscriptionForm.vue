<template>
  <div class="component-subscription-form">
    <UiLayout colSize="col-7">
      <template v-slot:content>
        <div class="divider"></div>
        <h4 class="h4">Subscribe to receive notifications</h4>
        <h4 class="h4-sub">0.8 emails/month sent on average</h4>
        <form class="subscription-form">
          <div class="subscription-input-wrapper">
            <input v-model="objData.email" v-if="step === 1" type="email" class="subscription-input" placeholder="Email">
            <input v-model="objData.name" v-else type="text" class="subscription-input" placeholder="Name" ref="inputName">
            <button type="submit" @click.prevent="handleSubmit" class="btn btn-link">
              <template v-if="step === 1">Subscribe</template>
              <template v-else>Confirm</template>
            </button>
          </div>
        </form>
      </template>
    </UiLayout>
  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
import types from '../store/types'

import UiLayout from './UiLayout'

export default {
  name: 'SubscriptionForm',

  components: { UiLayout },

  data () {
    return {
      step: 1,
      objData: {},
    }
  },

  computed: {
    ...mapState(['Subscriber']),
  },

  methods: {
    handleSubmit () {
      if (this.step === 1) {
        if (!this.objData.email) {
          this[types.NOTIFY]({ type: 'error', text: 'Please enter your email' })
        } else {
          this.step = 2
          this.$nextTick(() => this.$refs.inputName.focus())
        }
      } else {
        if (!this.objData.name) {
          this[types.NOTIFY]({ type: 'error', text: 'Please enter your name' })
        } else {
          this.Subscriber.post('register/', this.objData)
            .then(res => {
              // console.log('handleSubmit', res.data)
              if (res.data.success) {
                this[types.NOTIFY]({
                  type: 'success',
                  text: `Thanks! You'll be notified once new article's added`,
                })
              } else {
                this[types.NOTIFY]({
                  type: 'error',
                  text: res.data.message,
                  duration: 4000,
                })
              }

              this.step = 1
              this.objData = {}
            })
        }
      }
    },

    ...mapMutations([types.NOTIFY]),
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"

.divider
  margin 35px 0 50px

  +$mobile-only()
    margin 20px 0 35px

.subscription-form
  margin-top 25px

  +$mobile-only()
    margin-top 20px

.subscription-input
  display block
  width 100%
  line-height 1.66
  padding 12px 25px
  background-color c-grey-bg
  border 0
  border-radius 7px
  outline none

  +$mobile-only()
    padding-left 16px
    padding-right 16px

  &::placeholder
    color c-black

.subscription-input-wrapper
  position relative

  +$desktop-only()
    max-width 600px

  .btn
    position absolute
    top 8px
    right 25px
    font-weight bold
    color c-primary

    +$mobile-only()
      right 12px

    &:hover
      color c-primary-dark

.form-tsp
  margin-top 8px
  font-size 14px
  // font-style italic
  color c-grey
</style>
