<template>
    <div class="content">
        <br>
        <span class="span">Code:</span>
        <input class= "input-file" type="file" id="file" ref="file" v-on:change="readFile()"/>
        <textarea v-model="body.code" placeholder="paste code here" class="form-control"></textarea>
        <br>
        <span class="span">Delete after viewing:  </span>
        <br>
        <label class="container">
            <input type="checkbox" id="checkbox" v-model="body.delete_after_viewing">
            <span class="checkmark"></span>
        </label>
        <br><br>
        <span class="span">Language:</span>
        <select v-model="body.language" class="form-control">
            <option :value="python">Python</option>
            <option :value="js">JavaScript</option>
        </select>
        <br><br>
        <span class="span">Style:</span>
        <select v-model="body.style" class="form-control">
            <option>friendly</option>
            <option>native</option>
        </select>
        <br><br><br>
        <button v-on:click="notePost()" class="btn btn-primary btn-lg btn-block">Post</button>
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
                style: '',
            },
        }
    },
    methods: {
    async notePost() {
        let path = await this.$store.dispatch('snippet/POST_SNIPPET', this.body)
          this.$router.push({ name: 'Snippet', params:{ pk: path, isCodeExist: true } })   
    },
     readFile(){
        let file = this.$refs.file.files[0];
        let reader = new FileReader();
        var vm = this

        reader.onload = function(e){
            vm.body.code = e.target.result
        } 

        reader.readAsText(file);
    }
    },
}
</script>

<style lang="less">
    .input-file {
        opacity: 0;
        display: block;
        width: 660px;
        height: 410px;
        margin-left: 266px;
        position: absolute;
        cursor: pointer;
    }
    .content {
        max-width: 1200px;
        margin: auto;
        background: #F0F8FF;
        height: 775px;
        border: 1px ridge silver;
    }

    .form-control {
        display: block;
        margin-left: 266px;
        width: 660px;
        height: 35px;
        resize: none;    
    }

    textarea.form-control {
        height:410px;
    }
    
    .span {
        display: block;
        padding-left: 10px;
        margin-left: 130px;
        width: 120px;
        height: 25px; 
        text-align: right;
        position: absolute;
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
        background-color: #F5F5F5;
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