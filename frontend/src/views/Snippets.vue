<template>
  <div class="snippet">
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/styles/tomorrow.min.css">
      <span v-for="note in notes " :key="note.pk">
          <p v-if="note.pk ===  $route.params.pk">
              <pre v-highlightjs><code>{{note.code}}</code></pre>
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