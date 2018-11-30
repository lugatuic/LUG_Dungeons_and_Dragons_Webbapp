<template>
  <v-navigation-drawer
    app
    temporary
    :value="value"
    @input="(e) => $emit('input', e)"
    clipped>
    <v-list>
      <v-list-tile
        v-for="(link, i) in links"
        :key="i"
        :to="link.to"
        :href="link.href"
        :target="link.href && '_blank'"
        :rel="link.href && 'noopener'"
        @click="$emit('input', false)">
        <v-list-tile-action>
          <v-icon>{{ link.icon }}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>{{ link.label }}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: {
    value: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    links: () => [
      {
        to: '/',
        icon: 'dashboard',
        label: 'Home',
      },
      {
        href: 'https://lug.cs.uic.edu/',
        icon: 'android',
        label: 'LUG',
      },
    ],
  },
};
</script>
