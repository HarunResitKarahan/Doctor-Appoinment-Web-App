<template>
  <div class="profile-component">
      aasd
  </div>
</template>

<script>
// import $ from 'jquery'
export default {
  name: 'ProfileComponent',
  data () {
    return {
      issignin: '',
      isregistered: ''
    }
  },
  created () {
    this.localusername = localStorage.username
    this.issignin = localStorage.issignin
  }
}
</script>
