<script>
import Navbar from '../components/Navbar2.vue';
import { authenticationService } from '../utility/authenticationService';
import axios from 'axios';
export default {
  components: {
    Navbar
  },
  data() {
    return {
        company: '',
        dangUngTuyen: [],
    }
  },
  mounted() {
    let config = {
    headers: {
    'Authorization': 'Bearer ' + authenticationService.getUserToken()
    }
    }
    axios.get('http://localhost:8000/api/company/list', config)
    .then(res => {
        let data = res.data
        data.forEach(element => {
            if (String(element.id) === this.$route.params.id) {
                this.company = element
            }
        });
    })
    axios.get("http://localhost:8000/api/job/include?company=" + this.$route.params.id, config)
    .then(data => {
        let dangUngTuyen = data.data.filter(item => item.type !== 'done')
        console.log(dangUngTuyen)
        this.dangUngTuyen = [...dangUngTuyen]
    })
  }
}
</script>

<template>
    <Navbar />
            <div class="container-congty">
                <div class="box-congty">
                    <div :style="{display: 'flex', alignItems: 'center', marginBottom: '50px'}">
                        <img :style="{width: '150px', height: '150px', marginRight: '40px'}" src='../assets/logo.jpg'/>
                        <div>
                        <h1 :style="{color: '#0069DB', fontSize: '22px', fontWeight: '700', marginBottom: '40px'}">{{company.name}}</h1>
                        <h1 :style="{color: '#424242', fontSize: '16px', fontWeight: '400'}"><span :style="{fontWeight: '700'}">Địa chỉ công ty : </span>{{company.address}}</h1>
                        </div>
                    </div>

                    <div :style="{width: '100%', height: '1px', backgroundColor: '#bdbdbd'}"></div>

                    <div :style="{marginTop: '50px', width: '100%'}">
                        <h1 :style="{fontSize: '18px', fontWeight: '600', color: 'black', marginBottom: '30px'}">
                            Các việc đang tuyển dụng
                        </h1>

                        <div :style="{paddingLeft: '40px'}">
                            <div class="job-box" v-for="(item, index) in dangUngTuyen">
                                <img :style="{width: '100px', height: '100px', margin: '30px', border: '1px solid black'}" src='../assets/logo.jpg'/>
                                <div>
                                    <h1 :style="{color: 'black', fontSize: '18px', fontWeight: '600', margin: 0, padding: 0, marginBottom: '10px'}">{{item.title}} </h1>
                                    <div :style="{display: 'flex'}">
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0, width:'350px'}">{{company.name}}</h1>
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0}">Ngành nghề: {{item.field}}</h1>
                                    </div>
                                    <div :style="{display: 'flex'}">
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0,  width:'350px'}">Mức lương: {{item.salary_min}} - {{item.salary_max}} VNĐ</h1>
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0}">Thời gian ứng tuyển: {{item.public_date}} - {{item.expired_date}}</h1>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
</template>