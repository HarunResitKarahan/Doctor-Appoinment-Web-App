<template>
  <div class="booking">
    <Navbar />
    <SubNavbar :title="title"/>
    <BookingTab :doctor="$route.params.doctor"/>
    <Footer />
    <Login />
     <!-- <template v-for="(item, index) in responseData" >
        <p class="change" :key="item.message">{{ index }} {{ item }}</p>
      </template> -->
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'
import SubNavbar from '@/components/Booking/SubNavbar.vue'
import BookingTab from '@/components/Booking/BookingTab.vue'
import Footer from '@/components/Homepage/Footer.vue'
import Login from '@/components/Login/Login.vue'

export default {
  name: 'Booking',
  components: {
    Navbar,
    SubNavbar,
    BookingTab,
    Footer,
    Login
  },
  data () {
    return {
      title: '',
      responseData: []
    }
  },
  mounted () {
    document.title = 'Randevu Al'
    this.title = document.title
  },
  // Serverdan Anasayfa için veriler çekildi
  created () {
    fetch('http://localhost:8000/patient', {
      method: 'get'
    })
      .then((response) => response.json())
      .then(data => {
        this.responseData = data
      })
  }
}
</script>
