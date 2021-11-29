import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "@/css/Home_css/navbar.css";
import "@/css/Home_css/slide-area.css";
import "@/css/Home_css/clinic.css";

import "@/scripts/Home_js/clinic.js";
createApp(App).use(store).use(router).mount("#app");
