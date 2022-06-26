import { createWebHistory, createRouter } from "vue-router";
import TrangChu from "./TrangChu/TrangChu.vue";
import ViecLam from "./ViecLam.vue";
import Admin from './Admin/Admin.vue';
import CreateRecruit from './Admin/CreateRecruit.vue';
import DetailRecruit from './Admin/DetailRecruit.vue';
import Login from "./Taikhoan/Login.vue";
import Register from "./Taikhoan/Register.vue";
import Chat from "./Admin/Chat.vue";
import AdminRegister from "./Admin/AdminRegister.vue";
import CongTy from "./Admin/CongTy.vue";
import MyCV from './MyCV.vue';
import MyLetter from './MyLetter.vue';
import CongTy2 from './CongTy.vue'
import ViecLamCongTy from './ViecLamCongTy.vue';
import ChatEmployee from './Chat.vue'
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
    path: '/admin/chat',
    component: Chat
  },
  {
    path: "/dang-nhap",
    component: Login,
  },
  {
    path: "/dang-ky",
    component: Register,
  },
  {
    path: "/dang-ky-admin",
    component: AdminRegister,
  },
  {
    path: "/admin/cong-ty",
    component: CongTy,
  },
  {
    path: '/my-cv',
    component: MyCV
  },
  {
    path: '/my-letter',
    component: MyLetter
  },
  {
    path: '/cong-ty',
    component: CongTy2
  },
  {
    path: '/viec-lam-cong-ty',
    component: ViecLamCongTy
  },
  {
    path: '/chat',
    component: ChatEmployee
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


export default router;