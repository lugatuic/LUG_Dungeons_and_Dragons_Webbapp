import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    useLightTheme: false,
  },
  mutations: {
    setLightThemeUsage (state, useLightTheme) {
      state.useLightTheme = !!useLightTheme;
    },
  },
  actions: {

  },
});
