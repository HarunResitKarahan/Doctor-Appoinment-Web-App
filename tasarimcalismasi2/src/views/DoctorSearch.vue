<template>
  <div class="doctor-search">
      <Login />
      <Navbar />
      <SubNavbar :title = "title"/>
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import SubNavbar from '@/components/Booking/SubNavbar.vue'
import Login from '@/components/Login/Login.vue'

export default {
  name: 'DoctorSearch',
  data () {
    return {
      title: ''
    }
  },
  components: {
    Navbar,
    SubNavbar,
    Login
  },
  mounted () {
    document.title = 'Doktor Ara'
    this.title = document.title
  }
}
</script>
