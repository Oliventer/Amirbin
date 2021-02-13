<template>
  <div class="snippet">
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/styles/tomorrow.min.css">
      <ol>
          <li v-for="line in textSplit(snippet.code)" :key="line.pk" :id="++counter">
              <highlightjs autodetect :code="line" />
          </li>
      </ol>
      <span v-if="checkHash">
          {{setHash()}}
          {{removeClass()}}
          {{addClass()}}
      </span>
      
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
    data: function() {
         return {
             counter: 1,
             hash: "",
             prevId: "",
         }
    },
    props: {
        pk: String
    },
    computed: {
         ...mapState('snippet', [
        'snippet',
    ]),
    checkHash() {
        return this.$route.hash && this.$route.hash.split('#').pop() !== this.hash
    }
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
    },

    addClass(){
        document.getElementById(this.hash).classList.add('line-highlight');
        this.prevId = this.hash;
    },

    removeClass(){
        if (this.prevId !== ""){
            document.getElementById(this.prevId).classList.remove('line-highlight');
        }
    },

    setHash() {
        this.hash = this.$route.hash.split('#').pop();
    
    }
    },
    mounted() {
        this.getSnippetByUrl();
    },
    
    beforeUpdate() {
        this.resetCounter();
        if (this.hash !== "") {
            this.addClass();
        }
    },
};
</script>

<style lang="less">
    .line-highlight {
        background-color: #fffbdd !important;
        code {
            background-color: inherit !important;
        }
    }
    li {
        font-size: 12px;
    }

    li pre {
        font-size: 15px;
    }
    .hljs{
      padding:0em !important
  }
</style>
