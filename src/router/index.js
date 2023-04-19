import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddRegistry from '../views/RegisterView.vue'
import LoginForms from '../views/LoginView.vue'
import NewPost from '../views/CreatePosts.vue'
import Explore from '../views/ExploreView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: AddRegistry
    },
    {
      path: '/login',
      name: 'login',
      component: LoginForms
    },
    {
      path: '/posts/new',
      name: 'new post',
      component: NewPost
    },
    {
      path: '/explore',
      name: 'explore',
      component: Explore
    }
  ]
})

export default router
