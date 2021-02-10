import Vue from 'vue';

export default {
    namespaced: true,
    state: {
        snippet: [],
    },
    actions: {
        async GET_SNIPPET({ commit }, pk) {
            const response = await Vue.$axios.get(`/notes/${pk}/`);
            commit('SET_LIST', response.data);

        },
    },
    mutations: {
        SET_LIST: (state, list) => {
            state.snippet = list;
        },
    },
};