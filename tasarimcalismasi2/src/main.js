import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import '@/css/body.css'
import '@/css/Home_css/navbar.css'
import '@/css/Home_css/slide-area.css'
import '@/css/Home_css/clinic.css'
import '@/css/Home_css/doctors.css'
import '@/css/Home_css/footer.css'

import '@/css/Home_css/Login_css/login.css'

import '@/css/Booking_css/booking.css'
import '@/css/Booking_css/sub-navbar.css'
import '@/css/Booking_css/booking-tab.css'

import '@/css/DoctorSearch_css/doctor-search.css'
import '@/css/DoctorSearch_css/search.css'
import '@/css/DoctorSearch_css/show-doctors.css'

import '@/css/Profile_css/profile.css'
import '@/css/Profile_css/profile-component.css'

import './scripts/Home_js/clinic.js'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
