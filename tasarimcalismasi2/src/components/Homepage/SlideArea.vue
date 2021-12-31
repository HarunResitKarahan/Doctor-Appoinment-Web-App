<template>
  <div class="slide-area">
      <div class="image col-6 col-xl-7 col-lg-7 col-md-7" align="Right">
          <img style="border-radius: 30px;" src="@/./assets/hospital.png" width="600" height="400" alt="">
      </div>
      <div class="col-6 col-xl-5 col-lg-5 col-md-5">
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
                  <select v-model="gender" name="sex" id="sex">
                    <option value="" selected disabled hidden>Cinsiyet Seçin</option>
                    <option value="Erkek">Erkek</option>
                    <option value="Kadın">Kadın</option>
                  </select>
              </div>
              <div class="location">
                  <span>Bölüm</span>
                  <select v-model="department" name="department" id="department">
                    <option value="" selected disabled hidden>Bölüm Seçin</option>
                    <template v-for="(item,index) in policlinics">
                      <option :value="item.departmanName" :key="index">{{item.departmanName}}</option>
                    </template>
                  </select>
              </div>
              <div class="search">
                <template v-if="location == '' || gender == '' || department == ''">
                  <p style="background-color: rgb(126, 187, 181);border-radius: 15px;color: white; font-weight: 400;padding: 20px;">Randevu Bul</p>
                </template>
                <template v-if="location != '' && gender != '' && department != ''">
                  <router-link :to="{ name: 'DoctorSearch', params: { location: location, gender: gender, department: department } }"><p style="color: #212529; font-weight: 400;padding: 20px;">Randevu Bul</p></router-link>
                </template>
              </div>
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
      gender: '',
      department: '',
      policlinics: [],
      city: []
    }
  },
  created () {
    fetch('http://127.0.0.1:8000/department/getclinics', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        this.policlinics = data
      })
    fetch('http://127.0.0.1:8000/city/getcitys', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        this.city = data
      })
  }
}
</script>
