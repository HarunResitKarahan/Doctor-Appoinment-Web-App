<template>
  <div class="show-doctors">
    <template v-for="item in doctors">
      <div class="doctor-card" :key="item">
        <div class="doctor-image">
          <img src="@/assets/maledoctor.png" width="150" height="150">
        </div>
        <div class="doctor-info">
          <p style="color: #2E3842;font-size: 20px;font-weight: 500;">Fatma Gül</p>
          <p style="font-size: 14px;color: #757575;margin-bottom: 5px;">Dahiliye</p>
          <div class="doctor-rank" style="margin: 0 0 7px 0">
                <div class="star">
                    <span class="material-icons" >star</span ><span class="material-icons" >star</span ><span class="material-icons" >star</span ><span class="material-icons" >star</span ><span class="material-icons" >star</span ><p class="after">4.7</p><p style="height: 22px;">154 Değerlendirme</p>
                </div>
          </div>
          <div class="doctor-departmant">
              <span class="material-icons" style="color: rgb(2550, 0, 0, 0.300); font-size: 24px;padding: 1px; margin-right: 2px;">emergency</span><p style="padding-top: 3.5px;">Şevket Yılmaz Devlet Hastanesi</p>
          </div>
          <div class="make-appointment">
            <router-link to="/randevu" class="appointment"><p>Randevu Al</p></router-link>
          </div>
        </div>
    </div>
    </template>
  </div>
</template>

<script>

export default {
  name: 'ShowDoctors',
  data () {
    return {
      doctors: ['Ahmet Furkan ÇELİK', 'Mehmet Akif ÇELİKTÜRK', 'Fatma ARICI', 'Enes DEMİR']
    }
  }
}
</script>
