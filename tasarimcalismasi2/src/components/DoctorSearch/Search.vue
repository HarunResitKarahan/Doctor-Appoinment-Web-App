<template>
  <div class="search-content">
    <div class="search col-3">
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
            </div>
              <input v-model="date" type="date" id="date">
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
    <ShowDoctors :doctor="doctor" :department="department" :hospitalName="hospitalName"/>
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
      date: '',
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
    document.getElementById('date').valueAsDate = new Date()
    if (this.location !== undefined) {
      fetch('http://localhost:8000/hospital/gethospital', {
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
      } else if (event.target.checked === true && this.location !== undefined && this.gender !== undefined && this.department !== undefined && this.hospitalName !== undefined) {
        fetch('http://localhost:8000/doctor/getdoctor', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            departmanName: this.department,
            cityName: this.location,
            doctorSex: this.gender,
            hospitalName: this.hospitalName
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
        fetch('http://localhost:8000/hospital/gethospital', {
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
        this.location = undefined
      } else if (prop === 'hospital') {
        this.hospitalName = undefined
      } else if (prop === 'gender') {
        this.gender = undefined
      } else {
        this.department = undefined
      }
      var checkboxes = document.getElementsByClassName('checkbox')
      checkboxes.forEach((item) => {
        if (event.target.parentElement.lastChild.textContent === item.lastChild.textContent) item.firstChild.checked = false
      })
    }
  }
}
</script>
