<template>
  <div class="search col-3">
    <div class="filter-search">
        <h5>Filtreli Arama</h5>
        <div class="card-body">
          <div class="selected-options">
            <template v-if="location != undefined">
              <div class="cards"><span @click="hide($event, 'location')" class="material-icons" style="font-size: 14px;border: 1px solid white;cursor: pointer;border-radius: 100%;margin-right: 5px;">close</span><p>{{location}}</p></div>
            </template>
            <template v-if="gender != undefined">
              <div class="cards"><span @click="hide($event, 'gender')" class="material-icons" style="font-size: 14px;border: 1px solid white;cursor: pointer;border-radius: 100%;margin-right: 5px;">close</span><p>{{gender}}</p></div>
            </template>
            <template v-if="department != undefined">
            <div class="cards"><span @click="hide($event, 'department')" class="material-icons" style="font-size: 14px;border: 1px solid white;cursor: pointer;border-radius: 100%;margin-right: 5px;">close</span><p>{{department}}</p></div>
            </template>
          </div>
            <input type="date" id="date">
              <h6 style="font-size: 15px;margin-top: 20px;">Şehir</h6>
            <div style="height: 150px;overflow: auto;">
              <template v-for="(item,index) in city">
                <label class="checkbox" :key="index">
                      <input @click="onlyOneForLocation($event)" type="checkbox" name="checklocation" :checked="location == item.cityName ? 'checked' : false"><p style="text-align: left;">{{item.cityName}}</p>
                </label>
              </template>
            </div>
            <div>
              <h6 style="font-size: 15px;margin-top: 20px;">Cinsiyet</h6>
              <label class="checkbox">
                    <input @click="onlyOneForgender($event)" type="checkbox" name="checkgender" :checked="gender == 'Erkek' ? 'checked' : false"><p style="text-align: left;">Erkek</p>
              </label>
              <label class="checkbox">
                    <input @click="onlyOneForgender($event)" type="checkbox" name="checkgender" :checked="gender == 'Kadın' ? 'checked' : false"><p style="text-align: left;">Kadın</p>
              </label>
            </div>
            <div>
              <h6 style="font-size: 15px;margin-top: 20px;">Poliklinik</h6>
              <template v-for="(item,index) in policlinics">
                <label class="checkbox" :key="index">
                  <input @click="onlyOneForClinics($event)" type="checkbox" name="checkclinics" :checked="department == item.departmanName ? 'checked' : false"><p style="text-align: left;">{{item.departmanName}}</p>
                </label>
              </template>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
// import $ from 'jquery'
export default {
  name: 'Search',
  props: {
    department: String,
    location: String,
    gender: String
  },
  data () {
    return {
      policlinics: [],
      city: []
    }
  },
  created () {
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
  },
  methods: {
    onlyOneForLocation (event) {
      this.location = event.target.parentElement.lastChild.textContent
      var checkboxgender = document.getElementsByName('checklocation')
      checkboxgender.forEach((item) => {
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
    hide (event, prop) {
      if (prop === 'location') {
        this.location = undefined
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
