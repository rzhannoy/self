<template>
  <div class="view-post">
    <UiView>
      <template v-slot:content>
        <Post v-if="post" :obj="post" mode="full"/>
        <SubscriptionForm/>
      </template>
    </UiView>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import types from '../store/types'

import UiView from './UiView'

import Post from '@/components/Post'
import SubscriptionForm from '@/components/SubscriptionForm'

export default {
  name: 'PostView',

  components: {
    UiView, Post,
    SubscriptionForm,
  },

  watch: {
    posts () { this.initPost() },
  },

  data () {
    return {
      post: {},
    }
  },

  created () {
    this.initPost()
  },

  // metaInfo () {
  //   return {
  //     title: this.dummy.description,
  //     meta: [
  //       {
  //         name: 'description',
  //         content: this.dummy.description,
  //       },
  //     ],
  //   }
  // },

  computed: {
    slug () {
      return this.$route.params.slug
    },

    ...mapState(['posts', 'Hit']),
  },

  methods: {
    initPost () {
      this.post = this.posts.find(obj => obj.slug === this.slug)

      if (this.post) {
        this[types.RECORD_HIT]({
          type: this.Hit.POST_VIEW,
          post_id: this.post.id,
        })
      }
    },

    ...mapActions([types.RECORD_HIT]),
  },
}
</script>

<style scoped lang="stylus">
</style>
