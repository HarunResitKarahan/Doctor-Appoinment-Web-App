<template>
  <div class="appointmentsuccessful">
    <Navbar />
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import Footer from '@/components/Homepage/Footer.vue'

export default {
  name: 'AppointmentSuccessful',
  components: {
    Navbar,
    Footer
  },
  mounted () {
    document.title = 'Randevu Alındı'
  }
}
</script>
