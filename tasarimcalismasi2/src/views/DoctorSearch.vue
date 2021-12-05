<template>
  <div class="doctor-search">
      <Login />
      <Navbar />
      <SubNavbar :title = "title"/>
      <div class="search-content">
        <Search />
        <ShowDoctors />
      </div>
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
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
    ShowDoctors
  },
  mounted () {
    document.title = 'Doktor Ara'
    this.title = document.title
  }
}
</script>
