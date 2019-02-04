<template>
  <v-toolbar app>
    <v-toolbar-side-icon @click="$emit('input', !value)"/>
    <v-toolbar-title class="headline text-uppercase">
      <span>LUG</span>
      <span class="font-weight-light" v-text="'D&D Web App'"/>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon flat @click="toggleLightTheme">
      <v-icon>invert_colors</v-icon>
    </v-btn>
    <v-btn flat>
      <span class="mr-2">Login</span>
      <v-icon>person</v-icon>
    </v-btn>
  </v-toolbar>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
  props: {
    value: {
      type: Boolean,
    },
  },
  methods: {
    ...mapMutations(['setLightThemeUsage']),
    toggleLightTheme () {
      this.setLightThemeUsage(!this.$store.state.useLightTheme);
    },
  },
};
</script>
