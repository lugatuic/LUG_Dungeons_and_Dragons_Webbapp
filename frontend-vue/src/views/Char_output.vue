<template>
  <v-container fluid>
    <v-layout v-if="isLoading">
      <v-flex class="text-xs-center">
        <v-progress-circular indeterminate/>
        <h1 class="headline">Loading character data...</h1>
      </v-flex>
    </v-layout>
    <template v-else>
      <v-layout row wrap>
        <!-- left column -->
        <v-flex xs12 md6 d-flex>
          <v-layout column>
            <v-flex>
              general info here
            </v-flex>
            <v-flex>
              stats here
            </v-flex>
          </v-layout>
        </v-flex>

        <!-- right column -->
        <v-flex xs12 md6 d-flex>
          <v-layout column>
            <v-flex>
              equipment here
            </v-flex>
            <v-flex>
              abilities and spells here
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>

      <!-- TODO: refactor each section into its own component -->
      <!-- left column -->
      

      <!-- right column -->
      
    </template>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';
export default {
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
}
</script>
