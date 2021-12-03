<template>
  <div class="login">
      <div class="login-card">
          <span @click="loginPageClose" class="material-icons" style="position: absolute;right: 40px; top: 30px;font-size: 22px;color: rgba(0, 0, 0, 0.6);cursor: pointer;">
            highlight_off
          </span>
          <p class="h2">GİRİŞ YAPIN</p>
          <div class="username">
              <span>Kullanıcı Adı: </span>
              <input type="text">
          </div>
          <div class="password">
              <span>Şifre: </span>
              <input type="password">
          </div>
          <div class="remind-me">
              <label class="checkbox">
                  <input type="checkbox"><p style="width: 300px;text-align: left;">Beni Hatırla</p>
              </label>
              <div class="forgot-password">
                  <p>Şifremi Unuttum?</p>
              </div>
          </div>
          <div class="log-in">
              <p>Giriş Yap</p>
          </div>
          <p @click="registerPageOpen" class="register">Kayıtlı Değil misiniz ?</p>
      </div>
      <div class="register-card">
          <span @click="loginPageClose" class="material-icons" style="position: absolute;right: 40px; top: 30px;font-size: 22px;color: white;cursor: pointer;">
            highlight_off
          </span>
          <p class="h2">KAYIT OLUN</p>
          <div class="username">
              <span>Kullanıcı Adı: </span>
              <input type="text">
          </div>
          <div class="username">
              <span>Ad: </span>
              <input type="text">
          </div>
          <div class="username">
              <span>Soyad: </span>
              <input type="text">
          </div>
          <div class="username">
              <span>E-posta: </span>
              <input type="text">
          </div>
          <div class="password">
              <span>Şifre: </span>
              <input type="password">
          </div>
          <div class="log-in">
              <p>Kayıt Ol</p>
          </div>
          <p @click="loginPageOpen" class="register">Üye misiniz ?</p>
      </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Login',
  data () {
    return {
    }
  },
  methods: {
    loginPageClose () {
      $('.login').hide()
    },
    loginPageOpen () {
      $('.register-card').css('display', 'none')
      $('.login-card').css('display', 'block')
    },
    registerPageOpen () {
      $('.login-card').css('display', 'none')
      $('.register-card').css('display', 'block')
    }
  }
}
</script>
