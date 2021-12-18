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
                <div class="star">
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" fill="url(#grad)" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient id="grad">
                        <stop offset="0%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" fill="url(#grad1)" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient id="grad1">
                        <stop offset="0%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" fill="url(#grad2)" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient id="grad2">
                        <stop offset="0%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" fill="url(#grad3)" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient id="grad3">
                        <stop offset="0%" stop-color="white"/>
                        <stop offset="100%" stop-color="white"/>
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <svg xmlns="http://www.w3.org/2000/svg" style="margin: 0 -5px 0 0;padding: 1px;padding-bottom: 3px;font-size: 24px;" width="24" height="24" viewBox="0 0 24 24" fill="url(#grad4)" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                    <linearGradient id="grad4">
                        <stop offset="0%" stop-color="white"/>
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
// import $ from 'jquery'
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
    doctor () {
      this.star()
      // console.log(star[6].attributes[1].value)
    }
    // document.querySelector('linearGradient stop').attributes[0].value = '80%'
  },
  methods: {
    star () {
      var star = document.querySelectorAll('linearGradient stop')
      console.log(star.attributes[1])
      this.doctor.forEach(item => {
        console.log(Number(item.doctorScore))
        if (Number(item.doctorScore) > 1 && Number(item.doctorScore) < 2) {
          console.log('girdi 1 - 2 arası')
          star[0].attributes[1].value = 'rgb(255, 185, 88)'
          star[1].attributes[1].value = 'rgb(255, 185, 88)'
        } else if (Number(item.doctorScore) > 2 && Number(item.doctorScore) < 3) {
          console.log('girdi 2 - 3 arası')
          star[0].attributes[1].value = 'rgb(255, 185, 88)'
          star[1].attributes[1].value = 'rgb(255, 185, 88)'
          star[2].attributes[1].value = 'rgb(255, 185, 88)'
          star[3].attributes[1].value = 'rgb(255, 185, 88)'
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
        }
      })
    }
  }
}
</script>
