import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import DoctorSearch from '../views/DoctorSearch.vue'
import Profile from '../views/Profile.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/doktor-ara',
    name: 'DoctorSearch',
    component: DoctorSearch
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/randevu',
    name: 'Booking',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Booking.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
