<template>
    <div class="content">
        <br>
        <span class="span">Code:</span>
        <textarea v-model="body.code" placeholder="paste code here" class="textarea"></textarea>
        <br>
        <span class="span">Delete after viewing:  </span>
        <br>
        <label class="container">
            <input type="checkbox" id="checkbox" v-model="body.delete_after_viewing">
            <span class="checkmark"></span>
        </label>
        <br><br>
        <span class="span">Language:</span>
        <select v-model="body.language" class="select">
            <option :value="python">Python</option>
            <option :value="js">JavaScript</option>
        </select>
        <br><br>
        <span class="span">Style:</span>
        <select v-model="body.style" class="select">
            <option>friendly</option>
            <option>native</option>
        </select>
        <br><br><br>
        <button v-on:click="notePost()" class="button">Post</button>
    </div>
</template>

<script>

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
    methods: {
    async notePost() {
        let path = await this.$store.dispatch('snippet/POST_SNIPPET', this.body)
          this.$router.push({ name: 'Snippet', params:{ pk: path } })   
    },
    },
}
</script>

<style lang="less">
    .content {
        max-width: 1200px;
        margin: auto;
        border: 4px double gray;
        border-bottom-left-radius: 200px;
        border-bottom-right-radius: 200px;
        border-top-right-radius: 200px;
        background: #D9D6CF;
        height: 730px;
    }
    .textarea {
        resize: none;
        width: 660px !important;
        height: 430px !important;
        display: block;
        font-size:20px;
        margin-left: 263px;
        margin-right: auto;
    }
    .select {
        display: block;
        margin-left: 266px;
        width: 660px;
        height: 22px;
        
    }
    .span {
        display: block;
        padding-left: 166px;
        width: 85px;
        height: 25px; 
        text-align: right;
        position: absolute;
    }
    .button{
        display:inline-block;
        padding:1.2em 5.0em;
        margin-left: 514px;
        border-radius:2em;
        box-sizing: border-box;
        text-decoration:none;
        font-family:'Roboto',sans-serif;
        font-weight:300;
        color:#FFFFFF;
        background-color:#4eb5f1;
        text-align:center;
        transition: all 0.2s;
    }
    .button:hover {
        background-color:#4095c6;
    }
    @media all and (max-width: 30em){
        .button {
            display: block;
            margin: 0.2em auto;
        }
    }

    .container {
        display: block;
        position: relative;
        margin-left: 266px;
        cursor: pointer;
        font-size: 22px;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }

    .container input {
        position: absolute;
        opacity: 0;
        cursor: pointer;
        height: 0;
        width: 0;
    }   

    .checkmark {
        position: absolute;
        top: -15px;
        left: 0;
        height: 25px;
        width: 25px;
        background-color: white;
    }

    .container:hover input ~ .checkmark {
        background-color: rgb(175, 174, 174);
    }

    .container input:checked ~ .checkmark {
        background-color: #2196F3;
    }

    .checkmark:after {
        content: "";
        position: absolute;
        display: none;
    }

    .container input:checked ~ .checkmark:after {
        display: block;
    }

    .container .checkmark:after {
        left: 9px;
        top: 5px;
        width: 5px;
        height: 10px;
        border: solid white;
        border-width: 0 3px 3px 0;
        -webkit-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
        transform: rotate(45deg);
    }   
  
</style>