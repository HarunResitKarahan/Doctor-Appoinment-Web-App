<template>
  <div class="profile">
      asd
  </div>
</template>

<script>

export default {
  name: 'Profile',
  data () {
    return {
      title: ''
    }
  },
  mounted () {
    document.title = 'Profil'
    this.title = document.title
  }
}
</script>
