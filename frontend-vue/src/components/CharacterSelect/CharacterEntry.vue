<template>
  <v-list-tile
      avatar
      :to="`/char_output/${character.id}`">
      <v-list-tile-avatar>
        <v-icon>person</v-icon>
      </v-list-tile-avatar>
      <v-list-tile-content>
        <!-- name -->
        <v-list-tile-title>{{ character.name }}</v-list-tile-title>

        <!-- description -->
        <v-list-tile-sub-title><i v-text="character.catchphrase"/></v-list-tile-sub-title>
      </v-list-tile-content>
    </v-list-tile>
</template>

<script>
export default {
  props: {
    isPremade: {
      type: Boolean,
      default: false,
    },
    character: {
      type: Object,
      default: () => ({
        id: 'default_id',
        name: 'default_name',
        catchphrase: 'this is a default phrase',
      }),
    },
  },
};
</script>
