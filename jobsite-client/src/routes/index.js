import { createWebHistory, createRouter } from "vue-router";
import TrangChu from "./TrangChu/TrangChu.vue";
import ViecLam from "./ViecLam.vue";
import Admin from './Admin/Admin.vue';
import CreateRecruit from './Admin/CreateRecruit.vue';

const routes = [
  {
    path: "/",
    component: TrangChu,
  },
  {
    path: "/viec-lam",
    component: ViecLam,
  },
  {
    path: '/admin',
    component: Admin,
  },
  {
    path: '/admin/create-recruit',
    component: CreateRecruit
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;