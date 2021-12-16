<template>
  <div class="sub-navbar">
    <p><router-link to="/" style="color: white;font-weight: 400;">Anasayfa</router-link> > {{title}}</p>
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
