<template>
  <div class="search-content">
    <div class="search col-xl-3 col-lg-4 col-md-5">
      <div class="filter-search">
          <h5>Filtreli Arama</h5>
          <div class="card-body">
            <div class="selected-options">
              <!-- flex 60% -->
              <template v-if="location != undefined">
                <div class="cards"><span @click="hide($event, 'location')" class="material-icons" style="font-size: 14px;border: 1px solid white;cursor: pointer;border-radius: 100%;margin-right: 5px;">close</span><p>{{location}}</p></div>
              </template>
              <template v-if="hospitalName != undefined">
                <div class="cards"><span @click="hide($event, 'hospital')" class="material-icons" style="font-size: 14px;border: 1px solid white;cursor: pointer;border-radius: 100%;margin-right: 5px;">close</span><p>{{hospitalName}}</p></div>
              </template>
              <template v-if="gender != undefined">
                <div class="cards"><span @click="hide($event, 'gender')" class="material-icons" style="font-size: 14px;border: 1px solid white;cursor: pointer;border-radius: 100%;margin-right: 5px;">close</span><p>{{gender}}</p></div>
              </template>
              <template v-if="department != undefined">
              <div class="cards"><span @click="hide($event, 'department')" class="material-icons" style="font-size: 14px;border: 1px solid white;cursor: pointer;border-radius: 100%;margin-right: 5px;">close</span><p>{{department}}</p></div>
              </template>
              <template v-if="date != undefined">
              <div class="cards"><span @click="hide($event, 'date')" class="material-icons" style="font-size: 14px;border: 1px solid white;cursor: pointer;border-radius: 100%;margin-right: 5px;">close</span><p>{{datereverse}}</p></div>
              </template>
            </div>
              <input @change="datechange" v-model="date" type="date" id="date">
                <h6 style="font-size: 15px;margin-top: 20px;">Şehir</h6>
              <div style="height: 150px;overflow: auto;">
                <template v-for="(item,index) in city">
                  <label class="checkbox" :key="index">
                        <input @click="onlyOneForLocation($event)" @change="change($event)" type="checkbox" name="checklocation" :checked="location == item.cityName ? 'checked' : false"><p style="text-align: left;">{{item.cityName}}</p>
                  </label>
                </template>
              </div>
              <template v-if="hospital.length > 0">
              <h6 style="font-size: 15px;margin-top: 20px;">Hastane</h6>
              <div style="height: 150px;overflow: auto;">
                <template v-for="(item,index) in hospital">
                  <label class="checkbox" :key="index">
                        <input @click="onlyOneForHospital($event)" @change="change($event)" type="checkbox" name="checkhospital" :checked="hospitalName == item.hospitalName ? 'checked' : false"><p style="text-align: left;">{{item.hospitalName}}</p>
                  </label>
                </template>
              </div>
              </template>
              <div>
                <h6 style="font-size: 15px;margin-top: 20px;">Cinsiyet</h6>
                <label class="checkbox">
                      <input @click="onlyOneForgender($event)" @change="change($event)" type="checkbox" name="checkgender" :checked="gender == 'Farketmez' ? 'checked' : false"><p style="text-align: left;">Farketmez</p>
                </label>
                <label class="checkbox">
                      <input @click="onlyOneForgender($event)" @change="change($event)" type="checkbox" name="checkgender" :checked="gender == 'Erkek' ? 'checked' : false"><p style="text-align: left;">Erkek</p>
                </label>
                <label class="checkbox">
                      <input @click="onlyOneForgender($event)" @change="change($event)" type="checkbox" name="checkgender" :checked="gender == 'Kadın' ? 'checked' : false"><p style="text-align: left;">Kadın</p>
                </label>
              </div>
                <h6 style="font-size: 15px;margin-top: 20px;">Poliklinik</h6>
              <div style="height: 500px;overflow: auto;">
                <template v-for="(item,index) in policlinics">
                  <label class="checkbox" :key="index">
                    <input @click="onlyOneForClinics($event)" @change="change($event)" type="checkbox" name="checkclinics" :checked="department == item.departmanName ? 'checked' : false"><p style="text-align: left;">{{item.departmanName}}</p>
                  </label>
                </template>
              </div>
          </div>
      </div>
    </div>
    <ShowDoctors :doctor="doctor" :department="department" :hospitalName="hospitalName" :date="date" :location="location"/>
  </div>
</template>

<script>
// import $ from 'jquery'
import ShowDoctors from '@/components/DoctorSearch/ShowDoctors.vue'

export default {
  name: 'Search',
  components: {
    ShowDoctors
  },
  props: {
    department: String,
    location: String,
    gender: String
  },
  data () {
    return {
      policlinics: [],
      city: [],
      doctor: [],
      hospital: [],
      date: undefined,
      datereverse: '',
      // department: '',
      // location: '',
      // gender: '',
      hospitalName: undefined
    }
  },
  created () {
    // this.doctor = this.Doctor
    // this.location = this.Location
    // this.gender = this.Gender
    fetch('http://localhost:8000/department/getclinics', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        this.policlinics = data
      })
    fetch('http://localhost:8000/city/getcitys', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        this.city = data
      })
  },
  mounted () {
    var today = new Date()
    today.setDate(today.getDate() + 1)
    var dd = today.getDate()
    var mm1 = today.getMonth() + 1
    var yyyy1 = today.getFullYear()
    today.setDate(today.getDate() + 14)
    var dd2 = today.getDate()
    var mm = today.getMonth() + 1
    var yyyy = today.getFullYear()
    if (dd < 10) {
      dd = '0' + dd
    }
    if (dd2 < 10) {
      dd2 = '0' + dd2
    }
    if (mm < 10) {
      mm = '0' + mm
    }
    if (mm1 < 10) {
      mm1 = '0' + mm1
    }
    today = yyyy1 + '-' + mm1 + '-' + dd
    var today2 = yyyy + '-' + mm + '-' + dd2
    document.getElementById('date').setAttribute('min', today)
    document.getElementById('date').setAttribute('max', today2)
    if (this.location !== undefined) {
      fetch('http://127.0.0.1:8000/hospital/gethospital', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          cityName: this.location
        })
      })
        .then(response => response.json())
        .then(data => {
          this.hospital = data
        })
    }
  },
  methods: {
    onlyOneForLocation (event) {
      this.location = event.target.parentElement.lastChild.textContent
      var checkboxgender = document.getElementsByName('checklocation')
      checkboxgender.forEach((item) => {
        if (item !== event.target) item.checked = false
      })
    },
    onlyOneForHospital (event) {
      this.hospitalName = event.target.parentElement.lastChild.textContent
      var checkboxes = document.getElementsByName('checkhospital')
      checkboxes.forEach((item) => {
        if (item !== event.target) item.checked = false
      })
    },
    onlyOneForgender: function (event) {
      this.gender = event.target.parentElement.lastChild.textContent
      var checkboxgender = document.getElementsByName('checkgender')
      checkboxgender.forEach((item) => {
        if (item !== event.target) item.checked = false
      })
    },
    onlyOneForClinics (event) {
      this.department = event.target.parentElement.lastChild.textContent
      var checkboxes = document.getElementsByName('checkclinics')
      checkboxes.forEach((item) => {
        if (item !== event.target) item.checked = false
      })
    },
    datechange () {
      this.datereverse = String(this.date).split('-').reverse().join('/')
      if (this.location !== undefined && this.gender !== undefined && this.department !== undefined && this.hospitalName !== undefined && this.date !== undefined) {
        fetch('http://127.0.0.1:8000/doctor/getdoctor', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            departmanName: this.department,
            cityName: this.location,
            doctorSex: this.gender,
            hospitalName: this.hospitalName,
            appointmentTime: this.date
          })
        })
          .then(response => response.json())
          .then(data => {
            this.doctor = data
          })
      }
    },
    change (event) {
      if (event.target.checked === false) {
        if (event.target.attributes.name.textContent === 'checkclinics') {
          this.department = undefined
          this.doctor = []
        } else if (event.target.attributes.name.textContent === 'checkgender') {
          this.gender = undefined
          this.doctor = []
        } else if (event.target.attributes.name.textContent === 'checkhospital') {
          this.hospitalName = undefined
          this.doctor = []
        } else if (event.target.attributes.name.textContent === 'checklocation') {
          this.location = undefined
          this.doctor = []
          this.hospitalName = undefined
          this.hospital = []
        }
      } else if (event.target.checked === true && this.location !== undefined && this.gender !== undefined && this.department !== undefined && this.hospitalName !== undefined && this.date !== undefined) {
        fetch('http://127.0.0.1:8000/doctor/getdoctor', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            departmanName: this.department,
            cityName: this.location,
            doctorSex: this.gender,
            hospitalName: this.hospitalName,
            appointmentTime: this.date
          })
        })
          .then(response => response.json())
          .then(data => {
            this.doctor = data
          })
      }
      if (event.target.checked === true && event.target.attributes.name.textContent === 'checklocation') {
        this.hospitalName = undefined
        this.doctor = []
        fetch('http://127.0.0.1:8000/hospital/gethospital', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            cityName: this.location
          })
        })
          .then(response => response.json())
          .then(data => {
            this.hospital = data
          })
      }
    },
    hide (event, prop) {
      if (prop === 'location') {
        this.hospital = []
        this.hospitalName = undefined
        this.doctor = []
        this.location = undefined
      } else if (prop === 'hospital') {
        this.hospitalName = undefined
        this.doctor = []
      } else if (prop === 'gender') {
        this.gender = undefined
        this.doctor = []
      } else if (prop === 'date') {
        this.date = undefined
        this.doctor = []
      } else {
        this.department = undefined
        this.doctor = []
      }
      var checkboxes = document.getElementsByClassName('checkbox')
      checkboxes.forEach((item) => {
        if (event.target.parentElement.lastChild.textContent === item.lastChild.textContent) item.firstChild.checked = false
      })
    }
  }
}
</script>
