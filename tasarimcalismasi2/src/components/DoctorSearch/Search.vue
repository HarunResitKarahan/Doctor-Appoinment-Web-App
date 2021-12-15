<template>
  <div class="search col-3">
    <div class="filter-search">
        <h5>Filtreli Arama</h5>
        <div class="card-body">
            <input type="date" id="date">
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
      policlinics: []
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
  },
  mounted () {
    document.getElementById('date').valueAsDate = new Date()
  },
  methods: {
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
