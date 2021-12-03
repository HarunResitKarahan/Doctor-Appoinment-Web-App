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
              <input type="text">
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
    }
  }
}
</script>
