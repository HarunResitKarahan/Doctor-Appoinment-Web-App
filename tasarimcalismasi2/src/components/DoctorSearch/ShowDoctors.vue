<template>
  <div class="show-doctors">
    <template v-if="slicedDoctor.length > 0">
      <div class="sort">
        <select v-model="sort" @change="sortby($event)" name="sort" id="sort">
          <option value="" hidden>{{defaultsort}}</option>
          <option value="empty" selected>{{defaultsort}}</option>
          <!-- <option value="" disabled>Sıralama</option> -->
          <option value="countOfRating">Doktor Puanı</option>
          <option value="rating">Değerlendirme Sayısı</option>
        </select>
      </div>
    </template>
    <template v-for="(item,index) in slicedDoctor">
      <div class="doctor-card" :key="index">
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
                    </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><p class="after">{{item.doctorScore}}</p><p style="height: 22px;">{{item.countOfRating}} Değerlendirme</p>
                </div>
          </div>
          <div class="doctor-departmant">
              <span class="material-icons" style="color: rgb(2550, 0, 0, 0.300); font-size: 24px;padding: 1px; margin-right: 2px;">emergency</span><p style="padding-top: 3.5px;">{{hospitalName}}</p>
          </div>
          <div class="make-appointment">
            <template v-if="issignin != 'Giriş Başarılı'">
                <p @click="loginPage">Randevu Al</p>
            </template>
            <template v-if="issignin == 'Giriş Başarılı'">
                <router-link class="appointment" :to="{ name: 'Booking', params: { doctorID: item.doctorID, hospitalName: hospitalName, department: department, date: date } }"><p>Randevu Al</p></router-link>
            </template>
          </div>
        </div>
    </div>
    </template>
    <template v-if="doctor.length > 3">
      <div class="see-more">
        <p @click="slicedDoctorMore(3)">Daha Fazla Görüntüle</p>
      </div>
    </template>
    <hr />
    <template v-if="doctor.length > 0">
      <div v-if="suggestion.length > 0" style="font-weight: 300;font-size: 1.2rem;margin-top: 30px;margin-bottom: 5px;">Size Önerilenler:</div>
    </template>
    <VueSlickCarousel style="width: 95%;margin: auto;" v-if="suggestion.length > 0 && doctor.length > 0" :arrows="false" :dots="true" :speed="500" :variableWidth="true" :infinite="false" :slidesToScroll="3" :swipeToSlide="true">
      <template v-for="(item,index) in suggestion">
        <div class="suggestion-doctor-card" :key="index">
          <div class="doctor-image">
            <template v-if="item.doctorSex == 'Erkek'">
              <img src="@/assets/maledoctor.png" width="85" height="85">
            </template>
            <template v-else>
              <img src="@/assets/femaledoctor.png" width="85" height="85">
            </template>
            <div class="info">
              <p>{{item.doctorName}} {{item.doctorSurname}}</p>
              <p class="departman">({{item.departmanID_id}})</p>
              <div class="suggestion-doctor-rank" style="margin: 0 0 7px 0">
                  <div class="star" :id="item.doctorID">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}a)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${item.doctorID}a`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}1)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${item.doctorID}1`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}2)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${item.doctorID}2`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}3)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${item.doctorID}3`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${item.doctorID}4)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${item.doctorID}4`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <p class="after">{{item.doctorScore}}</p><p>{{item.countOfRating}} Değerlendirme</p>
                  </div>
              </div>
              <div class="doctor-departmant">
                <span class="material-icons">emergency</span><p>{{item.hospitalID_id}}</p>
              </div>
            </div>
          </div>
          <div class="doctor-info">
            <div class="make-appointment">
              <template v-if="issignin != 'Giriş Başarılı'">
                  <p @click="loginPage">Randevu Al</p>
              </template>
              <template v-if="issignin == 'Giriş Başarılı'">
                  <router-link class="appointment" :to="{ name: 'Booking', params: { doctorID: item.doctorID, hospitalName: item.hospitalID_id, department: item.departmanID_id, date: date } }"><p>Randevu Al</p></router-link>
              </template>
            </div>
          </div>
      </div>
      </template>
    </VueSlickCarousel>
    <template v-if="doctor.length == 0">
      <div class="no-found-doctor">
        <p style="font-size: 36px;color: #c3c3c3;">Aradığınız Kriterlere Uygun Doktor Bulunamadı</p>
      </div>
    </template>
  </div>
</template>

<script>
import $ from 'jquery'
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
export default {
  name: 'ShowDoctors',
  props: {
    doctor: Array,
    department: String,
    hospitalName: String,
    date: String,
    location: String
  },
  components: {
    VueSlickCarousel
  },
  data () {
    return {
      issignin: '',
      suggestion: undefined,
      backupdoctor: undefined,
      sayac: 3,
      sort: '',
      defaultsort: 'Sıralama'
    }
  },
  watch: {
    doctor: function () {
      this.star()
    },
    sort: function () {
      this.starchange()
    }
  },
  computed: {
    slicedDoctor: {
      get () {
        return this.doctor.slice(0, this.sayac)
      }
    }
  },
  methods: {
    slicedDoctorMore (more) {
      this.sayac += 3
    },
    sortby (event) {
      if (this.backupdoctor === undefined) {
        this.backupdoctor = this.doctor
      }
      if (event.target.value === 'countOfRating') {
        var sortable = []
        this.doctor.forEach((doctor) => {
          sortable.push([doctor, doctor.doctorScore])
        })
        sortable.sort(function (a, b) {
          return b[1] - a[1]
        })
        sortable.forEach((item, index) => {
          item.pop(1)
          sortable[index] = item[0]
        })
        this.doctor = sortable
      } else if (event.target.value === 'rating') {
        sortable = []
        this.doctor.forEach((doctor) => {
          sortable.push([doctor, doctor.countOfRating])
        })
        sortable.sort(function (a, b) {
          return b[1] - a[1]
        })
        sortable.forEach((item, index) => {
          item.pop(1)
          sortable[index] = item[0]
        })
        this.doctor = sortable
      } else if (event.target.value === 'empty') {
        this.doctor = this.backupdoctor
      }
    },
    loginPage () {
      $('.login').css('display', 'flex')
      $('.login .login-card').css('display', 'block')
      $('.login .register-card').css('display', 'none')
    },
    star () {
      if (!this.doctor.length > 0) {
        this.sayac = 3
      }
      if (this.doctor.length > 0) {
        fetch('http://127.0.0.1:8000/apriori', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            patientID: localStorage.username,
            departman: this.department,
            city: this.location
          })
        })
          .then(response => response.json())
          .then(data => {
            this.suggestion = data
            this.suggestion.forEach((item, index) => {
              this.suggestion[index] = item[0]
            })
          })
      }
    }
  },
  created () {
    this.issignin = localStorage.issignin
  },
  updated () {
    this.suggestion.forEach((item) => {
      var id = String(item.doctorID)
      var hash = '#'
      hash = hash.concat(id)
      var getstar = $('.suggestion-doctor-rank').find(hash)
      var star = $(getstar).find('linearGradient stop')
      if (Math.trunc((Number(item.doctorScore) % 1) * 100) <= 35) {
        var text1 = String(Math.trunc((Number(item.doctorScore) % 1) * 100) + 10)
      } else if (Math.trunc((Number(item.doctorScore) % 1) * 100) >= 75) {
        text1 = String(Math.trunc((Number(item.doctorScore) % 1) * 100) - 10)
      } else {
        text1 = String(Math.trunc((Number(item.doctorScore) % 1) * 100))
      }
      var text2 = '%'
      var concat = text1.concat(text2)
      if (Number(item.doctorScore) >= 1 && Number(item.doctorScore) < 2) {
        star[0].attributes[2].value = 'rgb(255, 185, 88)'
        star[1].attributes[2].value = 'rgb(255, 185, 88)'
        star[3].attributes[1].value = '0%'
        star[2].attributes[2].value = 'white'
        star[3].attributes[1].value = '0%'
        star[3].attributes[2].value = 'white'
        star[4].attributes[1].value = '0%'
        star[4].attributes[2].value = 'rgb(255, 185, 88)'
        star[5].attributes[1].value = concat
        star[5].attributes[2].value = 'rgb(255, 185, 88)'
        star[6].attributes[1].value = concat
      } else if (Number(item.doctorScore) >= 2 && Number(item.doctorScore) < 3) {
        star[0].attributes[2].value = 'rgb(255, 185, 88)'
        star[1].attributes[2].value = 'rgb(255, 185, 88)'
        star[2].attributes[2].value = 'rgb(255, 185, 88)'
        star[3].attributes[2].value = 'rgb(255, 185, 88)'
        star[4].attributes[2].value = 'rgb(255, 185, 88)'
        star[5].attributes[2].value = 'rgb(255, 185, 88)'
        star[6].attributes[2].value = 'rgb(255, 185, 88)'
        star[7].attributes[2].value = 'rgb(255, 185, 88)'
        star[8].attributes[1].value = concat
        star[8].attributes[2].value = 'rgb(255, 185, 88)'
        star[9].attributes[1].value = concat
      } else if (Number(item.doctorScore) >= 3 && Number(item.doctorScore) < 4) {
        star[0].attributes[2].value = 'rgb(255, 185, 88)'
        star[1].attributes[2].value = 'rgb(255, 185, 88)'
        star[2].attributes[2].value = 'rgb(255, 185, 88)'
        star[3].attributes[2].value = 'rgb(255, 185, 88)'
        star[4].attributes[2].value = 'rgb(255, 185, 88)'
        star[5].attributes[2].value = 'rgb(255, 185, 88)'
        star[6].attributes[2].value = 'rgb(255, 185, 88)'
        star[7].attributes[2].value = 'rgb(255, 185, 88)'
        star[8].attributes[2].value = 'rgb(255, 185, 88)'
        star[9].attributes[2].value = 'rgb(255, 185, 88)'
        star[10].attributes[2].value = 'rgb(255, 185, 88)'
        star[11].attributes[2].value = 'rgb(255, 185, 88)'
        star[12].attributes[1].value = concat
        star[12].attributes[2].value = 'rgb(255, 185, 88)'
        star[13].attributes[1].value = concat
      } else if (Number(item.doctorScore) >= 4 && Number(item.doctorScore) < 5) {
        star[0].attributes[2].value = 'rgb(255, 185, 88)'
        star[1].attributes[2].value = 'rgb(255, 185, 88)'
        star[2].attributes[2].value = 'rgb(255, 185, 88)'
        star[3].attributes[2].value = 'rgb(255, 185, 88)'
        star[4].attributes[2].value = 'rgb(255, 185, 88)'
        star[5].attributes[2].value = 'rgb(255, 185, 88)'
        star[6].attributes[2].value = 'rgb(255, 185, 88)'
        star[7].attributes[2].value = 'rgb(255, 185, 88)'
        star[8].attributes[2].value = 'rgb(255, 185, 88)'
        star[9].attributes[2].value = 'rgb(255, 185, 88)'
        star[10].attributes[2].value = 'rgb(255, 185, 88)'
        star[11].attributes[2].value = 'rgb(255, 185, 88)'
        star[12].attributes[2].value = 'rgb(255, 185, 88)'
        star[13].attributes[2].value = 'rgb(255, 185, 88)'
        star[14].attributes[2].value = 'rgb(255, 185, 88)'
        star[15].attributes[2].value = 'rgb(255, 185, 88)'
        star[16].attributes[2].value = 'rgb(255, 185, 88)'
        star[17].attributes[1].value = concat
        star[17].attributes[2].value = 'rgb(255, 185, 88)'
        star[18].attributes[1].value = concat
      }
    })
    var doctor = this.doctor
    var getstar
    var star
    doctor.forEach(item => {
      console.log(star)
      var id = String(item.doctorID)
      var hash = '#'
      hash = hash.concat(id)
      getstar = $('.doctor-rank').find(hash)
      star = $(getstar).find('linearGradient stop')
      if (Math.trunc((Number(item.doctorScore) % 1) * 100) <= 35) {
        var text1 = String(Math.trunc((Number(item.doctorScore) % 1) * 100) + 10)
      } else if (Math.trunc((Number(item.doctorScore) % 1) * 100) >= 75) {
        text1 = String(Math.trunc((Number(item.doctorScore) % 1) * 100) - 10)
      } else {
        text1 = String(Math.trunc((Number(item.doctorScore) % 1) * 100))
      }
      var text2 = '%'
      var concat = text1.concat(text2)
      if (Number(item.doctorScore) >= 1 && Number(item.doctorScore) < 2) {
        star[0].attributes[1].value = 'rgb(255, 185, 88)'
        star[1].attributes[1].value = 'rgb(255, 185, 88)'
        star[3].attributes[0].value = '0%'
        star[2].attributes[1].value = 'white'
        star[3].attributes[0].value = '0%'
        star[3].attributes[1].value = 'white'
        star[4].attributes[0].value = '0%'
        star[4].attributes[1].value = 'rgb(255, 185, 88)'
        star[5].attributes[0].value = concat
        star[5].attributes[1].value = 'rgb(255, 185, 88)'
        star[6].attributes[0].value = concat
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
      } else if (Number(item.doctorScore) >= 2 && Number(item.doctorScore) < 3) {
        star[0].attributes[1].value = 'rgb(255, 185, 88)'
        star[1].attributes[1].value = 'rgb(255, 185, 88)'
        star[2].attributes[1].value = 'rgb(255, 185, 88)'
        star[3].attributes[1].value = 'rgb(255, 185, 88)'
        star[4].attributes[1].value = 'rgb(255, 185, 88)'
        star[5].attributes[1].value = 'rgb(255, 185, 88)'
        star[6].attributes[1].value = 'rgb(255, 185, 88)'
        star[7].attributes[1].value = 'rgb(255, 185, 88)'
        star[8].attributes[0].value = concat
        star[8].attributes[1].value = 'rgb(255, 185, 88)'
        star[9].attributes[0].value = concat
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
      } else if (Number(item.doctorScore) >= 3 && Number(item.doctorScore) < 4) {
        star[0].attributes[1].value = 'rgb(255, 185, 88)'
        star[1].attributes[1].value = 'rgb(255, 185, 88)'
        star[2].attributes[1].value = 'rgb(255, 185, 88)'
        star[3].attributes[1].value = 'rgb(255, 185, 88)'
        star[4].attributes[1].value = 'rgb(255, 185, 88)'
        star[5].attributes[1].value = 'rgb(255, 185, 88)'
        star[6].attributes[1].value = 'rgb(255, 185, 88)'
        star[7].attributes[1].value = 'rgb(255, 185, 88)'
        star[8].attributes[1].value = 'rgb(255, 185, 88)'
        star[9].attributes[1].value = 'rgb(255, 185, 88)'
        star[10].attributes[1].value = 'rgb(255, 185, 88)'
        star[11].attributes[1].value = 'rgb(255, 185, 88)'
        star[12].attributes[0].value = concat
        star[12].attributes[1].value = 'rgb(255, 185, 88)'
        star[13].attributes[0].value = concat
        star[13].attributes[1].value = 'white'
        star[14].attributes[1].value = 'white'
        star[15].attributes[1].value = 'white'
        star[16].attributes[1].value = 'white'
        star[17].attributes[1].value = 'white'
        star[18].attributes[1].value = 'white'
        star[19].attributes[1].value = 'white'
      } else if (Number(item.doctorScore) >= 4 && Number(item.doctorScore) < 5) {
        star[0].attributes[1].value = 'rgb(255, 185, 88)'
        star[1].attributes[1].value = 'rgb(255, 185, 88)'
        star[2].attributes[1].value = 'rgb(255, 185, 88)'
        star[3].attributes[1].value = 'rgb(255, 185, 88)'
        star[4].attributes[1].value = 'rgb(255, 185, 88)'
        star[5].attributes[1].value = 'rgb(255, 185, 88)'
        star[6].attributes[1].value = 'rgb(255, 185, 88)'
        star[7].attributes[1].value = 'rgb(255, 185, 88)'
        star[8].attributes[1].value = 'rgb(255, 185, 88)'
        star[9].attributes[1].value = 'rgb(255, 185, 88)'
        star[10].attributes[1].value = 'rgb(255, 185, 88)'
        star[11].attributes[1].value = 'rgb(255, 185, 88)'
        star[12].attributes[1].value = 'rgb(255, 185, 88)'
        star[13].attributes[1].value = 'rgb(255, 185, 88)'
        star[14].attributes[1].value = 'rgb(255, 185, 88)'
        star[15].attributes[1].value = 'rgb(255, 185, 88)'
        star[16].attributes[1].value = 'rgb(255, 185, 88)'
        star[17].attributes[0].value = concat
        star[17].attributes[1].value = 'rgb(255, 185, 88)'
        star[18].attributes[0].value = concat
        star[18].attributes[1].value = 'white'
        star[19].attributes[1].value = 'white'
      } else if (Number(item.doctorScore) >= 0 && Number(item.doctorScore) < 1) {
        star[0].attributes[0].value = concat
        star[0].attributes[1].value = 'rgb(255, 185, 88)'
        star[1].attributes[0].value = concat
        star[1].attributes[1].value = 'white'
        star[2].attributes[1].value = 'white'
        star[3].attributes[1].value = 'white'
        star[4].attributes[1].value = 'white'
        star[5].attributes[1].value = 'white'
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
      } else if (Number(item.doctorScore) === 0) {
        star[0].attributes[1].value = 'white'
        star[1].attributes[1].value = 'white'
        star[2].attributes[1].value = 'white'
        star[3].attributes[1].value = 'white'
        star[4].attributes[1].value = 'white'
        star[5].attributes[1].value = 'white'
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
      } else if (Number(item.doctorScore) === 5) {
        star[0].attributes[1].value = 'rgb(255, 185, 88)'
        star[1].attributes[1].value = 'rgb(255, 185, 88)'
        star[3].attributes[1].value = 'rgb(255, 185, 88)'
        star[4].attributes[1].value = 'rgb(255, 185, 88)'
        star[5].attributes[1].value = 'rgb(255, 185, 88)'
        star[6].attributes[1].value = 'rgb(255, 185, 88)'
        star[7].attributes[1].value = 'rgb(255, 185, 88)'
        star[8].attributes[1].value = 'rgb(255, 185, 88)'
        star[9].attributes[1].value = 'rgb(255, 185, 88)'
        star[10].attributes[1].value = 'rgb(255, 185, 88)'
        star[11].attributes[1].value = 'rgb(255, 185, 88)'
        star[12].attributes[1].value = 'rgb(255, 185, 88)'
        star[13].attributes[1].value = 'rgb(255, 185, 88)'
        star[14].attributes[1].value = 'rgb(255, 185, 88)'
        star[15].attributes[1].value = 'rgb(255, 185, 88)'
        star[16].attributes[1].value = 'rgb(255, 185, 88)'
        star[17].attributes[1].value = 'rgb(255, 185, 88)'
        star[18].attributes[1].value = 'rgb(255, 185, 88)'
        star[19].attributes[1].value = 'rgb(255, 185, 88)'
      }
    })
  }
}
</script>
