<template>
  <div class="clinic">
    <p class="h4" style="margin-bottom: 15px;">Poliklinikler ve Uzmanlar</p>
    <p class="h5">Sistem üzerindeki mevcut poliklinikleri ve uzmanları görebilirsniiz</p>
    <div class="policlinics">
        <template v-for="item in policlinics" :key="item">
           <div style="flex: 60%;" class="policlinics-card">
               <p>{{item}}</p>
           </div>
        </template>
    </div>
  </div>
</template>

<script>
export default {
  name: "Clinic",
  data () {
    return {
      policlinics: ['DAHİLİYE', 'KULAK BURUN BOĞAZ(K.B.B.)', 'CİLDİYE (DERMATOLOJİ)', 'FİZİK TEDAVİ VE REHABİLİTASYON', 'ORTOPEDİ VE TRAVMATOLOJİ', 'KARDİYOLOJİ', 'GÖZ HASTALIKLARI', 'NÖROLOJİ', 'PSİKİYATRİ(RUH HEKİMLİĞİ)', 'GÖĞÜS HASTALIKLARI', 'GÖĞÜS CERRAHİ', 'ÇOCUK HASTALIKLARI', 'KALP DAMAR CERRAHİ', 'KADIN DOĞUM', 'ÇOCUK CERRAHİ', 'BEYİN VE SİNİR CERRAHİSİ', 'ÜROLOJİ (BEVLİYE)', 'GENEL CERRAHİ'],
    }
  }
};
</script>