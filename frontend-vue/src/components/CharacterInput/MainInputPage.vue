<template>
  <v-container grid-list-lg>
    <v-layout v-if="isLoading">
      <v-flex class="text-xs-center">
        <v-progress-circular indeterminate/>
        <h1 class="headline">Loading character data...</h1>
      </v-flex>
    </v-layout>
    <template v-else>
      <v-layout>
        <v-flex>
          <input-card :disableInput="disableInput">
            <h1 slot="title">System</h1>
            <v-container fluid class="pt-0">
              <v-select
                :disabled="disableInput"
                placeholder="Select a system"
                :items="['D&D 5e', 'D&D 4e', 'Reality']"/>
            </v-container>
          </input-card>
        </v-flex>
      </v-layout>
      <!-- TODO: move each input card into its own component? -->
      <v-layout>
        <v-flex>
          <input-card :onRandomizeButtonClick="randomizeGeneralCard" :disableInput="disableInput">
            <h1 slot="title">General</h1>
            <v-container fluid grid-list-lg class="pt-0">
              <v-layout wrap>
                <v-flex>
                  <v-text-field :disabled="disableInput" label="Name"/>
                </v-flex>
                <v-flex>
                  <v-text-field :disabled="disableInput" label="Catchphrase"/>
                </v-flex>
                <v-flex>
                  <v-select
                    :disabled="disableInput"
                    label="Alignment"
                    :items="allAlignments"/>
                </v-flex>
              </v-layout>
              <v-layout>
                <v-flex>
                  <v-textarea
                    :disabled="disableInput"
                    label="Backstory" outline/>
                </v-flex>
              </v-layout>
            </v-container>
          </input-card>
        </v-flex>
      </v-layout>
      <!-- TODO: add more cards -->
    </template>
  </v-container>
</template>

<script>
import InputCard from '@/components/CharacterInput/InputCard';
export default {
  props: {
    randomize: {
      type: Boolean,
      default: false,
    },
    disableInput: {
      type: Boolean,
      default: false,
    },
    character: {
      type: Object,
    },
    isLoading: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    InputCard,
  },
  computed: {
    allAlignments () {
      const result = [];
      ['Good', 'Neutral', 'Evil'].forEach(baseAlignment => {
        ['Lawful', 'Neutral', 'Chaotic'].forEach(modifier => {
          const name = baseAlignment !== modifier
            ? [modifier, baseAlignment]
            : [baseAlignment];
          result.push({
            text: name.join(' '),
            value: name.map(n => n.toLowerCase()).join('-'),
          });
        });
      });
      return result;
    },
  },
  methods: {
    randomizeGeneralCard () {
      // ideally, this would be in its own component
      console.warn('TODO: input card randomize');
    },
  },
  mounted () {
    if (this.randomize) {
      // TODO: randomize fields
      console.warn('TODO: randomize all data');
    }
  },
};
</script>
