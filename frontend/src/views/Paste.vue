<template>
    <div>
        <br>
        <span>Code:</span>
        <br>
        <textarea v-model="body.code" placeholder="paste code here"></textarea>
        <br><br>
        <span>Delete after viewing:  </span>
        <input type="checkbox" id="checkbox" v-model="body.delete_after_viewing">
        <br><br>
        <span>Language:</span>
        <br>
        <select v-model="body.language">
            <option :value="python">Python</option>
            <option :value="js">JavaScript</option>
        </select>
        <br><br>
        <span>Style:</span>
        <br>
        <select v-model="body.style">
            <option>friendly</option>
            <option>native</option>
        </select>
        <br><br><br>
        <button v-on:click="notePost()">Post</button>
        <button v-on:click="$router.push({ name: 'Snippet', params:{ pk: snippet_pk } })">To code</button>
    </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
    data: function() {
        return {
            body: {
                code: '',
                delete_after_viewing: false,
                delete_time: null,
                language: '',
                style: ''
            },
        }
    },
    computed: {
        ...mapState('snippet', [
        'snippet_pk',
    ]),
    },
    methods: {
        ...mapActions('snippet', 
    { postSnippet: 'POST_SNIPPET',
    }),
    notePost() {
        this.postSnippet(this.body)
    },
    },
}
</script>