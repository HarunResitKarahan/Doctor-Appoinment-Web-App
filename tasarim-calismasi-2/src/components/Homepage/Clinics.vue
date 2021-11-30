<template>
  <div class="clinic">
    <p class="h4" style="margin-bottom: 15px;">Poliklinikler ve Uzmanlar</p>
    <p class="h5">Sistem üzerindeki mevcut poliklinikleri ve uzmanları görebilirsniiz</p>
    <div class="policlinics">
        <template v-for="item in data" :key="item">
           <div style="flex: 1;" class="policlinics-card">
               <p>.</p>
           </div>
        </template>
        <!-- <VueSlickCarousel v-bind="settings">
          <div><h3>1</h3></div>
          <div><h3>1</h3></div>
          <div><h3>1</h3></div>
        </VueSlickCarousel> -->
    </div>
  </div>
</template>

<script>
  import VueSlickCarousel from '../../../node_modules/vue-slick-carousel'
  import '../../../node_modules/vue-slick-carousel/dist/vue-slick-carousel.css'
  import '../../../node_modules/vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  
export default {
  name: "Clinic",
  components: {
    VueSlickCarousel,
  },
  data () {
    return {
      settings: {
        arrows: true,
        speed: 500,
        variableWidth: true,
        infinite: true,
        slidesToScroll: 3,
        swipeToSlide: true
      },
      data: [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' '],
      policlinics: ['DAHİLİYE', 'KULAK BURUN BOĞAZ(K.B.B.)', 'CİLDİYE (DERMATOLOJİ)', 'FİZİK TEDAVİ VE REHABİLİTASYON', 'ORTOPEDİ VE TRAVMATOLOJİ', 'KARDİYOLOJİ', 'GÖZ HASTALIKLARI', 'NÖROLOJİ', 'PSİKİYATRİ(RUH HEKİMLİĞİ)', 'GÖĞÜS HASTALIKLARI', 'GÖĞÜS CERRAHİ', 'ÇOCUK HASTALIKLARI', 'KALP DAMAR CERRAHİ', 'KADIN DOĞUM', 'ÇOCUK CERRAHİ', 'BEYİN VE SİNİR CERRAHİSİ', 'ÜROLOJİ (BEVLİYE)', 'GENEL CERRAHİ'],
    }
  }
};
</script>