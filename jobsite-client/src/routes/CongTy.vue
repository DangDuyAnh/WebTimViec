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
        company: ''
    }
  },
  mounted() {
    let config = {
        headers: {
            'Authorization': 'Bearer ' + authenticationService.getUserToken()
        }
    }
    axios.get('http://localhost:8000/api/company/list', config).then(res => {
        console.log(res)
        let data = res.data
        this.company = [...data]
    })
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
                        <label class="container-checkbox">Hà Nội
                            <input type="checkbox" checked="checked">
                            <span class="checkmark"></span>
                        </label>
                        <label class="container-checkbox">Hồ Chí Minh
                            <input type="checkbox">
                            <span class="checkmark"></span>
                        </label>
                        <label class="container-checkbox">Đà Nẵng
                            <input type="checkbox">
                            <span class="checkmark"></span>
                        </label>
                    </div>

                    <div :style="{width: '920px', display: 'flex', flexWrap: 'wrap'}">
                        <div class="card-congty" v-for="item in company">
                            <div class="congty-wrapper">
                                <img :style="{width: '150px', height: '150px'}" src='../assets/logo.jpg'/>
                            </div>
                            <h1 :style="{fontSize: '18px', fontWeight: '700', color: 'black'}">{{item.name}}</h1>
                            <h1 :style="{fontSize: '14px', fontWeight: '600', color: '#0069DB'}">3 việc đang ứng tuyển</h1>
                            <h1 :style="{fontSize: '14px', fontWeight: '400', color: '#6c757d'}">Hà Nội</h1>
                        </div>   
                        
                    </div>
                </div>
            </div>
        </div>  
</template>