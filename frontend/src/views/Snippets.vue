<template>
  <div class="snippet">
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/styles/tomorrow.min.css">
      <ol v-for="note in notes " :key="note.pk">
          <span v-if="note.pk ===  $route.params.pk">
              <li v-for="word in TextSplit(note.code)" :key="word.pk"><highlightjs autodetect :code="word" /></li>
          </span>
      </ol>
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
    TextSplit(text) {
        return text.split("\n");
    }
    },
    mounted() {
        this.GET_NOTES();
    }, 
};
</script> 