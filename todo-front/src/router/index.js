import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '@/views/Login'  // @ -> src폴더, vue 안써도 괜찮

Vue.use(VueRouter)

const routes = [
  // 하나의 큰 페이지 단위의 component -> views 안에 있는 component
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
