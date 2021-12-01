<template>
  <div class="about">
     <template v-for="(item, index) in responseData" >
        <p class="change" :key="item.message">{{ index }} {{ item }}</p>
      </template>
  </div>
</template>

<script>
export default {
  name: 'About',
  // Home.vue 'un kapsadığı componentlar belirtildi.
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
