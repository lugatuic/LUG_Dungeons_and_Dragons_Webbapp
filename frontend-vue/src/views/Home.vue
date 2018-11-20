<template>
  <v-container justify-center>
    <!-- TODO: refactor into its own component -->
    <v-layout row wrap>
      <v-flex xs12>
        <h1 class="headline text-xs-center">Character List</h1>
      </v-flex>
      <v-flex xs12>
        <v-list two-line>
          <v-list-tile v-for="(char, i) in characters" :key="i" avatar>
            <v-list-tile-avatar>
              <v-icon>person</v-icon>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <!-- name -->
              <v-list-tile-title>{{ char[0] }}</v-list-tile-title>

              <!-- description -->
              <v-list-tile-subtitle>{{ char[1] }}</v-list-tile-subtitle>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-flex>
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
};
</script>
