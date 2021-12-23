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
                    <li><i><strong>Tarih:</strong></i><i> 20 Aralık 2021 9:30</i></li>
                    <li><i><strong>Doktor:</strong></i><i> Enes Demir</i></li>
                    <li><i><strong>Bölüm:</strong></i><i> Dahiliye</i></li>
                    <li><i><strong>Hastane:</strong></i><i> Şevket Yılmaz Devlet Hastanesi</i></li>
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
  created () {}
}
</script>
