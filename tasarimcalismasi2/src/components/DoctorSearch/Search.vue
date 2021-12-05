<template>
  <div class="search col-3">
    <div class="filter-search">
        <h5>Filtreli Arama</h5>
        <div class="card-body">
            <input type="date" id="date">
            <h6 style="font-size: 15px;margin-top: 20px;">Cinsiyet</h6>
            <label class="checkbox">
                  <input type="checkbox"><p style="text-align: left;">Erkek</p>
            </label>
            <label class="checkbox">
                  <input type="checkbox"><p style="text-align: left;">Kadın</p>
            </label>
            <h6 style="font-size: 15px;margin-top: 20px;">Poliklinik</h6>
            <template v-for="item in policlinics">
              <label class="checkbox" :key="item">
                <input type="checkbox"><p style="text-align: left;">{{item}}</p>
              </label>
            </template>
        </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Search',
  data () {
    return {
      policlinics: ['Dahiliye', 'Kulak Burun Boğaz (K.B.B)', 'Cildiye (Dermatoloji)', 'Fizik Tedavi ve Rehabilitasyon', 'Ortopedi ve Travmatoloji', 'Kardiyoloji', 'Göz Hastalıkları', 'Nöroloji', 'Psikiyatri (Ruh Hekimliği)', 'Göğüs Hastalıkları', 'Göğüs Cerrahi', 'Çocuk Hastalıkları', 'Kalp Damar Cerrahi', 'Kadın Doğum', 'Çocuk Cerrahi', 'Beyin ve Sinir Cerrahisi', 'Üroloji (Bevliye)', 'Genel Cerrahi']
    }
  },
  mounted () {
    document.getElementById('date').valueAsDate = new Date()
  }
}
</script>
