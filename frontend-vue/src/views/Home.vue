<template>
  <v-container>
    <!-- TODO: refactor into its own component -->
    <v-layout row>
      <v-flex>
        <v-card raised>
          <v-card-title>
            <v-spacer/>
            <h1 class="headline">Select a Character</h1>
            <v-spacer/>
          </v-card-title>
          <v-divider/>
          <div v-if="isLoading" class="text-xs-center pa-3">
            <v-progress-circular indeterminate/>
          </div>
          <v-list two-line v-else>
            <v-list-tile
              v-for="(char, i) in characters"
              :key="i"
              avatar
              :to="`/char_output/${char.id}`"
              @click="selectCharacter(char)">
              <v-list-tile-avatar>
                <v-icon>person</v-icon>
              </v-list-tile-avatar>
              <v-list-tile-content>
                <!-- name -->
                <v-list-tile-title>{{ char.name }}</v-list-tile-title>

                <!-- description -->
                <v-list-tile-sub-title><i v-text="char.catchphrase"/></v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-btn
        to="/char_input"
        class="ml-0"
        color="green darken-2 white--text">
        <v-icon left>add</v-icon>
        Create your own
      </v-btn>
      <v-spacer/>
      <v-btn
        to="/char_input?randomize=true"
        class="mr-0"
        color="green darken-2 white--text">
        Generate Random
        <v-icon right>casino</v-icon>
      </v-btn>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';
export default {
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
