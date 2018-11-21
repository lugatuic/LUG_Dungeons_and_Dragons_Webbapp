<template>
  <v-container grid-list-lg>
    <v-layout>
      <v-flex>
        <input-card>
          <h1 slot="title">System</h1>
          <v-container fluid class="pt-0">
            <v-select
              placeholder="Select a system"
              :items="['D&D 5e', 'D&D 4e', 'Reality']"/>
          </v-container>
        </input-card>
      </v-flex>
    </v-layout>
    <!-- TODO: move each input card into its own component? -->
    <v-layout>
      <v-flex>
        <input-card :onRandomizeButtonClick="randomizeGeneralCard">
          <h1 slot="title">General</h1>
          <v-container fluid grid-list-lg class="pt-0">
            <v-layout wrap>
              <v-flex>
                <v-text-field label="Name"/>
              </v-flex>
              <v-flex>
                <v-text-field label="Catchphrase"/>
              </v-flex>
              <v-flex>
                <v-select
                  label="Alignment"
                  :items="allAlignments"/>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex>
                <v-textarea label="Backstory" outline/>
              </v-flex>
            </v-layout>
          </v-container>
        </input-card>
      </v-flex>
    </v-layout>
    <!-- TODO: add more cards -->
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
