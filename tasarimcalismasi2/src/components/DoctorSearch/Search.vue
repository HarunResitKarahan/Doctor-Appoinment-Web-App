<template>
  <div class="search col-3">
    <div class="filter-search">
        <h5>Filtreli Arama</h5>
        <div class="card-body">
            <input type="date" id="date">
            <h6 style="font-size: 15px;margin-top: 20px;">Cinsiyet</h6>
            <label class="checkbox">
                  <input type="checkbox" :checked="sex == 'Erkek' ? 'checked' : ''"><p style="text-align: left;">Erkek</p>
            </label>
            <label class="checkbox">
                  <input type="checkbox" :checked="sex == 'Kadın' ? 'checked' : ''"><p style="text-align: left;">Kadın</p>
            </label>
            <h6 style="font-size: 15px;margin-top: 20px;">Poliklinik</h6>
            <template v-for="item in policlinics">
              <label class="checkbox" :key="item">
                <input type="checkbox" :checked="department == item.departmanName ? 'checked' : ''"><p style="text-align: left;">{{item.departmanName}}</p>
              </label>
            </template>
        </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Search',
  props: {
    department: String,
    location: String,
    sex: String
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
    $(document).ready(function () {
      $('label.checkbox').on('click', function () {
        $('label .checkbox input[type="checkbox"]').not(this).prop('checked', false)
      })
    })
  }
}
</script>
