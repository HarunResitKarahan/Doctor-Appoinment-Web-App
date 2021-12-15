<template>
  <div class="search col-3">
    <div class="filter-search">
        <h5>Filtreli Arama</h5>
        <div class="card-body">
          <div class="selected-options">
            <div class="cards"><span class="material-icons" style="font-size: 14px;border: 1px solid white;cursor: pointer;border-radius: 100%;margin-right: 5px;">close</span><p>{{location}}</p></div>
          </div>
            <input type="date" id="date">
              <h6 style="font-size: 15px;margin-top: 20px;">Şehir</h6>
            <div style="height: 150px;overflow: auto;">
              <template v-for="item in city">
                <label class="checkbox" :key="item">
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
              <template v-for="item in policlinics">
                <label class="checkbox" :key="item">
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
      // this.location = event.target.lastChild.textContent
      // var checkboxes = document.getElementsByName('checklocation')
      // console.log(checkboxes[0].firstChild)
      // console.log(checkboxes[0].lastChild)
      // console.log(event.target)
      // console.log('------------------------------------------')
      // checkboxes.forEach((item) => {
      //   if (item === event.target || item.firstChild === event.target || item.lastChild === event.target) {
      //     item.firstChild.checked = true
      //   } else {
      //     item.firstChild.checked = false
      //   }
      // })
    },
    onlyOneForgender: function (event) {
      var checkboxgender = document.getElementsByName('checkgender')
      checkboxgender.forEach((item) => {
        if (item !== event.target) item.checked = false
      })
    },
    onlyOneForClinics (event) {
      var checkboxes = document.getElementsByName('checkclinics')
      checkboxes.forEach((item) => {
        if (item !== event.target) item.checked = false
      })
    }
  }
}
</script>
