<template>
  <div class='home'>
    <LoaderScene />
    <Login />
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
import Login from '@/components/Login/Login.vue'
import LoaderScene from '@/components/LoaderScene/Loader.vue'

export default {
  name: 'Home',
  components: {
    LoaderScene,
    Navbar,
    SlideArea,
    Clinic,
    Footer,
    Doctors,
    Login
  },
  mounted () {
    document.title = 'Ana Sayfa'
  }
}
</script>
