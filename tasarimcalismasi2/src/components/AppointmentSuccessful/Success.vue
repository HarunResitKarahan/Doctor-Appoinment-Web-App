<template>
  <div class="success-comp">
    {{this.$route.params}}
      <div class="success">
        <div class="verify"><span class="material-icons">verified</span></div>
        <div class="appointment-info">
            <p class="successfull"><i>BAŞARIYLA RANDEVU ALINDI</i><span class="material-icons">check</span></p>
            <div class="successfull-info">
                <p><i>Randevu Bilgileri: </i></p>
                <ul>
                    <li><i><strong>Tarih:</strong></i><i> {{this.$route.params.dateday}} {{months[this.$route.params.datemonth - 1]}} {{this.$route.params.dateyear}} {{this.$route.params.selectedtime}}</i></li>
                    <li><i><strong>Doktor:</strong></i><i> {{this.$route.params.doctor[0].doctorName}} {{this.$route.params.doctor[0].doctorSurname}}</i></li>
                    <li><i><strong>Bölüm:</strong></i><i> {{this.$route.params.department}}</i></li>
                    <li><i><strong>Hastane:</strong></i><i> {{this.$route.params.hospitalName}}</i></li>
                </ul>
            </div>
        </div>
    </div>
    <div>
       <router-link to="/"><p class="return-homepage">Ana Sayfa'ya Dön</p></router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Success',
  props: {
    doctor: Array,
    dateyear: Number,
    datemonth: Number,
    selectedtime: undefined,
    dateday: Number
  },
  data () {
    return {
      months: ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
    }
  }
}
</script>
