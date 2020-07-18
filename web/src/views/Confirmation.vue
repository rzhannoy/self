<template>
  <div class="view-confirm">
    Confirming your email ...
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import types from '../store/types'

export default {
  name: 'Confirmation',

  data () {
    return {}
  },

  created () {
    this.handleConfirmation()
  },

  computed: {
    ...mapState(['Subscriber']),
  },

  methods: {
    handleConfirmation () {
      const query = this.$route.query

      if (query.token) {
        this.Subscriber.post('confirm/', query)
          .then(res => {
            if (res.data.success) {
              this.$router.push({ name: 'home' })
              this[types.NOTIFY]({
                type: 'success',
                text: 'Thanks for subscribing!',
                duration: 2000,
              })
            }
          })
      }
    },

    ...mapMutations([types.NOTIFY]),
  },
}
</script>

<style scoped lang="stylus">
.view-confirm
  text-align center
  padding-top 40px
  font-weight 600
</style>
