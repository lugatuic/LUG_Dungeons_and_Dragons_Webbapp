<template>
  <v-app>
    <app-bar/>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import AppBar from '@/components/AppBar';

export default {
  name: 'App',
  components: {
    AppBar,
  },
  data () {
    return {
      //
    }
  }
}
</script>
