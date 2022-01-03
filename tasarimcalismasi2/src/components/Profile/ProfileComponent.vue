<template>
  <div class="profile-component">
      <div class="profile-info col-3">
        <div class="card-body">
          <template v-if="userinfo.patientSex == 'Erkek'">
            <div>
              <img src="@/assets/malephoto.png" width="150" height="150">
            </div>
          </template>
          <template v-else>
            <div>
              <img src="@/assets/femalephoto.png" width="150" height="150">
            </div>
          </template>
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
            <template v-if="appointments.length > 0">
              <div v-for="(item,index) in reverseappointments3" :key="index" style="display: flex;
                          width: 100%;
                          padding: 20px 5px;
                          border: 0 solid #f0f0f0;
                          border-top-width: 1px;
                          border-bottom-width: 1px;">
                <!-- <template v-if="doctor[0].doctorSex == 'Erkek'">
                  <div>
                    <img src="@/assets/maledoctor.png" width="55" height="55" style="border-radius: 100%;">
                  </div>
                </template> -->
                <template v-if="item.doctorSex == 'Erkek'">
                  <div>
                    <img src="@/assets/maledoctor.png" width="55" height="55" style="border-radius: 100%;">
                  </div>
                </template>
                <template v-else>
                  <img src="@/assets/femaledoctor.png" width="55" height="55" style="border-radius: 100%;">
                </template>
                <div>
                  <p style="margin-left: 8px;font-weight: 500;font-size: 0.9rem;">{{appointments[index].appointmentDoctorID_id}}</p>
                  <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">({{appointments[index].appointmentDepartmanID_id}})</p>
                  <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">{{appointments[index].appointmentTime}}</p>
                </div>
              </div>
            </template>
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
            <tr class="doctors" v-for="(i,index) in reverseappointments" :key="index">
              <td><div style="display: flex;
                          align-items: center;
                          width: 100%;">
                <template v-if="i.doctorSex == 'Erkek'">
                  <div>
                    <img src="@/assets/maledoctor.png" width="55" height="55" style="border-radius: 100%;">
                  </div>
                </template>
                <template v-else>
                  <img src="@/assets/femaledoctor.png" width="55" height="55" style="border-radius: 100%;">
                </template>
                <div>
                  <p style="margin-left: 16px;font-weight: 500;font-size: 0.9rem;">{{i.appointmentDoctorID_id}}</p>
                </div>
              </div></td>
              <td><div>{{i.appointmentDepartmanID_id}}</div></td>
              <td><div>{{i.appointmentTime}}</div> </td>
              <td :id="i.id" style="display: flex;justify-content: space-between;align-items: center;padding: 15px;margin-right: 30px;" >
                <template v-if="i.appointmentPoint == null && new Date(Number(i.year), Number(i.month), Number(i.day), Number(i.hour), Number(i.minute), 0) < new Date()">
                  <div class="rate" v-for="item in 11" :key="item" style="display:flex;
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
                  <div class="rate-show" style="display:none;">
                    Randevuya Verdiğiniz Puan:
                  </div>
                </template>
                <template v-if="i.appointmentPoint == null && new Date(Number(i.year), Number(i.month), Number(i.day), Number(i.hour), Number(i.minute), 0) > new Date()">
                  <div style="width: 100%">
                    Randevunuza Gidiniz !
                  </div>
                </template>
                <template v-if="i.appointmentPoint != null ">
                  <div style="width: 100%;">
                    Randevuya Verdiğiniz Puan: {{i.appointmentPoint}}
                  </div>
                </template>
              </td>
              <template v-if="new Date(Number(i.year), Number(i.month), Number(i.day), Number(i.hour), Number(i.minute), 0) > new Date()">
                <td>
                  <p @click="cancel(i.id)" class="cancel">Randevuyu İptal Et</p>
                </td>
              </template>
              <template v-else>
                <td>
                </td>
              </template>
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
      reverseappointments: [],
      reverseappointments3: [],
      doctor: [],
      months: ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
    }
  },
  methods: {
    checktime (appointmentTime) {
      var split = appointmentTime.split(' ')
      var splittime = split[3].split(':')
      const d = new Date(split[2], this.months.findIndex(split[1]), split[0], splittime[0], splittime[1])
      print(d)
      return true
    },
    cancel (appointmentID) {
      fetch('http://127.0.0.1:8000/appointment/getappointment', {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          id: appointmentID
        })
      })
      // .then(res => res.json())
      // .then(data => {
      //   this.userinfo = data[0]
      //   // this.date = data[0].userCreateTime.split('T')
      // })
      console.log(event.target.parentNode.parentElement.style.css = 'none')
      event.target.parentNode.parentElement.style.display = 'none'
    }
  },
  created () {
    this.localusername = localStorage.username
    this.issignin = localStorage.issignin
    fetch('http://127.0.0.1:8000/patient/getuser', {
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
    fetch('http://127.0.0.1:8000/appointment/getappointment', {
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
          item.day = day
          item.month = month - 1
          item.year = year
          item.hour = hour
          item.minute = minute
        })
        this.reverseappointments = this.appointments.reverse()
        if (this.reverseappointments.length >= 3) {
          this.reverseappointments3[0] = this.reverseappointments[0]
          this.reverseappointments3[1] = this.reverseappointments[1]
          this.reverseappointments3[2] = this.reverseappointments[2]
        } else {
          this.reverseappointments.forEach((item) => {
            this.reverseappointments3.push(item)
          })
        }
      })
  },
  updated () {
    // ----height option----
    var height = $('.card-body').css('height')
    $('.booking-history').css('height', height)
    height = $('tr td:nth-child(1)').css('height')
    $('td').css('height', height)
    // ---------------------------
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
      fetch('http://127.0.0.1:8000/appointment/getappointment', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          id: Number($(this).parent('td').attr('id')),
          appointmentPoint: rate
        })
      })
    })
  }
}
</script>
