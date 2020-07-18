<template>
  <div class="view-apps">
    <UiView>
      <template v-slot:content>
        <UiLayout>
          <template v-slot:content>
            <h1 class="page-title text-center mt40">
              👇 Apps 👇
            </h1>
            <div class="app-tiles">
              <AppTile/>
            </div>
            <div class="apps-outro">
              Yep, only one app here, having its own section. #yolo
            </div>
          </template>
        </UiLayout>
      </template>
    </UiView>
  </div>
</template>

<script>
import UiView from './UiView'
import UiLayout from '@/components/UiLayout'
import AppTile from '@/components/AppTile'

export default {
  name: 'Apps',

  components: {
    UiView, UiLayout,
    AppTile,
  },

  data () {
    return {}
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/vars.styl"

.app-tiles
  text-align center
  margin-top 40px

.apps-outro
  margin-top 40px
  text-align center
  color c-grey
</style>
