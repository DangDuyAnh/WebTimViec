<script>
import Navbar2 from '../../components/Navbar.vue';
import Navbar from '../../components/Navbar2.vue';
import { authenticationService } from '../../utility/authenticationService';
export default {
  components: {
    Navbar,
    Navbar2
  },
  data() {
    return {
      index: 0,
      congViec: '',
      diaDiem: '',
      userToken: authenticationService.getUserToken()
    }
  }, 
    methods: {
        increment() {
            this.index++
        },
        decrement() {
		    this.index--
		},
        search() {
            window.location = '/tim-viec-lam?congviec=' + this.congViec + '&diadiem=' + this.diaDiem
        },
        goByTag () {
            window.location = '/tim-viec-lam?tag=nganhang'
        },
        check() {
            if (this.userToken) return 1;
            else return 0;
        }
    },
}
</script>

<template>
    <Navbar v-if="userToken"/>
    <Navbar2 v-else/>
    <div class="container">
        <div class="search-box">
            <div class="input-wrapper">
                <h1 class="input-label">Công việc</h1>
                <input v-model="congViec">
                <font-awesome-icon icon="magnifying-glass" class='input-icon'/>
            </div>
            <div class="input-wrapper">
                <h1 class="input-label">Địa điểm</h1>
                <input v-model="diaDiem">
                <font-awesome-icon icon="location-dot" class='input-icon'/>
            </div>
            <button @click="search" class="navbar-button" :style="{backgroundColor: '#e65100', border: '1px solid #e65100', color: 'white', padding: '5px 15px', margin: '5px 8px'}">Tìm kiếm</button>
        </div>

        <div :style="{display: 'flex', justifyContent: 'center'}">
            <a class="tao-CV" href="/my-cv">Tạo CV của bạn</a>
        </div>
        
        <div class="job-part">
            <h1 :style="{marginBottom: '30px', marginLeft: '70px', fontSize: '30px', fontWeight: 'bold'}">
                Việc làm theo ngành nghề
            </h1>

            <div v-if="index > 0" class="prev" @click="decrement"><p>&#10094;</p></div>
            <div v-if="index < 2" class="next" @click="increment"><p>&#10095;</p></div>

            <div class="job-series">
                <div class="track" :style="{transform: 'translateX(-'+ (index*186) +'px)'}">
                    <div class="card" :style="{backgroundColor: '#ffa45b'}">
                        <h1>Công nghệ thông tin</h1>
                    </div>
                    <div class="card" :style="{backgroundColor: '#bce6eb'}">
                        <h1>Kế toán / Kiểm toán</h1>
                    </div>    
                    <div class="card" :style="{backgroundColor: '#ffda77'}" @click="goByTag">
                        <h1>Ngân hàng</h1>
                    </div>
                    <div class="card" :style="{backgroundColor: '#fdcfdf'}">
                        <h1>Xây dựng</h1>
                    </div>  
                    <div class="card" :style="{backgroundColor: '#f2dcbb'}">
                        <h1>Y tế</h1>
                    </div>
                    <div class="card" :style="{backgroundColor: '#edf285'}">
                        <h1>Du lịch</h1>
                    </div>    
                    <div class="card" :style="{backgroundColor: '#a1eafb'}">
                        <h1>Nhân sự</h1>
                    </div>
                    <div class="card" :style="{backgroundColor: '#ff91b3'}">
                        <h1>Bảo hiểm</h1>
                    </div>                  
                </div>
            </div>

        </div>
    </div>
</template>

<style>
@import './TrangChu.css';
</style>