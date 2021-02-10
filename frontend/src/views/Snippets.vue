<template>
  <div class="snippet">
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/styles/tomorrow.min.css">
      <ol>
          <li v-for="line in textSplit(snippet.code)" :key="line.pk">
              <highlightjs autodetect :code="line" />
          </li>
      </ol>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
    props: ['pk'],
    computed: {
         ...mapState('snippet', [
        'snippet',
    ]),
    },
    
    methods: {
        ...mapActions('snippet', 
    { getSnippet: 'GET_SNIPPET',
    }),
    getSnippetByUrl() {
        this.getSnippet(this.pk);
    },
    textSplit(code) {
        return code.split('\n');
    }
    },

    mounted() {
        this.getSnippetByUrl();
    }, 
};
</script>