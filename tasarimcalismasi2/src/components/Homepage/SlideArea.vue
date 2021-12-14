<template>
  <div class="slide-area">
      <div class="image">
          <img style="border-radius: 30px;" src="@/./assets/hospital.png" width="600" height="400" alt="">
      </div>
      <div class="appointment-tab">
          <h2>Doktorunu Seç, Randevunu Al</h2>
          <div class="inputs">
              <div style="margin-top: 35px" class="location">
                  <span>Şehir</span>
                  <select v-model="location" style="margin-bottom: 15px;" name="department" id="department" default="Bölüm Seçin">
                    <option value="" selected disabled hidden>Şehir Seçin</option>
                    <option value="Bursa">Bursa</option>
                    <option value="İstanbul">İstanbul</option>
                    <option value="İzmir">İzmir</option>
                    <option value="Ankara">Ankara</option>
                  </select>
              </div>
              <div class="location">
                  <span>Cinsiyet</span>
                  <select v-model="sex" name="sex" id="sex">
                    <option value="" selected disabled hidden>Cinsiyet Seçin</option>
                    <option value="Erkek">Erkek</option>
                    <option value="Kadın">Kadın</option>
                  </select>
              </div>
              <div class="location">
                  <span>Bölüm</span>
                  <select v-model="department" name="department" id="department">
                    <option value="" selected disabled hidden>Bölüm Seçin</option>
                    <option value="Göz Hastalıkları">GÖZ HASTALIKLARI</option>
                    <option value="Beyin ve Sinir Cerrahisi">BEYİN VE SİNİR CERRAHİSİ</option>
                    <option value="Nöroloji">NÖROLOJİ</option>
                    <option value="Genel Cerrahi">GENEL CERRAHİ</option>
                  </select>
              </div>
              <div class="search">
                <template v-if="location == '' || sex == '' || department == ''">
                  <p style="background-color: rgb(126, 187, 181);border-radius: 15px;color: white; font-weight: 400;padding: 20px;">Randevu Bul</p>
                </template>
                <template v-if="location != '' && sex != '' && department != ''">
                  <router-link :to="{ name: 'DoctorSearch', params: { location: location, sex: sex, department: department } }"><p style="color: #212529; font-weight: 400;padding: 20px;">Randevu Bul</p></router-link>
                </template>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'SlideArea',
  data () {
    return {
      location: '',
      sex: '',
      department: ''
    }
  }
}
</script>
