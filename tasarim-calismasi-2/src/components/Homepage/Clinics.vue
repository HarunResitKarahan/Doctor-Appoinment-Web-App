<template>
  <div class="clinic">
    <p class="h4" style="margin-bottom: 15px;">Poliklinikler ve Uzmanlar</p>
    <p class="h5">Sistem üzerindeki mevcut poliklinikleri ve uzmanları görebilirsniiz</p>
    <div data-slick='{"slidesToShow": 4, "slidesToScroll": 4}' class="policlinics">
        <template v-for="item in data" :key="item">
           <div style="flex: 1;" class="policlinics-card">
               <p>.</p>
           </div>
        </template>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "Clinic",

  data () {
    return {
      data: [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' '],
      policlinics: ['DAHİLİYE', 'KULAK BURUN BOĞAZ(K.B.B.)', 'CİLDİYE (DERMATOLOJİ)', 'FİZİK TEDAVİ VE REHABİLİTASYON', 'ORTOPEDİ VE TRAVMATOLOJİ', 'KARDİYOLOJİ', 'GÖZ HASTALIKLARI', 'NÖROLOJİ', 'PSİKİYATRİ(RUH HEKİMLİĞİ)', 'GÖĞÜS HASTALIKLARI', 'GÖĞÜS CERRAHİ', 'ÇOCUK HASTALIKLARI', 'KALP DAMAR CERRAHİ', 'KADIN DOĞUM', 'ÇOCUK CERRAHİ', 'BEYİN VE SİNİR CERRAHİSİ', 'ÜROLOJİ (BEVLİYE)', 'GENEL CERRAHİ'],
    }
  },
  mounted () {
    $(document).ready(function () {
      $(".policlinics").slick()
    })
  }
};
</script>