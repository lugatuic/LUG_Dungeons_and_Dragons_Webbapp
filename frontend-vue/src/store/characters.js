import api from '@/modules/DndApi';

const state = {
  allCharacters: [],

   // TODO: remove once backend is ready for use
  useMockData: true,
};

const mutations = {
  setCharactersList (state, list = []) {
    state.allCharacters = list.slice();
  },
};

const actions = {
  async getAll ({ commit, state }, input = { storeResult: false }) {
    const characters = await api.getAllCharacters({ isMock: state.useMockData });
    if (input.storeResult) {
      commit('setCharactersList', characters);
    }
    return characters;
  },
  async getSingle ({ state }, input = { id: '' }) {
    const character = await api.getSingleCharacter(input.id, { isMock: state.useMockData });
    return character;
  },
};

export default {
  state,
  mutations,
  actions,
  namespaced: true,
};
