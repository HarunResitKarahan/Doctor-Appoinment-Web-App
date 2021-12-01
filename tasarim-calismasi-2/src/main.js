import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "@/css/Home_css/navbar.css";
import "@/css/Home_css/slide-area.css";
import "@/css/Home_css/clinic.css";
import "@/css/Home_css/footer.css";

import "@/scripts/Home_js/clinic.js";

import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
createApp(App).use(store).use(router).mount("#app");
