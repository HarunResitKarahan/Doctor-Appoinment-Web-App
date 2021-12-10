<template>
  <div class="booking-tab">
    <div class="doctor-info-tab">
        <div class="doctor-image">
            <img src="@/assets/doctor11.jpg" width="100" height="100">
        </div>
        <div class="doctor-info">
            <div class="doctor-name">
                Enes DEMİR
            </div>
            <div class="doctor-rank">
                <div class="star">
                    <span class="material-icons" >star</span ><span class="material-icons" >star</span ><span class="material-icons" >star</span ><span class="material-icons" >star</span ><span class="material-icons" >star</span ><p class="after">4.7</p><p style="height: 22px;">154 Değerlendirme</p>
                </div>
            </div>
            <div class="doctor-departmant" style="margin-top: 10px;">
                <span class="material-icons" style="color: rgb(0, 0, 0, 0.500); font-size: 24px;padding: 1px;
    margin-right: 2px;">location_on</span><p style="padding-top: 3px;">Şevket Yılmaz Devlet Hastanesi</p>
            </div>
        </div>
    </div>
    <div class="schedule-tab">
        <div @click="selectedDay" class="day">
            <VueSlickCarousel v-bind="settings">
                <template v-for="(item,index) in days">
                    <div class="date" :key="item">
                        <p style="color: #272B41">{{item}}</p>
                        <p class="h5" style="color: #757575;">{{index + 1}} Aralık 2021</p>
                    </div>
                </template>
            </VueSlickCarousel>
        </div>
        <div class="schedule">
            <div class="time">
                <div>
                    <template v-for="item in time">
                        <div class="appointment" :key="item">
                            <p>{{item}}</p>
                        </div>
                    </template>
                </div>
            </div>
            <div class="make-a-apointment">
                <p>RANDEVU AL</p>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
import VueSlickCarousel from 'vue-slick-carousel'

export default {
  name: 'BookingTab',
  components: {
    VueSlickCarousel
  },
  data () {
    return {
      settings: {
        arrows: true,
        speed: 1000,
        variableWidth: true,
        infinite: false,
        slidesToScroll: 3,
        swipeToSlide: true
      },
      days: ['PZT', 'SAL', 'ÇAR', 'PER', 'CUM', 'CMT', 'PAZ', 'PZT', 'SAL', 'ÇAR', 'PER', 'CUM', 'CMT', 'PAZ'],
      time: ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30']
    }
  },
  mounted () {
    $(document).ready(function () {
      $('.appointment').click(function () {
        if ($(this).hasClass('selected')) {
          $(this).removeClass('selected')
        } else {
          $('.appointment').removeClass('selected')
          $(this).addClass('selected')
        }
      })
      $('.date').click(function () {
        $('.date').css('background-color', 'white')
        $(this).css('background-color', '#00c4f4')
      })
    })
  }
}
</script>
