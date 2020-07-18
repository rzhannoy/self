<template>
  <div class="component-navbar">
    <UiLayout>
      <template v-slot:content>
        <nav class="navbar">
          <router-link v-if="displayBackLink" class="btn-back" :to="{ name: 'home' }">
            ⬅️
          </router-link>
          <router-link :to="{ name: 'home' }" class="btn btn-link btn-nav">Posts</router-link>
          <router-link :to="{ name: 'apps' }" class="btn btn-link btn-nav">Apps</router-link>
          <a href="#" class="btn btn-link btn-cta-i btn-nav"
            @click.prevent="showMessageModal = true">Message Me</a>
        </nav>
      </template>
    </UiLayout>
    <UiModal :is-open="showMessageModal" size="modal-sm"
      @close="showMessageModal = false">
      <template v-slot:content>
        <MessageForm @done="showMessageModal = false"/>
      </template>
    </UiModal>
  </div>
</template>

<script>
import UiLayout from './UiLayout'
import UiModal from './UiModal'
import MessageForm from './MessageForm'

export default {
  name: 'UiNavbar',

  components: {
    UiLayout, UiModal,
    MessageForm,
  },

  computed: {
    displayBackLink () {
      return this.$route.name !== 'home'
    },
  },

  data () {
    return {
      showMessageModal: false,
    }
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"

.component-navbar
  position fixed
  width 100%
  background-color #fff

.navbar
  position relative
  display block
  padding 25px 0
  text-align right

  +$mobile-only()
    padding 16px 0

.btn-nav
  +$mobile-only()
    display inline
    margin-left 8px
    padding-left 12px
    padding-right 12px

  @media (max-width: 340px)
    margin-left 5px
    padding-left 8px
    padding-right 8px

.btn-back
  position absolute
  left 0
  font-size 27px
  text-decoration none
  opacity .88

  +$mobile-only()
    font-size 18px

  &:hover
    opacity .7
</style>
