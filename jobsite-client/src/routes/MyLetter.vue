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
      pdf : [],
      nowPDF: 0,
      mainCV: -1,
    }
  },
  mounted(){
    console.log('user')
    console.log(authenticationService.getUser())
    let config = {
    headers: {
    'Authorization': 'Bearer ' + authenticationService.getUserToken()
    }
    }
    axios.get('http://localhost:8000/api/employee/letter-list', config)
        .then(res => {
          this.nowPDF = res.data.length
          let array = []
          res.data.forEach(item => array.push(item.letter_id))
          this.pdf = [...array]
    })
    axios.get('http://localhost:8000/api/employee/self-profile', config)
      .then(res => {
        if (res.data.main_letter_id === null || res.data.main_letter_id === undefined) {
          this.mainCV = -1;
          console.log('yes')
          }
        else { 
          this.mainCV = res.data.main_letter_id;
          console.log('no')
          console.log(res.data.main_letter_id)
        }
      })
  },
  methods: {
    addCV() {
        let config = {
        headers: {
        'Authorization': 'Bearer ' + authenticationService.getUserToken()
        }
        }
        axios.post('http://localhost:8000/api/employee/add-letter', {letter_id: String(this.nowPDF)}, config)
        .then(res => {
          console.log(res)
          this.pdf = [...this.pdf, this.nowPDF]
          this.nowPDF += 1
        })
    },
    setMainCV(id) {
        let config = {
        headers: {
        'Authorization': 'Bearer ' + authenticationService.getUserToken()
        }
        }
        axios.post('http://localhost:8000/api/employee/set-main-letter', {letter_id: id}, config)
        .then(res => {
          this.mainCV = id
        })
    },
    deleteM(id) {
         let config = {
        headers: {
        'Authorization': 'Bearer ' + authenticationService.getUserToken()
        }
        }
        axios.post('http://localhost:8000/api/employee/remove-letter', {letter_id: id}, config)
        .then(res => {
          let array = this.pdf.filter(item => item !== id)
          this.pdf = [...array]
        })     
    }
  }
}
</script>

<template>
    <Navbar />
    <div class="container-cv">
      <div class="boxwhite-cv">
        <div class="cv-da-tai">
          <h1>Thư xin việc đã tải lên</h1>
          <input @change="addCV" type='file' id='file' accept=".pdf" :style="{display: 'none'}"/>
          <label for='file'>Tải mới</label>
        </div>

        <div class="image-CV-list">
            <div class="image-CV" v-for="(item, index) in pdf">
              <img src='../assets/Letter1.png' v-if="item === 0"/>
              <img src='../assets/Letter2.png' v-if="item === 1"/>
              <img src='../assets/Letter3.png' v-if="item === 2"/>
              <div class="CV-inner">
              <div class="dat-lam-cv" v-if="mainCV === item">
              <button :style="{visibility: 'hidden'}">Đặt làm Thư xin việc chính</button>
              <font-awesome-icon icon="star" :style="{color: 'yellow', fontSize: '18px'}"/>
              </div>
              <div class="dat-lam-cv" v-else>
              <button @click="setMainCV(item)">Đặt làm Thư xin việc chính</button>
              </div>
              <p class="tieu-de">CV {{item + 1}}</p>
              <font-awesome-icon icon="trash" class='trash' @click="deleteM(item)" v-if="mainCV != item"/>
              </div>
            </div>
            
        </div>
      </div>
    </div>


</template>

<script>
  
</script>
<style>
@import './index.css';
</style>