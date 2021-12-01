<template>
  <div class='home'>
    <Navbar />
    <SlideArea />
    <Clinic />
    <Doctors />
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import SlideArea from '@/components/Homepage/SlideArea.vue'
import Clinic from '@/components/Homepage/Clinics.vue'
import Footer from '@/components/Homepage/Footer.vue'
import Doctors from '@/components/Homepage/Doctors.vue'

export default {
  name: 'Home',
  components: {
    Navbar,
    SlideArea,
    Clinic,
    Footer,
    Doctors
  },
  mounted () {
    document.title = 'Ana Sayfa'
  }
}
</script>
