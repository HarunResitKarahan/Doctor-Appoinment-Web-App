<template>
  <div class="home">
    <Navbar />
    <SlideArea />
    <Clinic />
  </div>
</template>

<script>
import Navbar from "@/components/Homepage/Navbar.vue";
import SlideArea from "@/components/Homepage/SlideArea.vue";
import Clinic from "@/components/Homepage/Clinics.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    SlideArea,
    Clinic,
  },
  mounted() {  
    document.title = "Ana Sayfa";  
  },
};
</script>
