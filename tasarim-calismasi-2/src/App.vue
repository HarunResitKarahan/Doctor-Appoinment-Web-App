<template>
  <div style="display: none;">
    <router-link style="display: none;" to="/">Home</router-link>
  </div>
  <router-view />
</template>

<style lang="scss">
* {
  font-family: 'Epilogue', sans-serif;
  transition: all 0.5s ease;
}
* a {
  text-decoration: none;
  color: black;
  font-weight: 500;
  cursor: pointer;
}
* p {
  margin: 0;
  padding: 0;
}
* .h4 {
  color: rgba(0, 0, 0, 0.726);
  font-size: 32px;
  font-weight: 500;
}
* .h5 {
  color: rgba(0, 0, 0, 0.555);
  font-size: 16px;
  margin-bottom: 5px;
  font-weight: 500;
}
* input:focus {
  outline: none;
}
body {
  margin: 0;
}
#app {
  overflow: hidden;
}
</style>
