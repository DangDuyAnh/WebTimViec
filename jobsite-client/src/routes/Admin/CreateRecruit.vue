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
                            <div :style="'position: absolute'" class="logout">
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
                    <div class="col-lg-3 col-md-4 col-sm-4 col-xs-12">
                        <h4 class="page-title">Đăng tin tuyển dụng</h4>
                    </div>
                    <div class="col-lg-9 col-sm-8 col-md-8 col-xs-12">
                        <div class="d-md-flex">
                            <ol class="breadcrumb ms-auto">
                            </ol>
                            <a href="https://www.wrappixel.com/templates/ampleadmin/" target="_blank"
                                class="btn btn-danger  d-none d-md-block pull-right ms-3 hidden-xs hidden-sm waves-effect waves-light text-white">Đăng</a>
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
                                <div class="form-horizontal form-material">
                                    <div class="form-group mb-4">
                                        <label class="col-md-12 p-0">Tiêu đề công việc</label>
                                        <div class="col-md-12 border-bottom p-0">
                                            <textarea rows="5" class="form-control p-0 border-0" v-model="tieuDe"></textarea>
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <label class="col-md-12 p-0">Số lượng cần tuyển</label>
                                        <div class="col-md-12 border-bottom p-0">
                                            <input type="text" class="form-control p-0 border-0" v-model="soLuongCanTuyen">
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <label class="col-md-12 p-0">Ngành nghề:</label>
                                        <div class="content">
                                            <ul>
                                                <li v-for="(tag, index) in tags">
                                                    {{tag}} <i class="fas fa-times-circle" @click="remove(index)"></i>
                                                </li>
                                                <input type="text" spellcheck="false" v-model="text"  @keyup.right="addTag($event)">
                                            </ul>
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <label class="col-md-6 p-0">Mức lương</label>
                                        <div>
                                            <div :style="{float: 'left'}">
                                                <p :style="{fontSize:'16px', padding: 0, margin: '7px 10px 0px 0px', fontStyle: 'italic', fontWeight: '800'}">từ</p>
                                            </div>
                                            <div class="col-md-4 border-bottom p-0" :style="{float: 'left'}">
                                                <input class="form-control p-0 border-0" placeholder="0" v-model="from">
                                            </div>
                                            <div :style="{float: 'left'}">
                                                <p :style="{fontSize:'16px', padding: 0, margin: '7px 0px 0px 7px', fontStyle: 'italic'}">VNĐ</p>
                                            </div>

                                            <div :style="{float: 'left'}">
                                                <p :style="{fontSize:'16px', padding: 0, margin: '7px 10px 0px 170px', fontStyle: 'italic', fontWeight: '800'}">đến</p>
                                            </div>
                                            <div class="col-md-4 border-bottom p-0" :style="{float: 'left'}">
                                                <input  class="form-control p-0 border-0" placeholder="0" v-model="to">
                                            </div>
                                            <div :style="{float: 'left'}">
                                                <p :style="{fontSize:'16px', padding: 0, margin: '7px 0px 0px 7px', fontStyle: 'italic'}">VNĐ</p>
                                            </div>                                         
                                        </div>
                                    </div>

                                    <div class="form-group mb-4" :style="{marginTop: '60px'}">
                                        <label class="col-md-6 p-0">Thời gian ứng tuyển</label>
                                        <div>
                                            <div :style="{float: 'left'}">
                                                <p :style="{fontSize:'16px', padding: 0, margin: '7px 10px 0px 0px', fontStyle: 'italic', fontWeight: '800'}">từ</p>
                                            </div>
                                            <div :style="{float: 'left'}">
                                                <DatePicker v-model:value="timeStart" />
                                            </div>

                                            <div :style="{float: 'left'}">
                                                <p :style="{fontSize:'16px', padding: 0, margin: '7px 10px 0px 395px', fontStyle: 'italic', fontWeight: '800'}">đến</p>
                                            </div>
                                            <div :style="{float: 'left'}">
                                                <DatePicker v-model:value="timeEnd" />
                                            </div>                                   
                                        </div>
                                    </div>

                                    <div class="form-group mb-4" :style="{marginTop: '60px'}">
                                        <label class="col-sm-12">Cấp bậc</label>

                                        <div class="col-sm-12 border-bottom">
                                            <select class="form-select shadow-none p-0 border-0 form-control-line" v-model="capBac">
                                                <option>--Chọn cấp bậc--</option>
                                                <option>Fresher</option>
                                                <option>Giám đốc</option>
                                                <option>Nhân viên</option>
                                                <option>Project Manager</option>
                                                <option>Thực tập sinh</option>
                                                <option>Trưởng phòng</option>
                                                <option>Sennior</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <label class="col-sm-12">Yêu cầu kinh nghiệm</label>

                                        <div class="col-sm-12 border-bottom">
                                            <select class="form-select shadow-none p-0 border-0 form-control-line" v-model="kinhNghiem">
                                                <option>--Chọn số năm kinh nghiệm--</option>
                                                <option>Không cần kinh nghiệm</option>
                                                <option>Dưới 1 năm</option>
                                                <option>Từ 1 - 3 năm</option>
                                                <option>> 5 năm</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <label class="col-sm-12">Hình thức làm việc</label>

                                        <div class="col-sm-12 border-bottom">
                                            <select class="form-select shadow-none p-0 border-0 form-control-line" v-model="type">
                                                <option>Offline</option>
                                                <option>Remote</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="form-group mb-4">
                                        <div class="col-sm-12">
                                            <button class="btn btn-success" @click="dangTin">Đăng tin</button>
                                        </div>
                                    </div>
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
import DatePicker from 'vue-datepicker-next';
import 'vue-datepicker-next/index.css';
import { post } from '../../utility/api'; 
import { authenticationService } from '../../utility/authenticationService';

export default {
    components: { DatePicker },
  data() {
    return {
      tags: [],
      text: '',
      from: undefined,
      to: undefined,
      savedFrom: 0,
      savedTo: 0,
      timeStart: null,
      timeEnd: null,
      tieuDe: '',
      soLuongCanTuyen: '',
      capBac: '--Chọn cấp bậc--',
      kinhNghiem: '--Chọn số năm kinh nghiệm--',
      type: 'Offline',
    }
  },
    methods: {
        formatDate(date) {
        var d = new Date(date),
            month = '' + (d.getMonth() + 1),
            day = '' + d.getDate(),
            year = d.getFullYear();

        if (month.length < 2) 
            month = '0' + month;
        if (day.length < 2) 
            day = '0' + day;

        return [year, month, day].join('/');
    },
        increment() {
            this.index++
        },
        decrement() {
		    this.index--
		},
        addTag(e){
            let tag = e.target.value.replace(/\s+/g, ' ');
            if(tag.length > 1 && !this.tags.includes(tag)){
                this.text = ''
                if(this.tags.length < 10){
                    tag.split(',').forEach(tag => {
                        this.tags.push(tag);
                    });
                }
               
            }
        },
        remove(index) {
            this.tags = [...this.tags.slice(0, index), ...this.tags.slice(index + 1)];
        },
        async dangTin() {
            let field = ''
            this.tags.forEach((item, index)=> {
                if (index < (this.tags.length - 1))
                    field += item + ', '
                else field += item
            })
            let sendObj = {
                title: this.tieuDe,
                salary_min : this.savedFrom,
                salary_max : this.savedTo,
                avaiable_slot: this.soLuongCanTuyen,
                field: field,
                position: this.capBac,
                required_experience: this.kinhNghiem,
                type: this.type,
                company: authenticationService.getCompanyId(),
                public_date: this.formatDate(this.timeStart),
                expired_date: this.formatDate(this.timeEnd)
            }
            console.log(sendObj)
            let res = await post('/job/register', sendObj, authenticationService.getAdminToken())
            console.log(res.data)
        }
    },
    watch: {
        from: function(newValue) {
        this.savedFrom = newValue
        const result = newValue.replace(/\D/g, "")
            .replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        this.from = result;
        },
        to: function(newValue) {
        this.savedTo = newValue
        const result = newValue.replace(/\D/g, "")
            .replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        this.to = result;
        },
  }
}
</script>

<style>
/* Import Google Font - Poppins */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

::selection{
  color: #fff;
  background: #5372F0;
}
.wrapper{
  width: 496px;
  background: #fff;
  border-radius: 10px;
  padding: 18px 25px 20px;
  box-shadow: 0 0 30px rgba(0,0,0,0.06);
}
.wrapper :where(.title, li, li i, .details){
  display: flex;
  align-items: center;
}
.title img{
  max-width: 21px;
}
.title h2{
  font-size: 21px;
  font-weight: 600;
  margin-left: 8px;
}
.wrapper .content{
  margin: 10px 0;
}
.content p{
  font-size: 15px;
}
.content ul{
  display: flex;
  flex-wrap: wrap;
  padding: 7px;
  margin: 12px 0;
  border-radius: 5px;
  border: 1px solid #a6a6a6;
}
.content ul  li{
  color: #333;
  margin: 4px 4px;
  list-style: none;
  border-radius: 5px;
  background: #F2F2F2;
  padding: 5px 8px 5px 8px;
  border: 1px solid #e3e1e1;
  font-size: 16px;
}
.content ul li i{
  height: 20px;
  width: 20px;
  color: #808080;
  margin-left: 8px;
  font-size: 15px;
  cursor: pointer;
  border-radius: 50%;
  justify-content: center;
}
.content ul input{
  flex: 1;
  padding: 5px;
  border: none;
  outline: none;
  font-size: 16px;
}
.wrapper .details{
  justify-content: space-between;
}
.details button{
  border: none;
  outline: none;
  color: #fff;
  font-size: 14px;
  cursor: pointer;
  padding: 9px 15px;
  border-radius: 5px;
  background: #5372F0;
  transition: background 0.3s ease;
}
.details button:hover{
  background: #2c52ed;
}
</style>