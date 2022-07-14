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
      pdf : [],
      nowPDF: 0,
      mainCV: 1,
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
    axios.get('http://localhost:8000/api/employee/cv-list', config)
        .then(res => {
          this.nowPDF = res.data.length
          let array = []
          res.data.forEach(item => array.push(item.cv_id))
          this.pdf = [...array]
    })
  },
  methods: {
    addCV() {
        let config = {
        headers: {
        'Authorization': 'Bearer ' + authenticationService.getUserToken()
        }
        }
        axios.post('http://localhost:8000/api/employee/add-cv', {cv_id: String(this.nowPDF + 1)}, config)
        .then(res => {
          console.log(res.data)
          console.log('DA dep trai')
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
          <h1>CV đã tải lên</h1>
          <input @change="addCV" type='file' id='file' accept=".pdf" :style="{display: 'none'}"/>
          <label for='file'>Tải mới</label>
        </div>

        <div class="image-CV-list">
            <div class="image-CV" v-for="(item, index) in pdf">
              <img src='../assets/CV1.png' v-if="index === 0"/>
              <img src='../assets/CV1.png' v-if="index === 1"/>
              <img src='../assets/CV1.png' v-if="index === 2"/>
              <div class="CV-inner">
              <div class="dat-lam-cv">
              <button>Đặt làm CV chính</button>
              <font-awesome-icon icon="star" :style="{color: 'yellow', fontSize: '18px'}"/>
              </div>
              <p class="tieu-de">Tiêu đề 1</p>
              <font-awesome-icon icon="trash" class='trash'/>
              </div>
            </div>
            <div class="image-CV">
              <img src='../assets/CV2.png'/>
              <div class="CV-inner">
              <div class="dat-lam-cv">
              <button>Đặt làm CV chính</button>
              </div>
              <div :style="{clear: 'both'}"></div>
              <p class="tieu-de">Tiêu đề 1</p>
              <font-awesome-icon icon="trash" class='trash'/>
              </div>
            </div>
            <div class="image-CV">
              <img src='../assets/CV3.png'/>
              <div class="CV-inner">
              <div class="dat-lam-cv">
              <button>Đặt làm CV chính</button>
              </div>
              <div :style="{clear: 'both'}"></div>
              <p class="tieu-de">Tiêu đề 1</p>
              <font-awesome-icon icon="trash" class='trash'/>
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