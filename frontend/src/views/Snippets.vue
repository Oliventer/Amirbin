<template>
  <div class="snippet">
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/styles/tomorrow.min.css">
      <ol>
          <li v-for="line in textSplit(snippet.code)" :key="line.pk" :id="++counter">
              <highlightjs autodetect :code="line" />
          </li>
          {{resetCounter()}}
      </ol>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
    data: function() {
         return {
             counter: 1
         }
    },
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
    },
    resetCounter() {
        this.counter = 0;
    }
    },

    mounted() {
        this.getSnippetByUrl();
    }, 
};
</script>
