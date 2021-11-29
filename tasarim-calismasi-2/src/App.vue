<template>
  <div style="display: none;">
    <router-link style="display: none;" to="/">Home</router-link>
  </div>
  <router-view />
</template>

<style lang="scss">
* {
  font-family: 'Epilogue', sans-serif;
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
body {
  margin: 0;
}
</style>
