<template>
  <div class="profile-component">
      <div class="profile-info col-4">
        asd
      </div>
      <div class="booking-history col-8">
        asd
      </div>
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
