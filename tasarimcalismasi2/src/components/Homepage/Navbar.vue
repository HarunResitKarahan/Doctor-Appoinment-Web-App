<template>
  <div class="navbar">
    <div class="logo">
      <router-link to="/"><img src="@/assets/logo4.png" width="165" height="44" style="float: left;margin-left: 15px"></router-link>
    </div>
    <!-- <div class="menu">
      <a href="#">Ana Sayfa</a>
      <a href="#">Randevu al</a>
    </div> -->
    <template v-if="issignin != 'Giriş Başarılı'">
      <div @click="loginPage" class="log-in" :style="issignin === undefined ? '' : 'display: none'">
          <a href="#">KAYIT OL / GİRİŞ YAP</a>
      </div>
    </template>
    <template v-if="issignin == 'Giriş Başarılı'">
      <div class="log-in">
          <div><router-link to="/profile">PROFİLE</router-link></div>
          <div @click="signout"><router-link to="/" style="border-left-width: 0;">ÇIKIŞ</router-link></div>
      </div>
    </template>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Navbar',
  data () {
    return {
      issignin: '',
      localusername: ''
    }
  },
  methods: {
    loginPage () {
      $('.login').css('display', 'flex')
      $('.login .login-card').css('display', 'block')
      $('.login .register-card').css('display', 'none')
    },
    signout () {
      localStorage.removeItem('username')
      localStorage.removeItem('issignin')
      setInterval(function () { location.reload() }, 100)
    }
  },
  created () {
    this.issignin = localStorage.issignin
    this.localusername = localStorage.username
  }
}
</script>
