import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "@/css/Home_css/navbar.css";
import "@/css/Home_css/slide-area.css";

createApp(App).use(store).use(router).mount("#app");
