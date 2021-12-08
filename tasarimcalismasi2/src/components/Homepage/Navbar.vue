<template>
  <div class="navbar">
    <div class="logo">
      <router-link to="/">HARUN KARAHAN</router-link>
    </div>
    <!-- <div class="menu">
      <a href="#">Ana Sayfa</a>
      <a href="#">Randevu al</a>
    </div> -->
    <template v-if="issignin != 'Giriş Başarılı'">
      <div @click="loginPage" class="log-in">
        <a href="#">KAYIT OL / GİRİŞ YAP</a>
      </div>
    </template>
    <template v-if="issignin == 'Giriş Başarılı'">
      <div style="margin-right: 30px;display:flex;justify-content: center;width: 5%;">
       <a href="#" class="dropdown">
              <!-- Profile ulaşmak için profile butonu oluşturuldu -->
              <b-icon-person id="btn" style="border: 1px solid rgb(71, 70, 71);color: rgb(71, 70, 71);border-radius: 100%;height: 40px;width:40px;padding: 3px;" class="person"/>
              <b-icon-caret-down-fill style="color: rgb(71, 70, 71);height: 10px;width:10px;vertical-align: middle !important;" class="chevron-down"/>
              <div class="dropdown-content" align="left">
                <router-link to="/profile" style="display: none;" :style="issignin === 'Giriş Başarılı' ? 'display: block' : ''">Profile</router-link>
                <a @click="signout" href="#" :style="issignin === 'Giriş Başarılı' ? '' : 'display: none'">Çıkış</a>
              </div>
            </a>
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
      setInterval(function () { location.reload() }, 500)
    }
  },
  created () {
    this.issignin = localStorage.issignin
    this.localusername = localStorage.username
  }
}
</script>
