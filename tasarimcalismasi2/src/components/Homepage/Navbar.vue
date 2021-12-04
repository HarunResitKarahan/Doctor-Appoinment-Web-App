<template>
  <div class="navbar">
    <div class="logo">
      <router-link to="/">HARUN KARAHAN</router-link>
    </div>
    <!-- <div class="menu">
      <a href="#">Ana Sayfa</a>
      <a href="#">Randevu al</a>
    </div> -->
    <div @click="loginPage" class="log-in">
      <a href="#">KAYIT OL / GİRİŞ YAP</a>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Navbar',
  methods: {
    loginPage () {
      $('.login').css('display', 'flex')
      $('.login .login-card').css('display', 'block')
      $('.login .register-card').css('display', 'none')
    }
  }
}
</script>
