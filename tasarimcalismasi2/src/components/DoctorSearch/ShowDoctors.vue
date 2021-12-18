<template>
  <div class="show-doctors">
    <template v-for="item in doctor">
      <div class="doctor-card" :key="item">
        <div class="doctor-image">
          <template v-if="item.doctorSex == 'Erkek'">
            <img src="@/assets/maledoctor.png" width="150" height="150">
          </template>
          <template v-else>
            <img src="@/assets/femaledoctor.png" width="150" height="150">
          </template>
        </div>
        <div class="doctor-info">
          <p style="color: #2E3842;font-size: 20px;font-weight: 500;">{{item.doctorName}} {{item.doctorSurname}}</p>
          <p style="font-size: 14px;color: #757575;margin-bottom: 5px;">{{department}}</p>
          <div class="doctor-rank" style="margin: 0 0 7px 0">
                <div class="star" :id="item.doctorID">
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}a)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient :id="`${item.doctorID}a`">
                        <stop offset="0%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                        <stop offset="60%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}1)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient :id="`${item.doctorID}1`">
                        <stop offset="0%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                        <stop offset="60%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}2)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient :id="`${item.doctorID}2`">
                        <stop offset="0%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                        <stop offset="60%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}3)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient :id="`${item.doctorID}3`">
                        <stop offset="0%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                        <stop offset="60%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}4)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient :id="`${item.doctorID}4`">
                        <stop offset="0%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                        <stop offset="60%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><p class="after">{{item.doctorScore}}</p><p style="height: 22px;">154 Değerlendirme</p>
                </div>
          </div>
          <div class="doctor-departmant">
              <span class="material-icons" style="color: rgb(2550, 0, 0, 0.300); font-size: 24px;padding: 1px; margin-right: 2px;">emergency</span><p style="padding-top: 3.5px;">{{hospitalName}}</p>
          </div>
          <div class="make-appointment">
            <router-link class="appointment" :to="{ name: 'Booking', params: { doctorID: item.doctorID, hospitalName: hospitalName, department: department } }"><p>Randevu Al</p></router-link>
          </div>
        </div>
    </div>
    </template>
    <template v-if="doctor.length == 0">
      <div class="no-found-doctor">
        <p style="font-size: 36px;color: #c3c3c3;">Aradığınız Kriterlere Uygun Doktor Bulunamadı</p>
      </div>
    </template>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'ShowDoctors',
  props: {
    doctor: Array,
    department: String,
    hospitalName: String
  },
  data () {
    return {
    }
  },
  watch: {
    doctor: function () {
      this.star()
    }
  },
  methods: {
    star () {
      var doctor = this.doctor
      var getstar
      var star
      $('linearGradient').ready(function () {
        doctor.forEach(item => {
          getstar = document.getElementById(String(item.doctorID))
          console.log(getstar)
          star = getstar.querySelectorAll('linearGradient stop')
          console.log(star)
          console.log(Number(item.doctorScore))
          if (Number(item.doctorScore) > 1 && Number(item.doctorScore) < 2) {
            console.log('girdi 1 - 2 arası')
            star[0].attributes[1].value = 'rgb(255, 185, 88)'
            star[1].attributes[1].value = 'rgb(255, 185, 88)'
            star[2].attributes[1].value = 'white'
            star[3].attributes[1].value = 'white'
            star[4].attributes[1].value = 'white'
            star[5].attributes[1].value = 'white'
            star[6].attributes[1].value = 'white'
            star[7].attributes[1].value = 'white'
            star[8].attributes[1].value = 'white'
            star[9].attributes[1].value = 'white'
            star[10].attributes[1].value = 'rgb(255, 185, 88)'
            star[11].attributes[1].value = 'rgb(255, 185, 88)'
            star[12].attributes[1].value = 'white'
            star[13].attributes[1].value = 'white'
            star[14].attributes[1].value = 'white'
            star[15].attributes[1].value = 'white'
            star[16].attributes[1].value = 'white'
            star[17].attributes[1].value = 'white'
            star[18].attributes[1].value = 'white'
            star[19].attributes[1].value = 'white'
          } else if (Number(item.doctorScore) > 2 && Number(item.doctorScore) < 3) {
            console.log('girdi 2 - 3 arası')
            console.log(Math.trunc((Number(item.doctorScore) % 1) * 100))
            var text1 = String(Math.trunc((Number(item.doctorScore) % 1) * 100))
            var text2 = '%'
            var concat = text1.concat(text2)
            star[0].attributes[1].value = 'rgb(255, 185, 88)'
            star[1].attributes[1].value = 'rgb(255, 185, 88)'
            star[2].attributes[1].value = 'rgb(255, 185, 88)'
            star[3].attributes[1].value = 'rgb(255, 185, 88)'
            star[4].attributes[1].value = 'rgb(255, 185, 88)'
            star[5].attributes[0].value = concat
            star[5].attributes[1].value = 'rgb(255, 185, 88)'
            star[6].attributes[1].value = 'white'
            star[7].attributes[1].value = 'white'
            star[8].attributes[1].value = 'white'
            star[9].attributes[1].value = 'white'
            star[10].attributes[1].value = 'white'
            star[11].attributes[1].value = 'white'
            star[12].attributes[1].value = 'white'
            star[13].attributes[1].value = 'white'
            star[14].attributes[1].value = 'white'
            star[15].attributes[1].value = 'white'
            star[16].attributes[1].value = 'white'
            star[17].attributes[1].value = 'white'
            star[18].attributes[1].value = 'white'
            star[19].attributes[1].value = 'white'
          } else if (Number(item.doctorScore) > 3 && Number(item.doctorScore) < 4) {
            console.log('girdi 3 - 4 arası')
            star[0].attributes[1].value = 'rgb(255, 185, 88)'
            star[1].attributes[1].value = 'rgb(255, 185, 88)'
            star[2].attributes[1].value = 'rgb(255, 185, 88)'
            star[3].attributes[1].value = 'rgb(255, 185, 88)'
            star[4].attributes[1].value = 'rgb(255, 185, 88)'
            star[5].attributes[1].value = 'rgb(255, 185, 88)'
            star[6].attributes[1].value = 'white'
            star[7].attributes[1].value = 'white'
            star[8].attributes[1].value = 'white'
            star[9].attributes[1].value = 'white'
            star[10].attributes[1].value = 'white'
            star[11].attributes[1].value = 'white'
            star[12].attributes[1].value = 'white'
            star[13].attributes[1].value = 'white'
            star[14].attributes[1].value = 'white'
            star[15].attributes[1].value = 'white'
            star[16].attributes[1].value = 'white'
            star[17].attributes[1].value = 'white'
            star[18].attributes[1].value = 'white'
            star[19].attributes[1].value = 'white'
          } else if (Number(item.doctorScore) > 4 && Number(item.doctorScore) < 5) {
            console.log('girdi 4 - 5 arası')
            star[0].attributes[1].value = 'rgb(255, 185, 88)'
            star[1].attributes[1].value = 'rgb(255, 185, 88)'
            star[2].attributes[1].value = 'rgb(255, 185, 88)'
            star[3].attributes[1].value = 'rgb(255, 185, 88)'
            star[4].attributes[1].value = 'rgb(255, 185, 88)'
            star[5].attributes[1].value = 'rgb(255, 185, 88)'
            star[6].attributes[1].value = 'rgb(255, 185, 88)'
            star[7].attributes[1].value = 'rgb(255, 185, 88)'
            star[8].attributes[1].value = 'white'
            star[9].attributes[1].value = 'white'
            star[10].attributes[1].value = 'white'
            star[11].attributes[1].value = 'white'
            star[12].attributes[1].value = 'white'
            star[13].attributes[1].value = 'white'
            star[14].attributes[1].value = 'white'
            star[15].attributes[1].value = 'white'
            star[16].attributes[1].value = 'white'
            star[17].attributes[1].value = 'white'
            star[18].attributes[1].value = 'white'
            star[19].attributes[1].value = 'white'
          }
        })
      })
    }
  }
}
</script>
