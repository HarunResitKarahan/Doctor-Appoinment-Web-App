<template>
  <div class="profile">
      <Navbar />
      <SubNavbar :title="title"/>
      <ProfileComponent />
      <Footer />
      <Login />
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import SubNavbar from '@/components/Booking/SubNavbar.vue'
import ProfileComponent from '@/components/Profile/ProfileComponent.vue'
import Footer from '@/components/Homepage/Footer.vue'
import Login from '@/components/Login/Login.vue'

export default {
  name: 'Profile',
  components: {
    Navbar,
    SubNavbar,
    ProfileComponent,
    Footer,
    Login
  },
  data () {
    return {
      title: ''
    }
  },
  mounted () {
    document.title = 'Profile'
    this.title = document.title
  }
}
</script>
