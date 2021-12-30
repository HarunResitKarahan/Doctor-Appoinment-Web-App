<template>
  <div class="booking-tab">
    <div class="doctor-info-tab">
        <template v-if="doctor[0].doctorSex == 'Kadın'">
          <div class="doctor-image">
            <img src="@/assets/femaledoctor.png" width="160" height="160">
          </div>
        </template>
        <template v-else>
          <div class="doctor-image">
            <img src="@/assets/maledoctor.png" width="160" height="160">
          </div>
        </template>
        <div class="doctor-info">
          <div class="datetext"><span class="material-icons">today</span><p class="h5">{{(dateday)}} {{months[datemonth - 1]}} {{dateyear}}</p></div>
            <div class="doctor-name">
                {{doctor[0].doctorName}} {{doctor[0].doctorSurname}}
            </div>
            <p style="font-size: 14px;color: #757575;margin-bottom: 5px;padding-left: 4px;">{{department}}</p>
            <div class="doctor-rank" style="margin: 0 0 7px 0">
                  <div class="star" :id="doctor[0].doctorID">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${doctor[0].doctorID}a)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${doctor[0].doctorID}a`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${doctor[0].doctorID}1)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${doctor[0].doctorID}1`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${doctor[0].doctorID}2)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${doctor[0].doctorID}2`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${doctor[0].doctorID}3)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${doctor[0].doctorID}3`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" :fill="`url(#${doctor[0].doctorID}4)`" stroke="rgb(255, 185, 88)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                      <linearGradient :id="`${doctor[0].doctorID}4`">
                          <stop  offset="0%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                          <stop  offset="60%" stop-color="white"/>
                          <stop  offset="100%" stop-color="white"/>
                      </linearGradient><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                      <p class="after">{{doctor[0].doctorScore}}</p><p>154 Değerlendirme</p>
                  </div>
              </div>
            <div class="doctor-departmant" style="margin-top: 10px;">
                <span class="material-icons" style="color: rgb(0, 0, 0, 0.500); font-size: 24px;padding: 1px;
    margin-right: 2px;">location_on</span><p style="padding-top: 3px;">{{hospitalName}}</p>
            </div>
        </div>
    </div>
    <div class="schedule-tab">
        <div @click="selectedDay" class="day">
            <!-- <VueSlickCarousel :arrows="true" :speed="500" :variableWidth="true" :infinite="false" :slidesToScroll="3" :swipeToSlide="true">
                <template v-for="index in 14">
                    <div @click="getappointment($event)" class="date" :key="index">
                        <p style="color: #272B41;">{{days[(day + index) - 1]}}</p>
                        <p class="h5" style="color: #757575;">{{newdate.getDate()}} {{months[datemonth - 1]}} {{newdate.getFullYear()}}</p>
                    </div>
                </template>
            </VueSlickCarousel> -->
            <template v-for="index in 14">
                <div @click="getappointment($event)" class="date" :key="index">
                    <p style="color: #272B41;">{{days[(day + index) - 1]}}</p>
                    <p class="h5" style="color: #757575;">{{newdate.getDate()}} {{months[datemonth - 1]}} {{newdate.getFullYear()}}</p>
                    <!-- <p class="h5" style="color: #757575;"><span class="dayy">{{newdate.getDate()}}</span> <span class="month">{{months[datemonth - 1]}}</span> <span class="year">{{dateyear}}</span></p> -->
                </div>
            </template>
        </div>
        <div class="schedule">
            <div class="time">
                <div>
                    <template v-for="item in time">
                        <div @click="selectedTime($event)" class="appointment" :key="item">
                            <p>{{item}}</p>
                        </div>
                    </template>
                </div>
            </div>
            <div class="make-a-apointment">
                <!-- <router-link :to="{name: 'AppointmentSuccessful', params: { dateday: dateday, datemonth: datemonth, dateyear: dateyear, doctor: doctor }}"><p>RANDEVU AL</p></router-link> -->
                    <!-- <router-link style="display: none;" :to="{name: 'AppointmentSuccessful', params: { dateday: dateday, datemonth: datemonth, dateyear: dateyear, doctor: doctor }}"><p>RANDEVU AL</p></router-link> -->
                    <a @click="randevuekle" style="display: none;"><p>RANDEVU AL</p></a>
                    <a>RANDEVU AL</a>
                <!-- :to="{ name: 'MakeAppointment', params: { } }" -->
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
// import Vue from 'vue'
// import VueSlickCarousel from 'vue-slick-carousel'
// import { mapState } from 'vuex'

export default {
  name: 'BookingTab',
  props: {
    doctorID: String,
    hospitalName: String,
    department: String,
    date: String
  },
  components: {
    // VueSlickCarousel
  },
  data () {
    return {
      // settings: {
      //   arrows: true,
      //   speed: 1000,
      //   variableWidth: true,
      //   infinite: false,
      //   slidesToScroll: 3,
      //   swipeToSlide: true
      // },
      days: ['PAZ', 'PZT', 'SAL', 'ÇAR', 'PER', 'CUM', 'CMT', 'PAZ', 'PZT', 'SAL', 'ÇAR', 'PER', 'CUM', 'CMT', 'PAZ', 'PZT', 'SAL', 'ÇAR', 'PER', 'CUM', 'CMT', 'PAZ', 'PZT', 'SAL', 'ÇAR', 'PER', 'CUM', 'CMT', 'PAZ'],
      months: ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'],
      dateday: Number,
      dateyear: Number,
      datemonth: Number,
      day: Number,
      time: ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00'],
      bookedtime: [],
      doctor: [],
      selectedtime: '',
      newdate: Date
    }
  },
  computed: {
    selectedtimeupdate: {
      get () {
        return this.selectedtime
      },
      set (value) {
        this.selectedtime = value
      }
    }
  },
  methods: {
    getappointment (event) {
      var date = event.target.parentNode.lastChild.textContent.split(' ')
      var month = this.getmonth(date[1])
      date = date[2] + '-' + String(month) + '-' + date[0]
      fetch('http://localhost:8000/schedule/getschedule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          scheduleDate: date,
          doctorID: this.doctor[0].doctorID
        })
      })
        .then(response => response.json())
        .then(data => {
          this.bookedtime = data
          $('.datetext p').text(event.target.parentNode.lastChild.textContent)
          if (this.bookedtime.length > 0) {
            this.bookedtime.forEach((item) => {
              $('.time div .appointment p').text((index, currentcontent) => {
                if (item[0] === '0') {
                  item = item.split('')
                  item.shift()
                  item = item.join('')
                }
                if (currentcontent === item) {
                  $('.time div:contains(' + currentcontent + ')').attr('class', 'booked')
                }
              })
            })
          } else {
            $('.booked').attr('class', 'appointment')
          }
        })
      this.selectedDate(event)
    },
    selectedDate (event) {
      var checkboxes = document.getElementsByClassName('date')
      checkboxes.forEach((item) => {
        if (item === event.target.parentNode) {
          event.target.parentNode.style.backgroundColor = 'rgba(73, 201, 188, 0.685)'
          event.target.parentNode.firstChild.style.color = 'white'
          event.target.parentNode.lastChild.style.color = 'white'
        } else {
          item.style.removeProperty('background-color')
          item.firstChild.style.removeProperty('color')
          item.lastChild.style.removeProperty('color')
        }
      })
    },
    selectedTime (event) {
      if (!$(event.target).hasClass('booked')) {
        if ($(event.target).hasClass('appointment')) {
          if ($(event.target).hasClass('selected')) {
            $(event.target).removeClass('selected')
            // this.selectedtime = ''
            // this.$set(this.$data, 'selectedtime', '')
            this.selectedtimeupdate = ''
          } else {
            $('.appointment').removeClass('selected')
            $(event.target).addClass('selected')
            // this.selectedtime = event.target.firstChild.textContent
            // this.$set(this.$data, 'selectedtime', event.target.firstChild.textContent)
            this.selectedtimeupdate = event.target.firstChild.textContent
          }
        } else if (event.target.tagName === 'P') {
          if (!$(event.target.parentNode).hasClass('booked')) {
            if ($(event.target.parentNode).hasClass('selected')) {
              $(event.target.parentNode).removeClass('selected')
              // this.selectedtime = ''
              // this.$set(this.$data, 'selectedtime', '')
              this.selectedtimeupdate = ''
            } else {
              $('.appointment').removeClass('selected')
              $(event.target.parentNode).addClass('selected')
              this.selectedtimeupdate = event.target.textContent
            }
          }
        }
      }
      // $('.make-a-apointment').html(this.template)
      if (this.selectedtime === '') {
        $('.make-a-apointment a:nth-child(1)').hide()
        $('.make-a-apointment a:nth-child(2)').show()
      } else {
        $('.make-a-apointment a:nth-child(2)').hide()
        $('.make-a-apointment a:nth-child(1)').show()
      }
    },
    randevuekle () {
      this.$router.push({ name: 'AppointmentSuccessful', params: { selectedtime: this.selectedtimeupdate, dateday: this.dateday, datemonth: this.datemonth, dateyear: this.dateyear, doctor: this.doctor, hospitalName: this.hospitalName, department: this.department } })
    },
    getmonth (month) {
      var i = 0
      this.months.forEach((item, index) => {
        if (item === month) {
          i = index
        }
      })
      return i + 1
    }
  },
  created () {
    $('.make-a-apointment a:nth-child(1)').hide()
    if (this.months.includes(this.date.split('-')[1])) {
      this.dateyear = Number(this.date.split('-')[0])
      this.dateday = Number(this.date.split('-')[2])
      this.datemonth = Number(this.months.indexOf(this.date.split('-')[1]) + 1)
      this.day = new Date(Number(this.date.split('-')[0]), Number(this.months.indexOf(this.date.split('-')[1])), Number(this.date.split('-')[2])).getDay()
    } else {
      this.dateyear = Number(this.date.split('-')[0])
      this.dateday = Number(this.date.split('-')[2])
      this.datemonth = Number(this.date.split('-')[1])
      this.day = new Date(Number(this.date.split('-')[0]), Number(this.date.split('-')[1]) - 1, Number(this.date.split('-')[2])).getDay()
    }
    this.newdate = new Date(this.dateyear, (this.datemonth - 1), this.dateday)
    fetch('http://localhost:8000/doctor/bookingdoctorinfo', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        doctorID: this.doctorID
      })
    })
      .then(response => response.json())
      .then(data => {
        this.doctor = data
        fetch('http://localhost:8000/schedule/getschedule', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            scheduleDate: this.date,
            doctorID: data[0].doctorID
          })
        })
          .then(response => response.json())
          .then(data => {
            this.bookedtime = data
            if (this.bookedtime.length > 0) {
              this.bookedtime.forEach((item) => {
                $('.time div .appointment p').text((index, currentcontent) => {
                  if (item[0] === '0') {
                    item = item.split('')
                    item.shift()
                    item = item.join('')
                  }
                  if (currentcontent === item) {
                    $('.time div:contains(' + currentcontent + ')').attr('class', 'booked')
                  }
                })
              })
            } else {
              $('.booked').attr('class', 'appointment')
            }
          })
      })
  },
  updated () {
    this.doctor.forEach((item) => {
      var id = String(item.doctorID)
      var hash = '#'
      hash = hash.concat(id)
      var getstar = $('.doctor-rank').find(hash)
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
      }
    })
    var date = document.getElementsByClassName('date')
    var datetext = document.querySelector('.datetext .h5').textContent
    date.forEach((item, index) => {
      if (index > 0) {
        this.newdate.setDate(this.newdate.getDate() + 1)
        if (this.newdate.getDate() === 1) {
          if (this.datemonth === 12) {
            this.datemonth = 1
            // this.newdate.setMonth(0)
            // this.newdate.setFullYear(this.newdate.getFullYear() + 1)
            this.dateyear += 1
          } else {
            this.datemonth += 1
            // this.newdate.setMonth(this.newdate.getMonth() + 1)
          }
        }
        item.querySelector('.h5').textContent = String(this.newdate.getDate()) + ' ' + this.months[this.datemonth - 1] + ' ' + this.newdate.getFullYear()
      }
      if (item.querySelector('.h5').textContent === datetext) {
        item.style.backgroundColor = 'rgba(73, 201, 188, 0.685)'
        item.style.transitionDuration = '0s'
        item.querySelector('.h5').style.transitionDuration = '0s'
        item.querySelector('.h5').style.color = 'white'
        item.querySelector('p').style.transitionDuration = '0s'
        item.querySelector('p').style.color = 'white'
      }
    })
  }
}
</script>
