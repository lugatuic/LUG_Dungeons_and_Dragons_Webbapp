import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Char_input from './views/Char_input.vue'
import Char_ouput from './views/Char_ouput.vue'


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
      path:'/',
      name:'Home',
      component: Home
    },
    {
      path:'/char_input',
      name:'Char_input',
      component: Char_input
    },
    {
      path:'/char_ouput',
      name:'Char_output',
      component: Char_ouput
    }

  ]
})
