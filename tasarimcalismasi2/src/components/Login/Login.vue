<template>
  <div class="login">
      <div class="login-card">
          <span @click="loginPageClose" class="material-icons" style="position: absolute;right: 40px; top: 30px;font-size: 22px;color: rgba(0, 0, 0, 0.6);cursor: pointer;">
            highlight_off
          </span>
          <p class="h2">GİRİŞ YAPIN</p>
          <div class="username">
              <span>Kullanıcı Adı: </span>
              <input v-model="username" type="text">
          </div>
          <div class="password">
              <span>Şifre: </span>
              <input v-model="password" type="password">
          </div>
          <div class="remind-me">
              <label class="checkbox">
                  <input type="checkbox"><p style="width: 300px;text-align: left;">Beni Hatırla</p>
              </label>
              <div class="forgot-password">
                  <p>Şifremi Unuttum?</p>
              </div>
          </div>
          <div @click="signin(username, password)" class="log-in">
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
              <span>TC NO: </span>
              <input v-model="id" type="number">
          </div>
          <div class="username">
              <span>Ad: </span>
              <input v-model="name" type="text">
          </div>
          <div class="username">
              <span>Soyad: </span>
              <input v-model="surname" type="text">
          </div>
          <div class="username">
              <span>E-posta: </span>
              <input v-model="email" type="text">
          </div>
          <div class="password">
              <span>Şifre: </span>
              <input v-model="registerpassword" type="password">
          </div>
          <template v-if="isregistered == 'Added Successfully'">
            <p style="color: lime;margin: 5px 0;">Başarıyla Kayıt Olundu.</p>
          </template>
          <template v-if="isregistered == 'Failed to Add'">
            <p style="color: red;margin: 5px 0;">Kayıt Olunamadı Kimlik Numarası Zaten Kayıtlı</p>
          </template>
          <div @click="registerbutton(id, name, surname, email, registerpassword)" class="log-in">
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
      localpassword: '',
      localusername: '',
      issignin: '',
      isregistered: ''
    }
  },
  created () {
    this.localusername = localStorage.username
    this.issignin = localStorage.issignin
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
    },
    signinbutton (username, password) {
      fetch('http://localhost:8000/patient/signin', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          patientID: username,
          patientPassword: password
        })
      })
        .then(response => response.json())
        .then(data => { console.log(data) })
        // this.issignin = data
        //   if (this.issignin === 'Giriş Başarılı') {
        //     localStorage.username = nick
        //     localStorage.issignin = this.issignin
        //     this.localusername = localStorage.username
        //     setInterval(function () { location.reload() }, 500)
    },
    registerbutton (id, name, surname, email, registerpassword) {
      fetch('http://localhost:8000/patient', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          patientID: id,
          patientName: name,
          patientSurname: surname,
          patientEmail: email,
          patientPassword: registerpassword
        })
      })
        .then(response => response.json())
        .then(data => {
          this.isregistered = data
          if (data === 'Added Successfully') {
            setInterval(function () { location.reload() }, 1500)
          }
        })
    }
  }
}
</script>
