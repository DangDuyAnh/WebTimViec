<template>
        <div id="main-wrapper" data-layout="vertical" data-navbarbg="skin5" data-sidebartype="full"
        data-sidebar-position="absolute" data-header-position="absolute" data-boxed-layout="full">
        <!-- ============================================================== -->
        <!-- Topbar header - style you can find in pages.scss -->
        <!-- ============================================================== -->
        <header class="topbar" data-navbarbg="skin5">
            <nav class="navbar top-navbar navbar-expand-md navbar-dark">
                <div class="navbar-header" data-logobg="skin6">
                    <!-- ============================================================== -->
                    <!-- Logo -->
                    <!-- ============================================================== -->
                    <div class="navbar-brand admin-out-text" href="dashboard.html">

                        <!-- <b class="logo-icon">

                            <img src="./plugins/images/logo-icon.png" alt="homepage" />
                        </b>

                        <span class="logo-text"> 
                            <img src="./plugins/images/logo-text.png" alt="homepage" />
                        </span> -->
                        <span class="logo-text logo-admin"> 
                            JOB SITE
                        </span> 
                    </div>
                    <!-- ============================================================== -->
                    <!-- End Logo -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- toggle and nav items -->
                    <!-- ============================================================== -->
                    <a class="nav-toggler waves-effect waves-light text-dark d-block d-md-none"
                        href="javascript:void(0)"><i class="ti-menu ti-close"></i></a>
                </div>
                <!-- ============================================================== -->
                <!-- End Logo -->
                <!-- ============================================================== -->
                <div class="navbar-collapse collapse" id="navbarSupportedContent" data-navbarbg="skin5">
                    <ul class="navbar-nav d-none d-md-block d-lg-none">
                        <li class="nav-item">
                            <a class="nav-toggler nav-link waves-effect waves-light text-white"
                                href="javascript:void(0)"><i class="ti-menu ti-close"></i></a>
                        </li>
                    </ul>
                    <!-- ============================================================== -->
                    <!-- Right side toggle and nav items -->
                    <!-- ============================================================== -->
                    <ul class="navbar-nav ms-auto d-flex align-items-center" >

                        <!-- ============================================================== -->
                        <!-- Search -->
                        <!-- ============================================================== -->
                        <li class=" in">
                            <form role="search" class="app-search d-none d-md-block me-3">
                                <input type="text" placeholder="Search..." class="form-control mt-0">
                                <a href="" class="active">
                                    <i class="fa fa-search"></i>
                                </a>
                            </form>
                        </li>
                        <!-- ============================================================== -->
                        <!-- User profile and search -->
                        <!-- ============================================================== -->
                        <li :style="'position: relative'">
                            <div :style="'display: flex; padding-right: 20px'">
                            <a class="profile-pic" href="#">
                                <img src="./plugins/images/users/varun.jpg" alt="user-img" width="36"
                                    class="img-circle"><span class="text-white font-medium">Admin</span>
                            </a>
                            <div :style="'display:flex; align-items:center; position: absolute; left: 90px; height: 100%'">
                                <font-awesome-icon icon="angle-down" class='icon-admin-2'/>
                            </div>
                            </div>
                        </li>
                        <!-- ============================================================== -->
                        <!-- User profile and search -->
                        <!-- ============================================================== -->
                    </ul>
                </div>
            </nav>
        </header>
        <!-- ============================================================== -->
        <!-- End Topbar header -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <aside class="left-sidebar" data-sidebarbg="skin6">
            <!-- Sidebar scroll-->
            <div class="scroll-sidebar">
                <!-- Sidebar navigation-->
                <nav class="sidebar-nav">
                    <ul id="sidebarnav">
                        <!-- User Profile-->
                        <li class="sidebar-item pt-2">
                            <a class="sidebar-link waves-effect waves-dark sidebar-link" href="/admin"
                                aria-expanded="false">
                                <i class="far fa-clock" aria-hidden="true"></i>
                                <span class="hide-menu">Dashboard</span>
                            </a>
                        </li>
                        <li class="sidebar-item">
                            <a class="sidebar-link waves-effect waves-dark sidebar-link" href="/admin/cong-ty"
                                aria-expanded="false">
                                <!-- <i class="fa fa-building" aria-hidden="true"></i> -->
                                <font-awesome-icon icon="building" class='icon-admin'/>
                                <span class="hide-menu">Công ty</span>
                            </a>
                        </li>
                        <li class="sidebar-item">
                            <a class="sidebar-link waves-effect waves-dark sidebar-link" href="/admin/create-recruit"
                                aria-expanded="false">
                                <font-awesome-icon icon="file-circle-plus" class='icon-admin'/>
                                <span class="hide-menu">Tuyển dụng</span>
                            </a>
                        </li>
                        <li class="sidebar-item">
                            <a class="sidebar-link waves-effect waves-dark sidebar-link" href="/admin/chat"
                                aria-expanded="false">
                                <font-awesome-icon icon="comment" class='icon-admin'/>
                                <span class="hide-menu">Trò chuyện</span>
                            </a>
                        </li>
                    </ul>

                </nav>
                <!-- End Sidebar navigation -->
            </div>
            <!-- End Sidebar scroll-->
        </aside>
        <!-- ============================================================== -->
        <!-- End Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Page wrapper  -->
        <!-- ============================================================== -->
        <div class="page-wrapper" style="min-height: 250px;">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <div class="page-breadcrumb bg-white">
                <div class="row align-items-center">
                    <div class="col-lg-3 col-md-4 col-sm-4 col-xs-12">
                        <h4 class="page-title">Thông tin công ty</h4>
                    </div>
                    <div class="col-lg-9 col-sm-8 col-md-8 col-xs-12">
                        <div class="d-md-flex">
                            <ol class="breadcrumb ms-auto">
                            </ol>
                            <a href="https://www.wrappixel.com/templates/ampleadmin/" target="_blank"
                                class="btn btn-danger  d-none d-md-block pull-right ms-3 hidden-xs hidden-sm waves-effect waves-light text-white">Lưu</a>
                        </div>
                    </div>
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- ============================================================== -->
            <!-- End Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Container fluid  -->
            <!-- ============================================================== -->
            <div class="container-fluid">
                <!-- ============================================================== -->
                <!-- Start Page Content -->
                <!-- ============================================================== -->
                <div class="row">
                    <div class="col-md-12">
                        <div class="white-box">
                                <form class="form-horizontal form-material">

                                    <div class="form-group mb-4">
                                        <p :style="{fontSize:'16px', padding: 0, marginBottom:'15px', fontWeight: 'bold'}">Thông tin chung: </p>
                                        <label class="col-md-12 p-0">Tên công ty</label>
                                        <div class="col-md-12 border-bottom p-0">
                                            <input type="text" class="form-control p-0 border-0" v-model="ten">
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <label class="col-md-12 p-0">Mô tả công ty</label>
                                        <div class="col-md-12 border-bottom p-0">
                                            <textarea rows="5" class="form-control p-0 border-0" v-model="moTa"></textarea>
                                        </div>
                                    </div>


                                    <div class="form-group mb-4">
                                        <div>
                                            <div :style="{float: 'left'}">
                                                <p :style="{fontSize:'16px', padding: 0, marginBottom: '15px', fontWeight: 'bold'}">Địa chỉ: </p>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="form-group mb-4" :style="{marginTop: '60px'}">
                                        <label class="col-sm-12">Quốc gia</label>

                                        <div class="col-sm-12 border-bottom">
                                            <select class="form-select shadow-none p-0 border-0 form-control-line" v-model="quocGia">
                                                <option>Việt Nam</option>
                                                <option>Hàn Quốc</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <label class="col-sm-12">Thành phố</label>

                                        <div class="col-sm-12 border-bottom">
                                            <select class="form-select shadow-none p-0 border-0 form-control-line" v-model="thanhPho">
                                                <option>Hà Nội</option>
                                                <option>Hồ Chí Minh</option>
                                            </select>
                                        </div>
                                    </div>

                                    
                                    <div class="form-group mb-4">
                                        <label class="col-sm-12">Quận / Huyện</label>

                                        <div class="col-sm-12 border-bottom">
                                            <select class="form-select shadow-none p-0 border-0 form-control-line" v-model="quan">
                                                <option>Hai Bà Trưng</option>
                                                <option>Hoàn Kiếm</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <label class="col-md-12 p-0">Số nhà, phố, phường</label>
                                        <div class="col-md-12 border-bottom p-0">
                                            <input type="text" class="form-control p-0 border-0" v-model="diaChi">
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <div class="col-sm-12">
                                            <div class="btn btn-success" @click="loadlai">Lưu</div>
                                        </div>
                                    </div>
                                </form>
                        </div>
                    </div>
                </div>
                <!-- ============================================================== -->
                <!-- End PAge Content -->
                <!-- ============================================================== -->
                <!-- ============================================================== -->
                <!-- Right sidebar -->
                <!-- ============================================================== -->
                <!-- .right-sidebar -->
                <!-- ============================================================== -->
                <!-- End Right sidebar -->
                <!-- ============================================================== -->
            </div>
        </div>
        <!-- ============================================================== -->
        <!-- End Page wrapper  -->
        <!-- ============================================================== -->
    </div>
</template>

<script>
import DatePicker from 'vue-datepicker-next';
import 'vue-datepicker-next/index.css';
import { authenticationService } from '../../utility/authenticationService';
import axios from 'axios';
export default {
    components: { DatePicker },
      data() {
    return {
        company: '',
        ten: '',
        moTa: '',
        diaChi: '',
        quocGia: '',
        thanhPho: '',
        quan: ''
    }
  },
  mounted() {
        let config = {
    headers: {
    'Authorization': 'Bearer ' + authenticationService.getAdminToken()
    }
        }
    axios.get('http://localhost:8000/api/employer/company', config)
    .then(res => {
        let data = res.data
        this.ten = data.name,
        this.diaChi = data.address,
        this.moTa = data.desc,
        this.quocGia = 'Việt Nam';
        if (data.province === 1) 
        this.thanhPho = 'Hà Nội'
        else this.thanhPho = "Hồ Chí Minh"

        if (this.$route.query.desc !== undefined) this.moTa = this.$route.query.desc
    })
  },
  methods: {
    loadlai() {
        window.location = '/admin/cong-ty?desc=' + this.moTa
    }
  }
}
</script>
