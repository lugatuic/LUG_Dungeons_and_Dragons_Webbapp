<template>
  <v-card>
    <v-card-title>
      <v-flex>
        <slot name="title">The Card Title</slot>
      </v-flex>
      <v-spacer/>
      <v-btn icon @click="onRandomizeButtonClick">
        <v-icon>casino</v-icon>
      </v-btn>
    </v-card-title>
    <slot name="default">
      Card content goes here
    </slot>
  </v-card>
</template>

<script>
export default {
  props: {
    onRandomizeButtonClick: {
      type: Function,
      default: () => console.debug('randomize button clicked')
    },
  },
};
</script>
