<script>
import { authenticationService } from '../utility/authenticationService';
export default {
    data(){
        return {
            username : authenticationService.getUser().username
        }
    },
    methods: {
        goToChat() {
            window.location = '/chat'
        },
        dangXuat() {
            authenticationService.logout();
            window.location = '/'
        }
    }
}
</script>

<template>
    <div class="Navbar">

        <div class="Navbar-inner">
            <a class="Home" href="/">
                Home
            </a>

            <ul class='Navbar-tab'>
                <li class="Navbar-dropdown">
                    <a class="Navbar-dropbtn">Việc làm</a>
                    <div class="dropdown-content">
                        <div class="dropdown-line">
                            <font-awesome-icon icon="magnifying-glass" class='dropdown-icon'/>
                            <a class="dropdown-line-a" href="/tim-viec-lam-filter">Tìm việc làm</a>
                        </div>
                        <div class="dropdown-line">
                            <font-awesome-icon icon="floppy-disk" class='dropdown-icon'/>
                            <a class="dropdown-line-a" href="/viec-da-luu">Việc làm đã lưu</a>
                        </div>
                        <div class="dropdown-line">
                            <font-awesome-icon icon="share-from-square" class='dropdown-icon'/>
                            <a class="dropdown-line-a" href="/viec-da-ung-tuyen">Việc làm đã ứng tuyển</a>
                        </div>
                    </div>
                </li>

                <li class="Navbar-dropdown">
                    <a class="Navbar-dropbtn">Hồ sơ & CV</a>
                        <div class="dropdown-content">
                            <div class="dropdown-line">
                                <font-awesome-icon icon="id-badge" class='dropdown-icon'/>
                                <a class="dropdown-line-a" href="/my-cv">Quản lý CV</a>
                            </div>
                            <div class="dropdown-line">
                                <font-awesome-icon icon="envelope-open-text" class='dropdown-icon'/>
                                <a class="dropdown-line-a" href="/my-letter">Thư xin việc</a>
                            </div>
                        </div>
                </li>

                <li class="Navbar-dropdown">
                    <a class="Navbar-dropbtn" href="/cong-ty">Công ty</a>
                </li>  
                
                <li class="Navbar-dropdown">
                    <a class="Navbar-dropbtn" href="/goi-y">Gợi ý</a>
                </li> 
            </ul>
        </div>

        <div :style="{marginRight: '22px', display: 'flex', alignItems: 'center'}">

            <font-awesome-icon icon="comments" :style="{color: '#ff7b00', fontSize: '20px', marginRight: '30px', cursor: 'pointer'}"
            @click='goToChat'/>

            <div class="Navbar-dropdown">
                <div :style="{display: 'flex', alignItems: 'center', backgroundColor: '#f5f5f5', padding: '7px 12px', borderRadius: '30px'}">
                    <img src='../assets/img_avatar3.png' :style="{width: '35px', height: '35px', borderRadius: '50%', marginRight: '10px'}"/>
                    <h1 :style="{margin: 0, padding: 0, fontSize: '16px', fontWeight: 'bold'}">{{username}}</h1>
                    <font-awesome-icon icon="angle-down" class='icon-admin-2' :style="{color: '#ff7b00'}"/>
                </div>

                <div class="dropdown-content">
                    <div class="dropdown-line" :style="{minWidth: '0px', width: '120px'}" @click="dangXuat">
                        <a class="dropdown-line-a" :style="{color: '#ff7b00'}">Đăng xuất</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>

</style>
