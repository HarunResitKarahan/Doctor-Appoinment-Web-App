<template>
  <div class="booking">
    <Navbar />
     <!-- <template v-for="(item, index) in responseData" >
        <p class="change" :key="item.message">{{ index }} {{ item }}</p>
      </template> -->
  </div>
</template>

<script>
import Navbar from '@/components/Homepage/Navbar.vue'

export default {
  name: 'Booking',
  components: {
    Navbar
  },
  data () {
    return {
      responseData: []
    }
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
