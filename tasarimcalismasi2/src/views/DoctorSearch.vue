<template>
  <div class="doctor-search">
      <Navbar />
      <SubNavbar :title = "title"/>
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import SubNavbar from '@/components/Booking/SubNavbar.vue'

export default {
  name: 'DoctorSearch',
  data () {
    return {
      title: ''
    }
  },
  components: {
    Navbar,
    SubNavbar
  },
  mounted () {
    document.title = 'Doktor Ara'
    this.title = document.title
  }
}
</script>
