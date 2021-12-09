<template>
  <div class="profile-component">
      <div class="profile-info col-3">
        <div class="card-body">
          <img src="@/assets/femalephoto.png" width="150" height="150">
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
      <div class="booking-history col-9">
        <div style="padding: 20px;
                    border: 0 solid #f0f0f0;
                    border-bottom-width: 1px;
                    width: 100%;
                    text-align: center;
                    height: fit-content;">
          <p style="font-weight: 500;letter-spacing: 1.8px;">Randevu Geçmişi</p>
        </div>
        <table style="width: 100%;">
          <tr>
            <th>Doktor</th>
            <th>Bölüm</th>
            <th>Randevu Tarihi</th>
            <th>Hastane</th>
          </tr>
          <tr>
            <td><div style="display: flex;
                        align-items: center;
                        width: 100%;">
              <div>
                <img src="@/assets/maledoctor.png" width="55" height="55" style="border-radius: 100%;">
              </div>
              <div>
                <p style="margin-left: 16px;font-weight: 500;font-size: 0.9rem;">Enes Demir</p>
              </div>
            </div></td>
            <td><div>Cildiye</div></td>
            <td><div>9 Aralık 2021 10:30</div> </td>
            <td><div>Şevket Yılmaz Devlet Hastanesi</div></td>
          </tr>
          <tr>
            <td><div style="display: flex;
                        align-items: center;
                        width: 100%;">
              <div>
                <img src="@/assets/femaledoctor.png" width="55" height="55" style="border-radius: 100%;">
              </div>
              <div>
                <p style="margin-left: 16px;font-weight: 500;font-size: 0.9rem;">Fatma Aksu</p>
              </div>
            </div></td>
            <td><div>Dahiliye</div></td>
            <td><div>9 Aralık 2021 10:30</div> </td>
            <td><div>Şevket Yılmaz Devlet Hastanesi</div></td>
          </tr>
          <tr>
            <td><div style="display: flex;
                        align-items: center;
                        width: 100%;">
              <div>
                <img src="@/assets/maledoctor.png" width="55" height="55" style="border-radius: 100%;">
              </div>
              <div>
                <p style="margin-left: 16px;font-weight: 500;font-size: 0.9rem;">Mehmet Akif Çeliktürk</p>
              </div>
            </div></td>
            <td><div>Göz Hastalıkları</div></td>
            <td><div>9 Aralık 2021 10:30</div> </td>
            <td><div>Şevket Yılmaz Devlet Hastanesi</div></td>
          </tr>
        </table>
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
