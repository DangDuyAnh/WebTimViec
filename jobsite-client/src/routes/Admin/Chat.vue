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

        <div class="page-wrapper" style="min-height: 90vh">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- End Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Container fluid  -->
            <!-- ============================================================== -->
            <div class="page-breadcrumb bg-white">
                <div class="row align-items-center">
                    <div class="col-lg-3 col-md-4 col-sm-4 col-xs-12">
                        <h4 class="page-title">Trò chuyện</h4>
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
			<div class="chat-container">
				<div class="name-list">
					<div class="one-user one-user-active">
						<img src="../../assets/img_avatar3.png" class='avatar-circle' st/>
						<div :style="{fontSize: '15px', fontWeight: 'revert'}">Tên gì đó</div>
					</div>
					<div class="one-user">
						<img src="../../assets/img_avatar3.png" class='avatar-circle' st/>
						<div :style="{fontSize: '15px', fontWeight: 'revert'}">Tên gì đó</div>
					</div>
				</div>

				<div class="conversation">
					<div class="conversation-title">
						<img src="../../assets/img_avatar3.png" class='avatar-circle' st/>
						<div :style="{fontSize: '15px', fontWeight: 'bold'}">Tên gì đó</div>
					</div>

					<div class="conversation-content">
						<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="receiver">
							<div> Hi Aiden, how are you? How is the project coming along? </div>
						</div>
												<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="receiver">
							<div> Hi Aiden, how are you? How is the project coming along? </div>
						</div>
												<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="receiver">
							<div> Hi Aiden, how are you? How is the project coming along? </div>
						</div>
					</div>

					<div class="send-button">
						<input class="send-input"/>
						<font-awesome-icon icon="paper-plane" :style="{color: '#2962ff', width: '20px', height: '20px'}"/>
					</div>
				</div>

			</div>
        </div>
        <!-- ============================================================== -->
        <!-- End Page wrapper  -->
        <!-- ============================================================== -->
    </div>
</template>

