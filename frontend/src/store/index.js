import Vue from 'vue'
import Vuex from 'vuex'

import notes from './notes';
import snippet from './snippet'
import stripe_key from './subscription'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
      notes,
      snippet,
      stripe_key,
  }
})
