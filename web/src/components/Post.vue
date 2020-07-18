<template>
  <div class="component-post">
    <UiLayout :colSize="colSize">
      <template v-slot:content>
        <h2 class="h3">
          <router-link :to="linkParams" v-if="isTeaser" class="post-title-link">{{ obj.title }}</router-link>
          <template v-else>{{ obj.title }}</template>
        </h2>
        <div class="post-meta c-grey">
          {{ createdAt }}
        </div>
        <div class="post-content content">
          <div v-if="isTeaser" v-html="obj.teaser"></div>
          <div v-else v-html="obj.content"></div>
        </div>
        <div v-if="isTeaser" class="post-actions">
          <router-link :to="linkParams">
            Read more
          </router-link>
        </div>
      </template>
    </UiLayout>
  </div>
</template>

<script>
import UiLayout from './UiLayout'

export default {
  name: 'Post',

  props: {
    mode: { type: String, default: 'teaser' },
    obj: { type: Object, required: true },
  },

  components: { UiLayout },

  data () {
    return {}
  },

  computed: {
    isTeaser () {
      return this.mode === 'teaser'
    },

    colSize () {
      return this.isTeaser ? 'col-8' : 'col-7'
    },

    createdAt () {
      const date = new Date(this.obj.created)
      return date.toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },

    linkParams () {
      return { name: 'post', params: { slug: this.obj.slug } }
    },
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"

.component-post
  padding-top 80px

  +$mobile-only()
    padding-top 40px

.post-meta
  margin-bottom 18px

.post-content >>>
  p
    line-height 1.75 !important

.post-actions
  +$mobile-only()
    margin-top -5px

  a
    font-weight bold
    color #000
    text-transform uppercase

.post-title-link
  color #000
  text-decoration none

  &:hover
    color c-grey-dark
</style>
