<template>
  <base-card
    systemName="DND 5e"
    :isLoading="isLoading"
    :premadeCharacters="characters"
    :playerCharacters="characters"
    createNewPlayerLink="/char_input?system=dnd5e"
    :createRandomPlayerLink="'/char_input?system=dnd5e&randomize=true'"/>
</template>

<script>
import BaseCard from '@/components/CharacterSelect/BaseCard';
import { mapActions } from 'vuex';

export default {
  components: {
    BaseCard,
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
  methods: {
    ...mapActions('characters', ['getAll']),
  },
};
</script>
