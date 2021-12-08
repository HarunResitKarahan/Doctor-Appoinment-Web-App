<template>
  <div class="profile-component">
      <div class="profile-info col-4">
        <div class="card-body">
          <img src="@/assets/malephoto.png" width="150" height="150">
          <p style="font-weight: 500;">Harun Reşit KARAHAN</p>
          <p style="color: #757575;
                    font-size: 13px;
                    font-weight: normal;
                    margin-top: 8px;
                    margin-bottom: 8px;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    white-space: nowrap;"
                    ><b>TC Kimlik No:</b> 38887030636 </p>
        <div style="text-align: left;
                    width: 100%;
                    margin-top:30px;
                    border: 0 solid #f0f0f0;
                    border-bottom-width: 1px;
                    padding: 15px; ">
            <p class="h6" style="margin:0">Son Randevular</p>
        </div>
        </div>
      </div>
      <div class="booking-history col-8">
        asd
      </div>
  </div>
</template>

<script>
// import $ from 'jquery'
export default {
  name: 'ProfileComponent',
  data () {
    return {
      issignin: '',
      isregistered: ''
    }
  },
  created () {
    this.localusername = localStorage.username
    this.issignin = localStorage.issignin
  }
}
</script>
