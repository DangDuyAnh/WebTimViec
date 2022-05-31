import { createWebHistory, createRouter } from "vue-router";
import TrangChu from "./TrangChu/TrangChu.vue";
import ViecLam from "./ViecLam.vue";
import Login from "./Taikhoan/Login.vue";
import Register from "./Taikhoan/Register.vue";



const routes = [
  {
    path: "/trang-chu",
    component: TrangChu,
  },
  {
    path: "/viec-lam",
    component: ViecLam,
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