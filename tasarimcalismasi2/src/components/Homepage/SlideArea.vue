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
                  <select style="margin-bottom: 15px;" name="department" id="department">
                    <option value="bursa">Bursa</option>
                    <option value="istanbul">İstanbul</option>
                    <option value="izmir">İzmir</option>
                    <option value="ankara">Ankara</option>
                  </select>
              </div>
              <div class="location">
                  <span>Cinsiyet</span>
                  <select name="sex" id="sex">
                    <option value="male">Erkek</option>
                    <option value="female">Kadın</option>
                  </select>
              </div>
              <div class="location">
                  <span>Bölüm</span>
                  <select name="department" id="department">
                    <option value="göz">GÖZ HASTALIKLARI</option>
                    <option value="beyin">BEYİN VE SİNİR CERRAHİSİ</option>
                    <option value="noroloji">NÖROLOJİ</option>
                    <option value="cerrahi">GENEL CERRAHİ</option>
                  </select>
              </div>
              <div class="search">
                  <router-link to="/about"><p style="color: #212529; font-weight: 400;padding: 20px;">Randevu Bul</p></router-link>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'SlideArea'
}
</script>
