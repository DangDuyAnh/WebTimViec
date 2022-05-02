import { createWebHistory, createRouter } from "vue-router";
import TrangChu from "./TrangChu/TrangChu.vue";
import ViecLam from "./ViecLam.vue";

const routes = [
  {
    path: "/",
    component: TrangChu,
  },
  {
    path: "/viec-lam",
    component: ViecLam,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;