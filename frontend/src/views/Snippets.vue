<template>
  <div>
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/styles/tomorrow.min.css">
      <ol>
          <li v-for="line in textSplit(snippet.code)" :key="line.pk" :id="line.pk">
              <highlightjs autodetect :code="line.name" />
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
             hash: "",
             prevId: "",
         }
    },
    props: {
        pk: String,
        isCodeExist: Boolean
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
    async getSnippetByUrl() {
        await this.getSnippet(this.pk);
    },

    textSplit(code) {
        let counter = 0
        let result = code.split('\n').map(function(elem) {
            counter++
            return {"pk": counter,"name": elem};
        });
        return result
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
        if (!this.isCodeExist) {
            this.getSnippetByUrl();
        }
    },
    
    beforeUpdate() {
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
      padding:0em !important;
      background: none !important;
  }
</style>
