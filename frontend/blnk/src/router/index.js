import { createRouter, createWebHistory } from 'vue-router';

// Import your components here
import HelloWorld from '@/components/HelloWorld.vue';
import Login from '@/components/Login.vue';

const routes = [
    { path: '/', name: "home", component: HelloWorld },
    { path: '/login', name: "login", component: Login }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
