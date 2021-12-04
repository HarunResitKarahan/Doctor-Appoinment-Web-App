<template>
  <div class="booking-tab">
    <div class="doctor-info-tab">
        <div class="doctor-image">
            <img src="@/assets/doctor11.jpg" width="80" height="80">
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
            <div class="doctor-departmant">
                <span class="material-icons" style="color: rgb(255, 0, 0, 0.500); font-size: 24px;padding: 1px;
    margin-right: 2px;">emergency</span><p style="padding-top: 2px;">Şevket Yılmaz Devlet Hastanesi</p>
            </div>
        </div>
    </div>
    <div class="schedule-tab">
        <div class="day">
            <template v-for="item in days">
                <p :key="item">
                    {{item}}
                </p>
            </template>
        </div>
        <div class="time">
            .
        </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'BookingTab',
  data () {
    return {
      days: ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma']
    }
  },
  mounted () {
    document.title = 'Randevu Al'
  }
}
</script>
