<template>
  <v-container>
    <!-- TODO: refactor into its own component -->
    <v-layout row>
      <v-flex>
        <dnd5e-card/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Dnd5eCard from '@/components/CharacterSelect/Dnd5eCard';
import { mapActions } from 'vuex';
export default {
  components: {
    Dnd5eCard,
  },
  methods: {
    ...mapActions('characters', ['getAll']),
    selectCharacter (char) {
      console.debug('selected character', char);
    },
  },
  data () {
    return {
      isLoading: true,
      characters: [],
    };
  },
  async mounted () {
    try {
      const characters = await this.getAll();
      this.characters = characters.slice();
    } catch (err) {
      console.error(err);
    } finally {
      this.isLoading = false;
    }
  },
};
</script>
