import Vue from 'vue';

export default {
    namespaced: true,
    state: {
        notes: [],
    },
    actions: {
        async GET_NOTES({ commit }) {
            const response = await Vue.$axios.get('/notes/');
            commit('SET_LIST', response.data);

        },
    },
    mutations: {
        SET_LIST: (state, list) => {
            state.notes = list;
        },
    },
};