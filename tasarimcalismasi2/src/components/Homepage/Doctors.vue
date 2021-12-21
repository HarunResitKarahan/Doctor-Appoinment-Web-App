<template>
  <div class="doctor">
      <p class="h4" style="margin-bottom: 15px;">En Beğenilen Doktorlardan Randevu Al</p>
      <p class="h5">Sistemdeki En Beğenilen Doktorlardan Randevu Alabilirsiniz.</p>
      <div class="doctor-cards">
        <VueSlickCarousel v-if="doctors.length > 0" :arrows="true" :speed="500" :variableWidth="true" :infinite="false" :slidesToScroll="3" :swipeToSlide="true" style="width: 80%;">
          <template v-for="item in doctors" >
            <div class="cards" :key = "item">
                <img src="@/assets/doctor1.jpg" width="240" height="160" style="border-radius: 10px;">
                <p class="doctor-name">{{item.doctorName}} {{item.doctorSurname}}</p>
                <p class="doctor-departmant">({{item.departmanID_id}})</p>
                <div class="star">
                    <span class="material-icons" >star</span ><p class="after">{{item.doctorScore}}</p><p>154 Değerlendirme</p>
                </div>
                <p class="doctor-location"><span class="material-icons">place</span>{{item.hospitalID_id}}</p>
                <p class="doctor-soon-appointmant"><span class="material-icons">schedule</span>Randevu Tarihi {{item.doctorCreateTime}}</p>
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
      data: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      doctors: []
    }
  },
  created () {
    fetch('http://localhost:8000/doctor/getdoctor', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        this.doctors = data
      })
  }
}
</script>
