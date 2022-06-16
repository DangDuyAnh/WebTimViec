import { createWebHistory, createRouter } from "vue-router";
import TrangChu from "./TrangChu/TrangChu.vue";
import ViecLam from "./ViecLam.vue";
import Admin from './Admin/Admin.vue';
import CreateRecruit from './Admin/CreateRecruit.vue';
import DetailRecruit from './Admin/DetailRecruit.vue';
import Login from "./Taikhoan/Login.vue";
import Register from "./Taikhoan/Register.vue";

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
  },
  {
    path: '/admin/detail-recruit',
    component: DetailRecruit
  },
  {
    path: "/dang-nhap",
    component: Login,
  },
  {
    path: "/dang-ky",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


export default router;