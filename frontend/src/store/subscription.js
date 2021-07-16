import Vue from 'vue';

export default {
    namespaced: true,
    state: {
        stripe_key: [],
        status_code: [],
        stripe_session_id: [],
    },
    actions: {
        async GET_SUBSCRIPTION_KEY({ commit }) {
            const response = await Vue.$axios.get('/subscribe/key/');
            commit('SET_STRIPE_KEY', response.data['stripe_key']);

        },
        async BUY_SUBSCRIPTION({ commit }, product_id) {
            return new Promise ((resolve, reject) => {
                Vue.$axios.post('/subscribe/' + product_id + '/').then(result => {
                  resolve(result)
                  commit('SET_STATUS_CODE', result.status);
                  commit('SET_SESSION_ID', result.data['sessionId']);
                }).catch(e => {
                  console.log(e)
                  reject('Something went wrong!')
                })
              })
          }
    },
    mutations: {
        SET_STRIPE_KEY: (state, data) => {
            state.stripe_key = data;
        },
        SET_STATUS_CODE: (state, status) => {
            state.status_code = status;
        },
        SET_SESSION_ID: (state, session) => {
            state.stripe_session_id = session;
        },
    },
};