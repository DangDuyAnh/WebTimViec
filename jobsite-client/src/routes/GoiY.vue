<template>
    <Navbar v-if="userToken"/>
    <Navbar2 v-else/>
    <div class="container-cv">
      <div class="boxwhite-cv">
        <div :style="{display: 'flex', justifyContent: 'center'}">
        <div :style="{width: '800px', marginTop: '50px'}">
            <h3 :style="{fontWeight: 'bold', fontSize: '24px'}">Gợi ý công việc</h3>
            <p :style="{fontSize: '16px', fontWeight: '400', margin: '20px 0px 0px 0px'}">Lĩnh vực</p>
            <input class="goi-y-input" v-model="expertise"/>
            <p :style="{fontSize: '16px', fontWeight: '400', margin: '20px 0px 0px 0px'}">CV</p>
            <textarea :rows="7" class="goi-y-input" v-model="resume"></textarea>
            <div :style="{display: 'flex', justifyContent: 'center', margin: '50px 0px'}">
                <button class="navbar-button" :style="{backgroundColor: '#e65100', border: '1px solid #e65100', color: 'white', padding: '5px 10px', margin: '5px 8px'}" @click="search()">Tìm kiếm</button>
            </div>
            <div :style="{display: 'flex', justifyContent: 'center'}" v-if="load">
                <div class="loader"></div>
            </div>
            <div :style="{display: 'flex', justifyContent: 'center', width: '100%'}">
                <div :style="{width: '750px', display: 'flex', flexWrap: 'wrap'}">
                    <div class="card-congty-2" v-for="(item, index) in job">
                        <div class="congty-wrapper-2">
                            <img :style="{width: '150px', height: '150px'}" :src="item.logo_link"/>
                        </div>
                        <h1 :style="{fontSize: '14px', fontWeight: '400', color: '#6c757d', textAlign: 'center'}">{{item.job_name}}</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
      </div>
    </div>
</template>

<style>
    .goi-y-input {
        background-color: #eeeeee;
        border: 2px solid #f5f5f5; 
        border-radius: 5px;
        padding: 4px 8px;
        width: 100%;
        transition: border 0.4s ease, background-color 0.4s ease;
    }

    .goi-y-input:focus {
        border: 2px solid #ff9800; 
        background-color: white;
    }

    .card-congty-2 {
    width: 170px;
    height: 170px;
    margin-bottom: 100px;
    cursor: pointer;
    margin-left: 7px;
    margin-right: 7px;
  }

  .congty-wrapper-2 {
    width: 170px;
    height: 170px;
    border: 1px solid #bdbdbd;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 10px;
  }

  .loader {
  border: 12px solid #f3f3f3;
  border-radius: 50%;
  border-top: 12px solid #ff9800;
  width: 80px;
  height: 80px;
  -webkit-animation: spin 2s linear infinite; /* Safari */
  animation: spin 2s linear infinite;
}

/* Safari */
@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
<script>
import Navbar2 from '../components/Navbar.vue';
import Navbar from '../components/Navbar2.vue';
import { authenticationService } from '../utility/authenticationService';
import axios from 'axios';
export default {
    components: {
    Navbar,
    Navbar2
  },
  data() {
    return {
        userToken: authenticationService.getUserToken(),
        load: false,
        job: '',
        resume: '',
        expertise: ''
    };
  },
  methods: {
    search() {
        console.log("hey")
        this.load = true
        let config = {
    headers: {
    'Authorization': 'Bearer ' + authenticationService.getUserToken()
    }
    }
    axios.post('http://localhost:8000/api/employee/job-search',{alpha: 0.5, search_keywords: this.expertise} ,config)
    .then(res => {
        let data = res.data.splice(0, 30)
        console.log(data)
        this.load = false
        this.job = [...data]
    })
    }    
  }
}
</script>
