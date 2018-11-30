<template>
  <v-app :dark="!useLightTheme">
    <app-bar v-model="showSidebar"/>
    <side-bar v-model="showSidebar"/>
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
import SideBar from '@/components/SideBar';

export default {
  name: 'App',
  components: {
    AppBar,
    SideBar,
  },
  computed: {
    ...mapState(['useLightTheme']),
  },
  data: () => ({
    showSidebar: false,
  }),
};
</script>

<style>
html {
  overflow: auto;
}
</style>

