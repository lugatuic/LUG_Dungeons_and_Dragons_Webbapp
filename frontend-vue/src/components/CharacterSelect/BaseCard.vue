<template>
  <v-card raised>
    <v-card-title>
      <h1 class="headline">{{ systemName }} Characters</h1>
    </v-card-title>
    <div v-if="isLoading" class="text-xs-center pa-3">
      <v-progress-circular indeterminate/>
    </div>
    <v-list two-line v-else>
      <character-entry
        v-for="(pChar, i) in premadeCharacters"
        :key="`premade-${i}`"
        :isPremade="true"
        :character="pChar"
        @click="selectCharacter(pChar)"/>

      <character-entry
        v-for="(char, i) in playerCharacters"
        :key="`player-${i}`"
        :isPremade="true"
        :character="char"
        @click="selectCharacter(char)"/>
    </v-list>
    <v-card-actions>
      <v-btn
        :to="createNewPlayerLink"
        class="ml-0"
        color="green darken-2 white--text">
        <v-icon left>add</v-icon>
        Create your own
      </v-btn>
      <v-spacer/>
      <v-btn
        :to="createRandomPlayerLink"
        class="mr-0"
        color="green darken-2 white--text">
        Generate Random
        <v-icon right>casino</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import CharacterEntry from './CharacterEntry';

export default {
  props: {
    systemName: {
      type: String,
      default: "DEFAULT_SYSTEM_NAME",
    },
    isLoading: {
      type: Boolean,
      default: false,
    },
    premadeCharacters: {
      type: Array,
      default: () => [],
    },
    playerCharacters: {
      type: Array,
      default: () => [],
    },
    createNewPlayerLink: {
      type: String,
      default: '/char_input',
    },
    createRandomPlayerLink: {
      type: String,
      default: '/char_input?randomize=true',
    },
  },
  components: {
    CharacterEntry,
  },
  methods: {
    selectCharacter (char) {
      console.debug('selected character', char);
    },
  },
};
</script>
