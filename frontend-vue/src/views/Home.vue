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
          <v-list two-line>
            <v-list-tile v-for="(char, i) in characters" :key="i" avatar @click="selectCharacter(char)">
              <v-list-tile-avatar>
                <v-icon>person</v-icon>
              </v-list-tile-avatar>
              <v-list-tile-content>
                <!-- name -->
                <v-list-tile-title>{{ char[0] }}</v-list-tile-title>

                <!-- description -->
                <v-list-tile-sub-title>{{ char[1] }}</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-btn class="ml-0" color="success">
        <v-icon left>add</v-icon>
        Create your own
      </v-btn>
      <v-spacer/>
      <v-btn class="mr-0" color="success">
        Generate Random
        <v-icon right>casino</v-icon>
      </v-btn>
    </v-layout>
  </v-container>
</template>

<script>
// TODO: replace with actual data
const sampleCharacters = [
  ['Character 1', 'A cool character'],
  ['Character 2', 'Second is best'],
  ['Character 3', 'A description goes here'],
];
export default {
  computed: {
    characters: () => sampleCharacters,
  },
  methods: {
    selectCharacter (char) {
      console.debug('selected character', char);
    },
  },
};
</script>
