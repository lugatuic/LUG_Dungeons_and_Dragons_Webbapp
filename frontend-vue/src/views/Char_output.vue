<template>
  <main-input-page :disableInput="true" :isLoading="isLoading" :character="character"/>
</template>

<script>
import MainInputPage from '@/components/CharacterInput/MainInputPage';
import { mapActions } from 'vuex';

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
  computed: {
    inputId () {
      return this.$route.params.id;
    },
  },
  data () {
    return {
      isLoading: true,
      character: {},
    };
  },
  methods: {
    ...mapActions('characters', ['getSingle']),
  },
  async mounted () {
    try {
      const character = await this.getSingle({ id: this.inputId });
      this.character = character;
    } catch (err) {
      console.error(err);
    } finally {
      this.isLoading = false;
    }
  },
};
</script>
