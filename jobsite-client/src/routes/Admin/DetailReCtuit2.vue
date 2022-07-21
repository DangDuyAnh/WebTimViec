<template>

    <div id="myModal" className="modal modal-active" v-if="modal" @click="closeModal">
        <div className="modal-content">
            <!-- <span class="close-2">&times;</span> -->
            <font-awesome-icon icon="xmark" class="close-2"></font-awesome-icon>
            <p :style="{textAlign: 'center', fontWeight: 'bold', fontSize: '20px', marginTop: 0}">CV ứng viên</p>
            <p :style="{textAlign: 'center'}" v-if="cv === -1">(Chưa có thông tin)</p>
            <img src='../../assets/CV1.png' v-if="cv === 0"/>
            <img src='../../assets/CV2.png' v-if="cv === 1"/>
            <img src='../../assets/CV3.png' v-if="cv === 2"/>
            <p :style="{textAlign: 'center', fontWeight: 'bold', fontSize: '20px', marginTop: 0}">Thư xin việc ứng viên</p>
            <p :style="{textAlign: 'center'}" v-if="letter === -1">(Chưa có thông tin)</p>
            <img src='../../assets/Letter1.png' v-if="letter === 0"/>
            <img src='../../assets/Letter1.png' v-if="letter === 1"/>
            <img src='../../assets/Letter1.png' v-if="letter === 2"/>
        </div>
    </div> 

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
                    <a class="navbar-brand" href="/admin">
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
                            <div :style="{display: 'flex', alignItems : 'center', position: 'absolute', left: '115px', height: '100%'}">
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
                        <h4 class="page-title" :style="{color: '#ff7b00'}">Thông tin tuyển dụng</h4>
                    </div>

                    <div class="col-lg-9 col-sm-8 col-md-8 col-xs-12">
                        <div class="d-md-flex">
                            <ol class="breadcrumb ms-auto">
                            </ol>
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
                            <div :style="{marginLeft: '170px'}">
                                <div :style="{display: 'flex'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '200px', fontSize: '16px'}">Tiêu đề công việc: </p>
                                    <p className="booking-pay-line" :style="{fontSize:'16px'}">{{job.title}}</p>
                                </div>
                                <div :style="{display: 'flex'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '200px'}">Số lượng cần tuyển: </p>
                                    <p className="booking-pay-line" :style="{fontSize:'16px'}">{{job.avaiable_slot}}</p>
                                </div>
                                <div :style="{display: 'flex'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '200px'}">Ngành nghề: </p>
                                    <p className="booking-pay-line" :style="{fontSize:'16px'}">{{job.field}}</p>
                                </div>
                                <div :style="{display: 'flex'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '200px'}">Mức lương: </p>
                                    <p className="booking-pay-line" :style="{fontSize:'16px'}">{{job.salary_min}} - {{job.salary_max}} VNĐ</p>
                                </div>
                                <div :style="{display: 'flex'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '200px', fontSize: '16px'}">Thời gian ứng tuyển: </p>
                                    <p className="booking-pay-line" :style="{fontSize:'16px'}">{{job.public_date}} - {{job.expired_date}}</p>
                                </div>
                                <div :style="{display: 'flex'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '200px'}">Cấp bậc: </p>
                                    <p className="booking-pay-line" :style="{fontSize:'16px'}">{{job.position}}</p>
                                </div>
                                <div :style="{display: 'flex'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '200px'}">Yêu cầu kinh nghiệm: </p>
                                    <p className="booking-pay-line" :style="{fontSize:'16px'}">{{job.required_experience}}</p>
                                </div>
                                <div :style="{display: 'flex'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '200px'}">Hình thức làm việc: </p>
                                    <p className="booking-pay-line" :style="{fontSize:'16px'}">{{job.type}}</p>
                                </div>

                                <div :style="{display: 'flex', margin: '50px 0px 10px 0px'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '200px', color: 'green'}">Đã ứng tuyển: </p>
                                    <p className="booking-pay-line" :style="{fontSize:'16px', color: 'green'}">{{job.accepted_applicant}}/{{job.avaiable_slot}} ứng viên</p>
                                </div>

                                <div :style="{display: 'flex', alignItems: 'center'}">
                                    <p class="booking-pay-line" :style="{fontWeight:'bold', width: '210px'}">Danh sách ứng viên: </p>
                                    <div :style="{width: '600px'}">
                                        <select class="form-select shadow-none row border-top" v-model="filter">
                                            <option>Ứng viên đang chờ</option>
                                            <option>Ứng viên đã tuyển</option>
                                        </select>
                                    </div>
                                </div>

                                <div>
                                    <div :style="{marginTop: '40px'}">
                                        <div class="row-user" v-for="(item, index) in listCand">
                                            <div :style="{display: 'flex', alignItems: 'center'}">
                                                <img src="../../assets/img_avatar3.png" class='avatar-circle'/>
                                                <div class="user-name">{{item.user.username}}</div>
                                                <font-awesome-icon v-if="clicked[index] === 2" icon="xmark" :style="{marginLeft: '10px', fontSize: '18px',color: '#F33155'}" @click="reset(index)"/>
                                                <font-awesome-icon v-if="clicked[index] === 1" icon="check" :style="{marginLeft: '10px', fontSize: '18px',color: '#7ACE4C'}" @click="reset(index)"/>
                                            </div> 

                                            <div :style="{display: 'flex', alignItems: 'center'}">
                                                <div class="avatar-wrapper-button button-color-yellow" @click="openModal(item)">
                                                    <font-awesome-icon icon="id-badge" class='icon-button'/>
                                                </div>
                                                <div class="avatar-wrapper-button button-color-blue" @click="moveToChat(item)">
                                                    <font-awesome-icon icon="comments" class='icon-button'/>
                                                </div>
                                                <div class="avatar-wrapper-button button-color-green" v-if="selectFilter" @click="accept(index)">
                                                    <font-awesome-icon icon="check" class='icon-button'/>
                                                </div>
                                                <div class="avatar-wrapper-button button-color-red" v-if="selectFilter" @click="deny(index)">
                                                    <font-awesome-icon icon="xmark" class='icon-button'/>
                                                </div>
                                            </div> 
                                        </div>

                                    </div>
                                </div>

                                <div class="form-group mb-4" :style="{margin: '40px 0px 0px 350px'}">
                                    <div class="col-sm-12">
                                        <button class="btn btn-success" :style="{color: 'white'}" @click="save">Lưu</button>
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
import axios from 'axios'
import { authenticationService } from "../../utility/authenticationService";

    export default {
        data() {
            return{
                filter: 'Ứng viên đang chờ',
                admin : authenticationService.getAdmin(),
                modal: false,
                job: '',
                listCand: [],
                selectFilter: true,
                clicked: [],
                cv: -1,
                letter: -1
            }
        },
        watch: {
            async filter(newValue, oldValue) {
                if (newValue === 'Ứng viên đang chờ') {
                    this.selectFilter = true
                    let config = {
                    headers: {
                    'Authorization': 'Bearer ' + authenticationService.getAdminToken()
                    }
                    }
                    axios.get('http://localhost:8000/api/employer/applicant-list?job_id=' + this.$route.params.id + '&status=0', config)
                    .then(res => {
                        let array = res.data
                        let array2 = []
                        let array3 = []
                        async function getUser(e) {
                            let res2 = await axios.get('http://localhost:8000/api/employee/profile?id=' + e.id , config);
                            array2.push(res2.data)
                            array3.push(0)
                        }
                        Promise.all(array.map(getUser)).then(item => {
                            this.listCand = [...array2];
                            this.clicked = [...array3]});
                    })
                } else if (newValue === 'Ứng viên đã tuyển') {
                    this.selectFilter = false
                    let config = {
                    headers: {
                    'Authorization': 'Bearer ' + authenticationService.getAdminToken()
                    }
                    }
                    axios.get('http://localhost:8000/api/employer/applicant-list?job_id=' + this.$route.params.id + '&status=1', config)
                    .then(res => {
                        let array = res.data
                        let array2 = []
                        let array3 = []
                        async function getUser(e) {
                            let res2 = await axios.get('http://localhost:8000/api/employee/profile?id=' + e.id , config);
                            array2.push(res2.data)
                            array3.push(0)
                        }
                        Promise.all(array.map(getUser)).then(item => {
                            this.listCand = [...array2];
                            this.clicked = [...array3]})
                    })
                }
                }
        },
        mounted(){
        let config = {
        headers: {
        'Authorization': 'Bearer ' + authenticationService.getAdminToken()
        }
        }
        axios.get('http://localhost:8000/api/job/detail?id=' + this.$route.params.id, config)
        .then(data => {
            this.job = data.data;
            console.log(data.data)
        })

        axios.get('http://localhost:8000/api/employer/applicant-list?job_id=' + this.$route.params.id + '&status=0', config)
        .then(res => {
            let array = res.data
            let array2 = []
            let array3 = []
            async function getUser(e) {
                let res2 = await axios.get('http://localhost:8000/api/employee/profile?id=' + e.id , config);
                array2.push(res2.data)
                array3.push(0)
            }
            Promise.all(array.map(getUser)).then(item => {
                console.log(array2)
                this.listCand = [...array2];
                this.clicked = [...array3]})
        })        
        },
        methods: {
            moveToChat(item) {
                let config = {
                headers: {
                'Authorization': 'Bearer ' + authenticationService.getAdminToken()
                }
                }
                axios.post('http://localhost:8000/api/chat-room/create-pair', {user_id: item.user.id, room_name: authenticationService.getAdmin().id + item.user.id}, config)
                .then(res => {
                    window.location = '/admin/chat'
                })
                window.location = '/admin/chat'
            }
            ,
            accept(index) {
                console.log('clicked')
                console.log(this.clicked)
                let array = this.clicked
                array[index] = 1
                console.log('array')
                console.log(array)
                this.clicked = [...array]
            },
            deny (index) {
                console.log('deny')
                let array = this.clicked
                array[index] = 2
                this.clicked  = [...array]
            },
            reset (index) {
                console.log('reset')
                let array = this.clicked
                array[index] = 0
                this.clicked  = [...array]
            },
            save () {
                    let config = {
                    headers: {
                    'Authorization': 'Bearer ' + authenticationService.getAdminToken()
                    }
                    }
                    console.log('List Cand')
                    function hi() {
                        console.log(this.listCand)
                    }
                    hi()
                    

                // Promise.all(this.clicked.forEach((item, index) => {
                //     let config = {
                //     headers: {
                //     'Authorization': 'Bearer ' + authenticationService.getAdminToken()
                //     }
                //     }
                //     axios.post('http://localhost:8000/api/employer/set-status', {employee_id: this.listCand[index].id, job_id: this.$route.params.id, status: item}, config)
                //     .then(data => {
                //         console.log(data)
                //     })
                // }))

                    async function getUser(item, index) {
                        console.log(this.$route.params.id)
                        // await axios.post('http://localhost:8000/api/employer/set-status', {employee_id: this.listCand[index].id, job_id: this.$route.params.id, status: item}, config)
                    }
                        Promise.all(this.clicked.map((item, index) => getUser(item, index)))


                // let config = {
                // headers: {
                // 'Authorization': 'Bearer ' + authenticationService.getAdminToken()
                // }
                // }
                // let res = await axios.get("http://localhost:8000/api/job/detail?id=" + this.$route.params.id, config)
                // let yes = this.clicked.filter (item => item === 1)
                // let data = res.data
                // data.accepted_applicant = data.accepted_applicant + yes.length
                // axios.post("http://localhost:8000/api/job/update", data, config)
                // window.location = '/admin/detail-recruit/' + this.$route.params.id
            }, 
            closeModal(){
                this.modal = false
            },
            openModal(item) {
                let config = {
                headers: {
                'Authorization': 'Bearer ' + authenticationService.getAdminToken()
                }
                }
                axios.get('http://localhost:8000/api/employee/profile?id=' + item.id , config)
                .then(res => {
                        if (res.data.main_cv_id !== null && res.data.main_cv_id !== undefined) {
                            this.cv = res.data.main_cv_id;
                        }

                        if (res.data.main_letter_id !== null && res.data.main_letter_id !== undefined) {
                            this.letter = res.data.main_letter_id;
                        }
                        this.modal = true
                })
            }
        }
    }
</script>

<style>
    .booking-pay-line {
    margin: 3px 0px 3px 0px;
    padding: 0;
    font-size: 16px;
    }

</style>