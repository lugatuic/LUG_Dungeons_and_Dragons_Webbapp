import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import misha from '@/views/misha.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path:'/Home_page',
      name:'Home_page',
      component: Home_page
    },
    {
      path:'/Char_input',
      name:'Char_input',
      component: Char_input
    },
    {
      path:'/Output_page',
      name:'Output_page',
      component: Output_page
    }

  ]
})
