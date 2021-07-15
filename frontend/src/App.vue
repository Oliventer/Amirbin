<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/note">Note</router-link> |
      <router-link to="/paste">Paste</router-link> |
      <router-link to="/subscribe">Subscribe</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="less">
body {
        background-color: #F5FFFA !important;
    }
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 10px;
  max-width: 170px;
  margin: auto;
  
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #0069FF;
    }
  }
}

</style>
