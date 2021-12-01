<template>
  <div class='home'>
    <Navbar />
    <SlideArea />
    <Clinic />
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import SlideArea from '@/components/Homepage/SlideArea.vue'
import Clinic from '@/components/Homepage/Clinics.vue'
import Footer from '@/components/Homepage/Footer.vue'

export default {
  name: 'Home',
  components: {
    Navbar,
    SlideArea,
    Clinic,
    Footer
  },
  mounted () {
    document.title = 'Ana Sayfa'
  }
}
</script>
