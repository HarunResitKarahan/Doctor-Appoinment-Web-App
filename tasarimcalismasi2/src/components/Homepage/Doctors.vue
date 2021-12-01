<template>
  <div class="doctor">
      <p class="h4" style="margin-bottom: 15px;">En Beğenilen Doktorlardan Randevu Al</p>
      <p class="h5">Sistemdeki En Beğenilen Doktorlardan Randevu Alabilirsiniz.</p>
      <div class="doctor-cards">
          <template v-for="item in doctors" >
            <div class="cards" :key = "item">
                <img src="@/././assets/doctor1.jpg" width="240" style="border-radius: 10px;">
                <p class="doctor-name">{{item}}</p>
                <p class="doctor-departmant">(Dahiliye)</p>
                <div class="star">
                    <span class="material-icons" >star</span><p>4.7</p><div style="background: black;border-radius: 30px;width: 2px;height: 2px;margin-top: auto;margin-bottom: auto;margin-left: 5px;margin-right: 5px;"> </div><p>154 Değerlendirme</p>
                </div>
                <p class="doctor-location"><span class="material-icons">place</span>Şevket Yılmaz Devlet Hastanesi</p>
                <p class="doctor-soon-appointmant"><span class="material-icons">schedule</span>Randevu Tarihi 23 Ocak 2022</p>
                <div class="sent">
                    <a href="#" class="sent">Randevu Al</a>
                </div>
            </div>
          </template>
      </div>
  </div>
</template>

<script>

export default {
  name: 'Doctors',
  data () {
    return {
      data: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      doctors: ['Ahmet Furkan ÇELİK', 'Mehmet Akif ÇELİKTÜRK', 'Fatma ARICI', 'Enes DEMİR']
    }
  }
}
</script>
