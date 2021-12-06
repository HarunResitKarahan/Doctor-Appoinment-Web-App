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
        <div class="day">
            <template v-for="item in days">
                <div class="date" :key="item">
                    <p style="color: #272B41">{{item}}</p>
                    <p class="h5" style="color: #757575;">4 Aralık 2021</p>
                </div>
            </template>
        </div>
        <div class="schedule">
            <div class="time">
                <div v-for="item in days" :key="item">
                    <div style="display: none;" >{{item}}</div>
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

export default {
  name: 'BookingTab',
  data () {
    return {
      days: ['PZT', 'SAL', 'ÇAR', 'PER', 'CUM', 'CMT'],
      time: ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30']
    }
  },
  mounted () {
    $(document).ready(function () {
      $('.appointment').click(function () {
        $('.appointment').css('background-color', '#e9e9e9')// background-color: #e9e9e9;color: #757575;
        $('.appointment').css('color', '#757575')
        $(this).css('background-color', '#66b7cb')// background-color: #e9e9e9;color: #757575;
        $(this).css('color', 'white')
      })
    })
  }
}
</script>
