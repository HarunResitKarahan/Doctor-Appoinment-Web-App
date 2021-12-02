<template>
  <div class="clinic">
    <p class="h4" style="margin-bottom: 15px;">Poliklinikler ve Uzmanlar</p>
    <p class="h5">Sistem üzerindeki mevcut poliklinikleri ve uzmanları görebilirsniiz</p>
    <div class="policlinics">
        <VueSlickCarousel v-bind="settings" style="width: 65%;">
          <template v-for="item in policlinics" >
            <div class="policlinics-card" :key="item">
                <p>{{item}}</p>
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
  name: 'Clinic',
  components: {
    VueSlickCarousel
  },
  data () {
    return {
      settings: {
        dots: true,
        arrows: false,
        speed: 500,
        variableWidth: true,
        infinite: true,
        slidesToScroll: 3,
        swipeToSlide: true
      },
      data: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      policlinics: ['DAHİLİYE', 'KULAK BURUN BOĞAZ(K.B.B.)', 'CİLDİYE (DERMATOLOJİ)', 'FİZİK TEDAVİ VE REHABİLİTASYON', 'ORTOPEDİ VE TRAVMATOLOJİ', 'KARDİYOLOJİ', 'GÖZ HASTALIKLARI', 'NÖROLOJİ', 'PSİKİYATRİ(RUH HEKİMLİĞİ)', 'GÖĞÜS HASTALIKLARI', 'GÖĞÜS CERRAHİ', 'ÇOCUK HASTALIKLARI', 'KALP DAMAR CERRAHİ', 'KADIN DOĞUM', 'ÇOCUK CERRAHİ', 'BEYİN VE SİNİR CERRAHİSİ', 'ÜROLOJİ (BEVLİYE)', 'GENEL CERRAHİ']
    }
  }
}
</script>
