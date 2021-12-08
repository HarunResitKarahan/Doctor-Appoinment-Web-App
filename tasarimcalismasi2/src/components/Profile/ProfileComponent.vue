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
                    padding: 15px; ">
            <p class="h6" style="margin:0;margin-bottom: 5px;">Son Randevular</p>
            <div style="display: flex;
                        width: 100%;
                        padding: 20px 5px;
                        border: 0 solid #f0f0f0;
                        border-top-width: 1px;
                        border-bottom-width: 1px;">
              <div>
                <img src="@/assets/maledoctor.png" width="55" height="55" style="border-radius: 100%;">
              </div>
              <div>
                <p style="margin-left: 8px;font-weight: 500;font-size: 0.9rem;">Enes Demir</p>
                <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">(Dahiliye)</p>
                <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">9 Aralık 2021 10:30</p>
              </div>
            </div>
            <div style="display: flex;
                        width: 100%;
                        padding: 20px 5px;
                        border: 0 solid #f0f0f0;
                        border-top-width: 1px;
                        border-bottom-width: 1px;">
              <div>
                <img src="@/assets/femaledoctor.png" width="55" height="55" style="border-radius: 100%;">
              </div>
              <div>
                <p style="margin-left: 8px;font-weight: 500;font-size: 0.9rem;">Fatma Aksu</p>
                <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">(Cildiye)</p>
                <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">9 Aralık 2021 10:30</p>
              </div>
            </div>
            <div style="display: flex;
                        width: 100%;
                        padding: 20px 5px;
                        border: 0 solid #f0f0f0;
                        border-top-width: 1px;
                        border-bottom-width: 1px;">
              <div>
                <img src="@/assets/maledoctor.png" width="55" height="55" style="border-radius: 100%;">
              </div>
              <div>
                <p style="margin-left: 8px;font-weight: 500;font-size: 0.9rem;">Mehmet Akif Çeliktürk</p>
                <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">(Göz Hastalıkları)</p>
                <p style="margin-left: 8px;font-weight: 300;font-size: 0.8rem;">9 Aralık 2021 10:30</p>
              </div>
            </div>
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
