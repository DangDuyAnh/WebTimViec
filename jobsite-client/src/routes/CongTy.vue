<script>
import Navbar from '../components/Navbar.vue';
import { authenticationService } from '../utility/authenticationService';
import axios from 'axios';
export default {
  components: {
    Navbar
  },
  data() {
    return {
        company: '',
        renderCompany: '',
        cityChoose: 0,
        check1: false,
        check2: false,
        check3: false
    }
  },
  mounted() {
    let config = {
    headers: {
    'Authorization': 'Bearer ' + authenticationService.getAdminToken()
    }
    }
    axios.get('http://localhost:8000/api/company/list', config)
    .then(res => {
        let data = res.data
        data.forEach(element => {
            if (element.province === 1) element.province = 'Hà Nội'
            else element.province = 'Hồ Chí Minh'
        });
        this.company = [...data]
        this.renderCompany = [...data]
    })
  },
  methods: {
    check(num) {
        if (num === 1) {
            this.check2 = false
            this.check3 = false
            let data
            if (this.check1 === false) {
            data = this.company.filter(item => item.province === 'Hà Nội')
            } else {
                data = this.company
            }
            this.renderCompany = [...data]
        }
        else if (num === 2) {
            this.check1 = false
            this.check3 = false
            let data
            if (this.check2 === false) {
            data = this.company.filter(item => item.province === 'Hồ Chí Minh')
            } else {
                data = this.company
            }
            this.renderCompany = [...data]
        }
        else if (num === 3) {
            this.check1 = false
            this.check2 = false
            let data
            if (this.check3 === false) {
            data = this.company.filter(item => item.province === 'Đà Nẵng')
            } else {
                data = this.company
            }
            this.renderCompany = [...data]
        }
        if (this.cityChoose === num) this.cityChoose = 0
        else this.cityChoose = num
    },
    moveToDetail(item) {
        window.location = '/viec-lam-cong-ty/' + item.id
    }
  }
}
</script>

<template>
    <Navbar />
        <div class="container-congty">
            <div class="box-congty">
                <div :style="{display: 'flex', justifyContent: 'space-between'}">
                    <h1 :style="{fontWeight: '900', color: 'black'}">Danh sách công ty</h1>
                    <div class="input-wrapper-2">
                        <font-awesome-icon icon="magnifying-glass" class='input-icon-2'/>
                        <input placeholder="Tìm công ty">
                    </div>
                </div>

                <div :style="{display: 'flex', marginTop: '70px'}">
                    <div :style="{width: '250px'}">
                        <h1 :style="{color: 'black', fontSize: '17px', fontWeight: '700', marginBottom: '20px'}">Nơi làm việc</h1>
                        <label class="container-checkbox" >Hà Nội
                            <input type="checkbox" @click="check(1)" v-model="check1">
                            <span class="checkmark"></span>
                        </label>
                        <label class="container-checkbox">Hồ Chí Minh
                            <input type="checkbox" @click="check(2)" v-model="check2">
                            <span class="checkmark"></span>
                        </label>
                        <label class="container-checkbox" >Đà Nẵng
                            <input type="checkbox" @click="check(3)" v-model="check3">
                            <span class="checkmark"></span>
                        </label>
                    </div>

                    <div :style="{width: '920px', display: 'flex', flexWrap: 'wrap'}">
                        <div class="card-congty" v-for="(item, index) in renderCompany" @click="moveToDetail(item)">
                            <div class="congty-wrapper">
                                <img :style="{width: '150px', height: '150px'}" src='../assets/logo.jpg'/>
                            </div>
                            <h1 :style="{fontSize: '18px', fontWeight: '700', color: 'black'}">{{item.name}}</h1>
                            <h1 :style="{fontSize: '14px', fontWeight: '600', color: '#0069DB'}">{{item.desc}}</h1>
                            <h1 :style="{fontSize: '14px', fontWeight: '400', color: '#6c757d'}">{{item.province}}</h1>
                        </div>   
        
                    </div>
                </div>
            </div>
        </div>  
</template>