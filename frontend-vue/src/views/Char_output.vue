<template>
  <v-container fluid grid-list-lg>
    <v-layout v-if="isLoading">
      <v-flex class="text-xs-center">
        <v-progress-circular indeterminate/>
        <h1 class="headline">Loading character data...</h1>
      </v-flex>
    </v-layout>
    <template v-else>
      <v-layout row wrap>
        <!-- TODO: refactor each section into its own component once sections are finalized-->
        <!-- left column -->
        <v-flex xs12 md6 d-flex>
          <v-layout column>
            <!-- top left quadrant -->
            <v-flex>
              <v-layout wrap>
                <v-flex>
                  <v-text-field
                    :value="character.name"
                    label="Name"
                    readonly/>
                </v-flex>
                <v-flex>
                  <v-text-field
                    value="some title"
                    label="Title"
                    readonly/>
                </v-flex>
              </v-layout>
              <v-layout wrap>
                <v-flex>
                  <v-text-field
                    value="some occupation"
                    label="Occupation"
                    readonly/>
                </v-flex>
                <v-flex>
                  <v-text-field
                    value="some class"
                    label="Class"
                    readonly/>
                </v-flex>
                <v-flex>
                  <v-text-field
                    value="some alignment"
                    label="Alignment"
                    readonly/>
                </v-flex>
              </v-layout>
              <!-- TODO: add more fields as necessary -->
            </v-flex>

            <!-- bottom left quadrant -->
            <v-flex>
              stats here, maybe a fancy radar chart?
            </v-flex>
          </v-layout>
        </v-flex>

        <!-- right column -->
        <v-flex xs12 md6 d-flex>
          <v-layout column>
            <!-- top right quadrant -->
            <v-flex>
              equipment cards here
            </v-flex>

            <!-- bottom right quadrant -->
            <v-flex>
              abilities and spells here
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
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
};
</script>
