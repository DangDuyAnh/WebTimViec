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
                    <a class="navbar-brand" href="dashboard.html">
                        <span class="logo-text logo-admin"> 
                            JOB SITE
                        </span> 
                    </a>
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
                    <ul class="navbar-nav ms-auto d-flex align-items-center">

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
                            <div :style="'display: flex; padding-right: 20px'" @click="toggleLogout">
                            <a class="profile-pic" href="#">
                                <img src="./plugins/images/users/varun.jpg" alt="user-img" width="36"
                                    class="img-circle"><span class="text-white font-medium">{{admin.username}}</span>
                            </a>
                            <div :style="'display:flex; align-items:center; position: absolute; left: 90px; height: 100%'">
                                <font-awesome-icon icon="angle-down" class='icon-admin-2'/>
                            </div>
                            </div>
                            <div :style="'position: absolute'" class="logout" v-if="openLogout" @click="clickLogout">
                                <p>Logout</p>
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
                            <a class="sidebar-link waves-effect waves-dark sidebar-link" href="dashboard.html"
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
                            <a class="sidebar-link waves-effect waves-dark sidebar-link" href="fontawesome.html"
                                aria-expanded="false">
                                <font-awesome-icon icon="user" class='icon-admin'/>
                                <span class="hide-menu">Ứng viên</span>
                            </a>
                        </li>
                        <li class="sidebar-item">
                            <a class="sidebar-link waves-effect waves-dark sidebar-link" href="map-google.html"
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
                    <div>
                        <ul class="Navbar-tab">
                            <li>
                                <p class = "Navbar-tab-p new">Việc đang tuyển</p>
                            </li>

                            <li>
                                <p class = "Navbar-tab-p">Việc đã tuyển</p>
                            </li>

                        </ul>
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
                <div class="row justify-content-center">
                    <div class="col-lg-4 col-md-12">
                        <div class="white-box analytics-info">
                            <h3 class="box-title">Việc đã tuyển dụng</h3>
                            <ul class="list-inline two-part d-flex align-items-center mb-0">
                                <li>
                                    <div id="sparklinedash"><canvas width="67" height="30"
                                            style="display: inline-block; width: 67px; height: 30px; vertical-align: top;"></canvas>
                                    </div>
                                </li>
                                <li class="ms-auto"><span class="counter text-success">659</span></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-12">
                        <div class="white-box analytics-info">
                            <h3 class="box-title">Việc đang tuyển dụng</h3>
                            <ul class="list-inline two-part d-flex align-items-center mb-0">
                                <li>
                                    <div id="sparklinedash2"><canvas width="67" height="30"
                                            style="display: inline-block; width: 67px; height: 30px; vertical-align: top;"></canvas>
                                    </div>
                                </li>
                                <li class="ms-auto"><span class="counter text-purple">869</span></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-12">
                        <div class="white-box analytics-info">
                            <h3 class="box-title">Ứng viên đang chờ</h3>
                            <ul class="list-inline two-part d-flex align-items-center mb-0">
                                <li>
                                    <div id="sparklinedash3"><canvas width="67" height="30"
                                            style="display: inline-block; width: 67px; height: 30px; vertical-align: top;"></canvas>
                                    </div>
                                </li>
                                <li class="ms-auto"><span class="counter text-info">22</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-12 col-lg-12 col-sm-12">
                        <div class="white-box white-box-extra">
                            <div>
                                <div>
                                    <span :style="{margin:0, padding: 0, marginBottom: 0, fontWeight: '800', fontSize: '16px'}">1/5/2000 - 3/3/2007</span>
                                </div>
                                <div :style="{margin: '15px 0px'}">
                                    <span :style="{margin:0, padding: 0, marginBottom: 0, fontSize: '16px'}">Tiêu đề công việc</span>
                                </div>
                                <div :style="{margin: 0, padding: 0}">
                                    <span :style="{margin:0, padding: 0, color: 'green'}">Đã tuyển 12/15 ứng viên</span></div>
                                <div>
                                    <span :style="{margin:0, padding: 0, color: '#F33E15'}">Có 5 ứng viên đang chờ</span>
                                </div>
                            </div>

                            <div :style="{display: 'flex', flexDirection: 'column', justifyContent: 'center'}">
                                <button class="button-admin" :style="{color: 'green', border: '1px solid green'}">Hoàn thành</button>
                                <button class="button-admin" :style="{color: 'blue', border: '1px solid blue'}">Chỉnh sửa</button>
                                <button class="button-admin" :style="{color: 'red', border: '1px solid red'}">Xóa</button>
                            </div>
                        </div>

                        <div class="white-box white-box-extra">
                            <div>
                                <div>
                                    <span :style="{margin:0, padding: 0, marginBottom: 0, fontWeight: '800', fontSize: '16px'}">1/5/2000 - 3/3/2007</span>
                                </div>
                                <div :style="{margin: '15px 0px'}">
                                    <span :style="{margin:0, padding: 0, marginBottom: 0, fontSize: '16px'}">Tiêu đề công việc</span>
                                </div>
                                <div :style="{margin: 0, padding: 0}">
                                    <span :style="{margin:0, padding: 0, color: 'green'}">Đã tuyển 12/15 ứng viên</span></div>
                                <div>
                                    <span :style="{margin:0, padding: 0, color: '#F33E15'}">Có 5 ứng viên đang chờ</span>
                                </div>
                            </div>

                            <div :style="{display: 'flex', flexDirection: 'column', justifyContent: 'center'}">
                                <button class="button-admin" :style="{color: 'green', border: '1px solid green'}">Hoàn thành</button>
                                <button class="button-admin" :style="{color: 'blue', border: '1px solid blue'}">Chỉnh sửa</button>
                                <button class="button-admin" :style="{color: 'red', border: '1px solid red'}">Xóa</button>
                            </div>
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
import { authenticationService } from "../../utility/authenticationService";
export default {
    data() {
        return {
            admin : authenticationService.getAdmin(),
            openLogout : false,
            dangUngTuyen: [],
            daUngTuyen: []
        }
    },
    mounted(){
        console.log("mounted")
    },
    methods: {
        toggleLogout() {
            this.openLogout = !this.openLogout
        },
        clickLogout() {
            authenticationService.logout();
            window.location = '/'
        }
    }
}
</script>


<style>
@import './css/style.min.css';
@import './Admin.css';

.icon-admin {
    width: 15px;
    height: 15px;
    padding: 2px 10px;
}

.icon-admin-2 {
    width: 15px;
    height: 15px;
    padding: 2px 10px;
    color: white;
    cursor: pointer;
}

.logo-admin {
    color: #ff7b00;
    font-size: 25px;
    font-weight: 700;
    margin-left: 15px;
}

.admin-out-text {
    text-align: center;
}

.logout {
    right: 10px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    padding: 8px 16px;
    border-radius: 5px;
    cursor: pointer;
    z-index: 100;
}


.logout:hover {
    background-color: #d3d3d3;
}

.logout p {
    font-size: 16px;
    color: black;
    margin: 0;
    padding: 0;
}

.white-box-extra:hover {
    background-color: #f8f8f8;
    cursor: pointer;
}

.white-box-extra {
    display: flex;
    justify-content: space-between;
}

</style>