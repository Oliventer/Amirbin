import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'
import hljs from 'highlight.js'
import "bootstrap/dist/css/bootstrap.min.css";


Vue.$axios = axios.create();

Vue.use(hljs.vuePlugin);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
