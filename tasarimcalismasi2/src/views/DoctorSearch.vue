<template>
  <div class="doctor-search">
      <Login />
      <Navbar />
      <SubNavbar :title = "title"/>
      <Search :department="$route.params.department" :gender="$route.params.gender" :location="$route.params.location" />
      <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import Footer from '@/components/Homepage/Footer.vue'
import SubNavbar from '@/components/Booking/SubNavbar.vue'
import Login from '@/components/Login/Login.vue'
import Search from '@/components/DoctorSearch/Search.vue'

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
    Login,
    Search,
    Footer
  },
  mounted () {
    document.title = 'Doktor Ara'
    this.title = document.title
  }
}
</script>
