<script>
import Navbar from '../components/Navbar.vue';
export default {
  components: {
    Navbar
  },
  data() {
    return {
      pdf : ['']
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
          <input type='file' id='file' accept=".pdf" :style="{display: 'none'}"/>
          <label for='file'>Tải mới</label>
        </div>

        <div class="image-CV-list">
            <div class="image-CV">
              <img src='../assets/Letter1.png'/>
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
              <img src='../assets/Letter2.png'/>
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
              <img src='../assets/Letter3.png'/>
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