<template>
  <div class="profile-component">
      <div class="profile-info col-3">
        <div class="card-body">
          <img src="@/assets/malephoto.png" width="150" height="150">
          <p style="font-weight: 500;">{{userinfo.patientName}} {{userinfo.patientSurname}}</p>
          <p style="color: #757575;
                    font-size: 13px;
                    font-weight: normal;
                    margin-top: 8px;
                    margin-bottom: 8px;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    white-space: nowrap;"
                    ><b>TC Kimlik No:</b> {{userinfo.patientID}} </p>
        <div style="text-align: left;
                    width: 100%;
                    margin-top:30px;
                    padding: 15px; ">
            <p class="h6" style="margin:0;margin-bottom: 5px;">Son Randevular</p>
            <div style="display: flex;
                        width: 100%;
                        padding: 20px 5px;
                        border: 0 solid #f0f0f0;
                        border-top-width: 1px;
                        border-bottom-width: 1px;" v-for="item in 3" :key="item">
              <template v-if="doctor[0].doctorSex == 'Erkek'">
                <div>
                  <img src="@/assets/maledoctor.png" width="55" height="55" style="border-radius: 100%;">
                </div>
              </template>
              <template v-else>
                <div>
                   <img src="@/assets/femaledoctor.png" width="55" height="55" style="border-radius: 100%;">
                </div>
              </template>
              <div>
                <p style="margin-left: 8px;font-weight: 500;font-size: 0.9rem;">Enes Demir</p>
                <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">(Dahiliye)</p>
                <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">9 Aralık 2021 10:30</p>
              </div>
            </div>
        </div>
        </div>
      </div>
      <div class="booking-history col-9">
        <div style="padding: 20px;
                    border: 0 solid #f0f0f0;
                    border-bottom-width: 1px;
                    width: 100%;
                    text-align: center;
                    height: fit-content;">
          <p style="font-weight: 500;letter-spacing: 1.8px;">Randevu Geçmişi</p>
        </div>
        <div style="overflow: auto;width: 100%">
          <table style="width: 100%;">
            <tr>
              <th>Doktor</th>
              <th>Bölüm</th>
              <th>Randevu Tarihi</th>
              <th>Puanla</th>
            </tr>
            <tr v-for="(i,index) in appointments" :key="index">
              <td><div style="display: flex;
                          align-items: center;
                          width: 100%;">
                <div>
                  <img src="@/assets/maledoctor.png" width="55" height="55" style="border-radius: 100%;">
                </div>
                <div>
                  <p style="margin-left: 16px;font-weight: 500;font-size: 0.9rem;">{{i.appointmentDoctorID_id}}</p>
                </div>
              </div></td>
              <td><div>{{i.appointmentDepartmanID_id}}</div></td>
              <td><div>{{i.appointmentTime}}</div> </td>
              <td style="display: flex;justify-content: space-between;align-items: center;padding: 15px;width: 80%;" >
                <div class="rate"  v-for="item in 11" :key="item" style="display:flex;
                                                                         align-items: center;
                                                                         justify-content: center;
                                                                         width: 24px;
                                                                         height: 24px;
                                                                         border: 2px solid gray;
                                                                         border-radius: 100%;
                                                                         transition-duration: 0s;">
                  <span style="font-size: 12px;
                               font-weight: 600;
                               padding-top: 2px;">
                    {{item}}
                  </span>
                </div>
                <div class="rate-show" style="display:none; text-align: center;">
                  Randevuya Verdiğiniz Puan:
                </div>
              </td>
            </tr>
          </table>
        </div>
      </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'ProfileComponent',
  data () {
    return {
      issignin: '',
      isregistered: '',
      userinfo: '',
      appointments: [],
      doctor: [],
      months: ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
    }
  },
  created () {
    this.localusername = localStorage.username
    this.issignin = localStorage.issignin
    fetch('http://localhost:8000/patient/getuser', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        patientID: localStorage.username
      })
    })
      .then(res => res.json())
      .then(data => {
        this.userinfo = data[0]
        // this.date = data[0].userCreateTime.split('T')
      })
    fetch('http://localhost:8000/appointment/getappointment', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        appointmentPatientID_id: localStorage.username
      })
    })
      .then(res => res.json())
      .then(data => {
        this.appointments = data
        this.appointments.forEach((item) => {
          var day = item.appointmentTime.split('T')[0].split('-')[2]
          var month = item.appointmentTime.split('T')[0].split('-')[1]
          var year = item.appointmentTime.split('T')[0].split('-')[0]
          var hour = item.appointmentTime.split('T')[1].split(':')[0]
          var minute = item.appointmentTime.split('T')[1].split(':')[1]
          item.appointmentTime = day + ' ' + this.months[month - 1] + ' ' + year + ' ' + hour + ':' + minute
          console.log(day + ' ' + month + ' ' + year + ' ' + hour + ':' + minute)
        })
      })
    fetch('http://localhost:8000/appointment/getappointment', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        appointmentPatientID_id: localStorage.username
      })
    })
      .then(res => res.json())
      .then(data => {
        this.doctor = data
      })
  },
  mounted () {
    $(document).ready(function () {
      // ----height option----
      var height = $('.card-body').css('height')
      $('.booking-history').css('height', height)
      height = $('tr td:nth-child(1)').css('height')
      $('td').css('height', height)
      // --------
      $('.rate').hover(function () {
        $(this).next().prevAll('.rate:nth-child(n + 1):nth-child(-n + 3)').css({ 'background-color': '#ff6240', color: 'white' })
        $(this).next().prevAll('.rate:nth-child(n + 4):nth-child(-n + 7)').css({ 'background-color': '#f6a31c', color: 'white' })
        $(this).next().prevAll('.rate:nth-child(n + 8):nth-child(-n + 10)').css({ 'background-color': '#29cc81', color: 'white' })
      }, function () {
        $(this).next().prevAll('.rate:nth-child(n + 1):nth-child(-n + 3)').css({ 'background-color': 'white', color: '#ff6240' })
        $(this).next().prevAll('.rate:nth-child(n + 4):nth-child(-n + 7)').css({ 'background-color': 'white', color: '#f6a31c' })
        $(this).next().prevAll('.rate:nth-child(n + 8):nth-child(-n + 10)').css({ 'background-color': 'white', color: '#29cc81' })
      })
      $('.rate').click(function () {
        var rate = $(this).text()
        $(this).parent('td').find('.rate').hide()
        $(this).parent('td').find('.rate-show').append(rate)
        $(this).parent('td').css('justify-content', 'center')
        $(this).parent('td').find('.rate-show').css('display', 'block')
      })
    })
  }
}
</script>
