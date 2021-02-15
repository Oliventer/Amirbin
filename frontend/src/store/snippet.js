import Vue from 'vue';

export default {
    namespaced: true,
    state: {
        snippet: [],
        snippet_pk: String,
    },
    actions: {
        async GET_SNIPPET({ commit }, pk) {
            const response = await Vue.$axios.get(`/notes/${pk}/`);
            commit('SET_SNIPPET', response.data);

        },
        async POST_SNIPPET({commit}, data) {
            const response = await Vue.$axios.post('/notes/', data);
            commit('SET_SNIPPET_PK', response.data.pk);
        }
    },
    mutations: {
        SET_SNIPPET: (state, list) => {
            state.snippet = list;
        },
        SET_SNIPPET_PK: (state, response_pk) => {
            state.snippet_pk = response_pk
        },
    },
};
