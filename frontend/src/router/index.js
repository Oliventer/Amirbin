import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
      path: '/note',
      name: 'Note',
      props: true,
      component: () => import(/* webpackChunkName: "about" */ '../views/Note.vue'),
  },
  {
    path: '/note/:pk',
    name: 'Snippet',
    props: true,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Snippets.vue'),
  },
  {
    path: '/paste',
    name: 'Paste',
    component: () => import('../views/Paste.vue'),  
  },
  {
    path: '/subscribe',
    name: 'Subscribe',
    component: () => import('../views/Subscribe.vue'),
  },
  {
    path: '/success',
    name: 'SuccessPage',
    component: () => import('../components/SuccessPage.vue'),
  },
  {
    path: '/cancel',
    name: 'CancelPage',
    component: () => import('../components/CancelPage.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to) {
      if (to.hash) {
        let hashNum = parseInt(to.hash.split('#').pop()) - 5
        if (hashNum>0) {
            return {selector: `#${hashNum}`}
        }
        return {selector: '#1'}
        
      }
      
  }
})

export default router
