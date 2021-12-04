<template>
  <div class="booking-tab">
    <div class="doctor-info-tab">
        <div class="doctor-image">
            <img src="@/assets/doctor11.jpg" width="80" height="80">
        </div>
        <div class="doctor-info">
            <div class="doctor-name">
                Enes DEMİR
            </div>
            <div class="doctor-rank">
                .
            </div>
            <div class="doctor-departmant">
                .
            </div>
        </div>
    </div>
    <div class="schedule-tab">

    </div>
  </div>
</template>

<script>

export default {
  name: 'BookingTab',
  mounted () {
    document.title = 'Randevu Al'
  }
}
</script>
