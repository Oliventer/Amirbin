<template>
  <div class="snippet">
      <span v-for="note in notes " :key="note.pk">
          <p v-if="note.pk ===  $route.params.pk">
              <pre v-html="note.code"></pre>
          </p>
      </span>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
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