import { createWebHistory, createRouter } from "vue-router";
import TrangChu from "./TrangChu/TrangChu.vue";
import Admin from './Admin/Admin.vue';
import Admin2 from './Admin/Admin2.vue';
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
import TimViecLam from './TimViecLam.vue'
import TimViecLamFilter from './TimViecLamFilter.vue'
import TimViecLamDetail from './TimViecLamDetail.vue'
import ViecDaLuu from './ViecDaLuu.vue'
import ViecDaUngTuyen from './ViecDaUngTuyen.vue'
import GoiY from './GoiY.vue'
import TimViecLam2 from './TimViecLam2.vue'
import ThongTinCaNhan from './Info.vue'
import { authenticationService } from '../utility/authenticationService'

const routes = [
  {
    path: "/",
    component: TrangChu,
  },
  {
    path: '/admin',
    component: Admin,
    name: '/admin'
  },
  {
    path: '/admin/da-tuyen-dung',
    component: Admin2,
    name: '/admin/da-tuyen-dung'
  },
  {
    path: '/admin/create-recruit',
    component: CreateRecruit,
    name: '/admin/create-recruit'
  },
  {
    path: '/admin/detail-recruit/:id',
    component: DetailRecruit,
    name: '/admin/detail-recruit'
  },
  {
    path: '/admin/chat',
    component: Chat,
    name: '/admin/chat'
  },
  {
    path: "/dang-nhap",
    component: Login,
    name: '/dang-nhap'
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
    name: '/admin/cong-ty'
  },
  {
    path: '/my-cv',
    component: MyCV,
    name: '/my-cv'
  },
  {
    path: '/tim-viec-lam',
    component: TimViecLam
  },
  {
    path: '/tim-viec-lam-moi-nhat',
    component: TimViecLam2
  },
  {
    path: '/tim-viec-lam-filter',
    component: TimViecLamFilter
  },
  {
    path: '/tim-viec-lam/detail/:id',
    component: TimViecLamDetail
  },
  {
    path: '/viec-da-luu',
    component: ViecDaLuu,
    name: '/viec-da-luu'
  },
  {
    path: '/viec-da-ung-tuyen',
    component: ViecDaUngTuyen,
    name: '/viec-da-ung-tuyen'
  },
  {
    path: '/my-letter',
    component: MyLetter,
    name: '/my-letter'
  },
  {
    path: '/cong-ty',
    component: CongTy2
  },
  {
    path: '/viec-lam-cong-ty/:id',
    component: ViecLamCongTy
  },
  {
    path: '/chat',
    component: ChatEmployee,
    name: '/chat'
  },
  {
    path: '/goi-y',
    component: GoiY,
    name: '/goi-y'
  },
  {
    path: '/thong-tin-ca-nhan',
    component: ThongTinCaNhan,
    name: '/thong-tin-ca-nhan'
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from) => {
  const userRoutes = ['/my-cv', '/viec-da-luu', '/viec-da-ung-tuyen', '/my-letter', '/chat']
  const adminRoutes = ['/admin/cong-ty', '/admin', '/admin/da-tuyen-dung', '/admin/create-recruit', '/admin/detail-recruit', '/admin/chat']
  if (
    (authenticationService.getUserToken() === undefined || authenticationService.getUserToken() === null) && (to.name !== 'dang-nhap') 
    && userRoutes.includes(to.name)
  ) {
    return { name: '/dang-nhap' }
  }

  if (
    (authenticationService.getAdminToken() === undefined || authenticationService.getAdminToken() === null) && (to.name !== 'dang-nhap') 
    && adminRoutes.includes(to.name)
  ) {
    return { name: '/dang-nhap' }
  }
})

export default router;