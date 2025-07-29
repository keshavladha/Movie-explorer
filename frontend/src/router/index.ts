import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import MovieDetail from '@/views/MovieDetail.vue'
import ActorProfile from '@/views/ActorProfile.vue'
import DirectorProfile from '@/views/DirectorProfile.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/movie/:id',
      name: 'MovieDetail',
      component: MovieDetail,
      props: true
    },
    {
      path: '/actor/:id',
      name: 'ActorProfile',
      component: ActorProfile,
      props: true
    },
    {
      path: '/director/:id',
      name: 'DirectorProfile',
      component: DirectorProfile,
      props: true
    }
  ]
})

export default router 