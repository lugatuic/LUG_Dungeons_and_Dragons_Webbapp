<template>
  <main-input-page :randomize="randomize"/>
</template>

<script>
import MainInputPage from '@/components/CharacterInput/MainInputPage';
export default {
  props: {
    randomize: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    MainInputPage,
  },
};
</script>
