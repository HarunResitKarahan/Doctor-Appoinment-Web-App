<template>
  <div class="home">
    <Navbar />
    <SlideArea />
  </div>
</template>

<script>
import Navbar from "@/components/Homepage/Navbar.vue";
import SlideArea from "@/components/Homepage/SlideArea.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    SlideArea,
  },
};
</script>
