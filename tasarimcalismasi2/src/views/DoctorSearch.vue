<template>
  <div class="doctor-search">
      <Login />
      <Navbar />
      <SubNavbar :title = "title"/>
      <div class="search-content">
        <Search :department="$route.params.department" :sex="$route.params.sex" :location="$route.params.location" />
        <ShowDoctors />
      </div>
      <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import Footer from '@/components/Homepage/Footer.vue'
import SubNavbar from '@/components/Booking/SubNavbar.vue'
import Login from '@/components/Login/Login.vue'
import Search from '@/components/DoctorSearch/Search.vue'
import ShowDoctors from '@/components/DoctorSearch/ShowDoctors.vue'

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
    ShowDoctors,
    Footer
  },
  mounted () {
    document.title = 'Doktor Ara'
    this.title = document.title
  }
}
</script>
