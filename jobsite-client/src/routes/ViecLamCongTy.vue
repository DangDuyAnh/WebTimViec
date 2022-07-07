<script>
import Navbar from '../components/Navbar2.vue';
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

        for (let index = 0; index < this.company.length; index++) {
            const element = this.company[index];
            element.jobs = []
            axios.get(`http://localhost:8000/api/job/filter?company=${element.id}`, config).then(res => {
                element.jobs = [...res.data]
            })
        }
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
                        <h1 :style="{color: '#0069DB', fontSize: '22px', fontWeight: '700', marginBottom: '40px'}">Công ty gì đó</h1>
                        <h1 :style="{color: '#424242', fontSize: '16px', fontWeight: '400'}"><span :style="{fontWeight: '700'}">Địa chỉ công ty : </span>Địa chỉ gì gì đó</h1>
                        </div>
                    </div>

                    <div :style="{width: '100%', height: '1px', backgroundColor: '#bdbdbd'}"></div>

                    <div :style="{marginTop: '50px', width: '100%'}">
                        <h1 :style="{fontSize: '18px', fontWeight: '600', color: 'black', marginBottom: '30px'}">
                            Các việc đang tuyển dụng
                        </h1>

                        <div :style="{paddingLeft: '40px'}">
                            <div class="job-box">
                                <img :style="{width: '100px', height: '100px', margin: '30px', border: '1px solid black'}" src='../assets/logo.jpg'/>
                                <div>
                                    <h1 :style="{color: 'black', fontSize: '18px', fontWeight: '600', margin: 0, padding: 0}">Tiêu đề </h1>
                                    <div :style="{display: 'flex'}">
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0, width:'200px'}">Công ty</h1>
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0}">Ngành nghề: </h1>
                                    </div>
                                    <div :style="{display: 'flex'}">
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0,  width:'200px'}">Mức lương: </h1>
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0}">Thời gian ứng tuyển</h1>
                                    </div>
                                </div>
                            </div>

                            <div class="job-box">
                                <img :style="{width: '100px', height: '100px', margin: '30px', border: '1px solid black'}" src='../assets/logo.jpg'/>
                                <div>
                                    <h1 :style="{color: 'black', fontSize: '18px', fontWeight: '600', margin: 0, padding: 0}">Tiêu đề </h1>
                                    <div :style="{display: 'flex'}">
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0, width:'200px'}">Công ty</h1>
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0}">Ngành nghề: </h1>
                                    </div>
                                    <div :style="{display: 'flex'}">
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0,  width:'200px'}">Mức lương: </h1>
                                        <h1 :style="{color: 'black', fontSize: '16px', fontWeight: '500', margin: 0, padding: 0}">Thời gian ứng tuyển</h1>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
</template>