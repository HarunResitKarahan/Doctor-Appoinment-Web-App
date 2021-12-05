<template>
  <div class="sub-navbar">
    <p>Anasayfa > {{title}}</p>
  </div>
</template>

<script>

export default {
  name: 'SubNavbar',
  props: {
    title: String
  }
}
</script>
