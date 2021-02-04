<template>
  <div class="about">
    <span v-for="note in notes " :key="note.pk">
         <router-link :to="{ name: 'Snippet', params:{ pk: note.pk } }">{{note.pk}}</router-link>
         <br>
    </span>
    
  </div>
</template>
<script>
import { mapActions, mapState } from 'vuex';

export default {
    data: function() {
        return {
            message: "test",
        }
    },
    computed: {
         ...mapState('notes', [
        'notes',
    ]),
    },
    methods: {...mapActions('notes', [
        'GET_NOTES',
    ]),
    },
    mounted() {
        this.GET_NOTES();
    }, 
};
</script> 