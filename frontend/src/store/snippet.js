import Vue from 'vue';

export default {
    namespaced: true,
    state: {
        snippet: [],
    },
    actions: {
        async GET_SNIPPET({ commit }, pk) {
            const response = await Vue.$axios.get(`/notes/${pk}/`);
            commit('SET_SNIPPET', response.data);

        },
        POST_SNIPPET({ commit }, body) {
            return new Promise ((resolve, reject) => {
              Vue.$axios.post('/notes/', body).then(result => {
                resolve(result.data.pk)
                commit('SET_SNIPPET', result.data);
              }).catch(e => {
                console.log(e)
                reject('Something went wrong!')
              })
            })
          }
    },
    mutations: {
        SET_SNIPPET: (state, list) => {
            state.snippet = list;
        },

    },
};
