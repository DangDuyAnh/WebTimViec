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
import MyCV from './MyCV.vue'
import TimViecLam from './TimViecLam.vue'
import PhienDichVien from './PhienDichVien.vue'
import NhanVienKho from './NhanVienKho.vue'
import ViecDaLuu from './ViecDaLuu.vue'
import ViecDaUngTuyen from './ViecDaUngTuyen.vue'

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
    component: MyCV,
  },
  {
    path: '/tim-viec-lam',
    component: TimViecLam
  },
  {
    path: '/tim-viec-lam/phien-dich-vien',
    component: PhienDichVien
  },
  {
    path: '/tim-viec-lam/nhan-vien-kho',
    component: NhanVienKho
  },
  {
    path: '/viec-da-luu',
    component: ViecDaLuu
  },
  {
    path: '/viec-da-ung-tuyen',
    component: ViecDaUngTuyen
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