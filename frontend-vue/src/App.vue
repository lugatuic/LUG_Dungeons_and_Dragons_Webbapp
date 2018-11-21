<template>
  <v-app :dark="!useLightTheme">
    <app-bar/>
    <v-content>
      <v-fade-transition mode="out-in">
        <router-view/>
      </v-fade-transition>
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

<style>
html {
  overflow: auto;
}
</style>

