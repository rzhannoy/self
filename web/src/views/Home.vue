<template>
  <div class="view-home">
    <UiView>
      <template v-slot:content>
        <template v-if="showIntro">
          <Intro/>
          <div class="divider"></div>
        </template>
        <div class="posts">
          <Post v-for="post in posts" :key="post.id"
            :obj="post"/>
        </div>
      </template>
    </UiView>
  </div>
</template>

<script>
import { mapState } from 'vuex'

import UiView from './UiView'
import Intro from '@/components/Intro'
import Post from '@/components/Post'

export default {
  name: 'Home',

  components: {
    Intro, Post,
    UiView,
  },

  data () {
    return {}
  },

  computed: {
    ...mapState(['showIntro', 'posts']),
  },
}
</script>

<style scoped lang="stylus">
</style>
