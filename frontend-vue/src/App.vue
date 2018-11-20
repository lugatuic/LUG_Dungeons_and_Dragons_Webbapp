<template>
  <v-app :dark="!useLightTheme">
    <app-bar/>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import { mapState } from 'vuex';
import AppBar from '@/components/AppBar';

export default {
  name: 'App',
  components: {
    AppBar,
  },
  computed: {
    ...mapState(['useLightTheme']),
  }
}
</script>
