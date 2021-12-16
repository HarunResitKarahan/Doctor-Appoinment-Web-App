<template>
  <div class="doctor">
      <p class="h4" style="margin-bottom: 15px;">En Beğenilen Doktorlardan Randevu Al</p>
      <p class="h5">Sistemdeki En Beğenilen Doktorlardan Randevu Alabilirsiniz.</p>
      <div class="doctor-cards">
        <VueSlickCarousel v-bind="settings" style="width: 80%;">
          <template v-for="item in doctors" >
            <div class="cards" :key = "item">
                <img src="@/assets/doctor1.jpg" width="240" height="160" style="border-radius: 10px;">
                <p class="doctor-name">{{item}}</p>
                <p class="doctor-departmant">(Dahiliye)</p>
                <div class="star">
                    <span class="material-icons" >star</span ><p class="after">4.7</p><p>154 Değerlendirme</p>
                </div>
                <p class="doctor-location"><span class="material-icons">place</span>Şevket Yılmaz Devlet Hastanesi</p>
                <p class="doctor-soon-appointmant"><span class="material-icons">schedule</span>Randevu Tarihi 23 Ocak 2022</p>
                <div class="sent">
                    <a href="#" class="sent">Randevu Al</a>
                </div>
            </div>
          </template>
        </VueSlickCarousel>
      </div>
  </div>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  name: 'Doctors',
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
      data: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      doctors: ['Ahmet Furkan ÇELİK', 'Mehmet Akif ÇELİKTÜRK', 'Fatma ARICI', 'Enes DEMİR']
    }
  }
}
</script>
