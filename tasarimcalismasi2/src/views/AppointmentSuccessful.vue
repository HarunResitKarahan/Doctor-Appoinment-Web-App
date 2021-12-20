<template>
  <div class="appointment-successful">
    <Navbar />
    <Success />
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import Footer from '@/components/Homepage/Footer.vue'
import Success from '@/components/AppointmentSuccessful/Success.vue'

export default {
  name: 'AppointmentSuccessful',
  components: {
    Navbar,
    Footer,
    Success
  },
  mounted () {
    document.title = 'Randevu Alındı'
  }
}
</script>
