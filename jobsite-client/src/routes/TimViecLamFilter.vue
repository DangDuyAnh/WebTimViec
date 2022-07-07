<template>
    <Navbar v-if="userToken"/>
    <Navbar2 v-else/>
  <div>
    <div class="box-header">
      <div class="logo-web">
      </div>
      <form class="box-search">
        <input class="search-company" placeholder="Nhập tên vị trí, công ty, từ khóa" v-model="ten">
        <select class="search-city">
          <option>--Chọn tên tỉnh, thành phố--</option>
					<option>Hà Nội</option>
					<option>TP Hồ Chí Minh</option>
					<option>Hải Dương</option>
					<option>Hải Phòng</option>
          <option>Bắc Ninh</option>
          <option>Đà Nẵng</option>
          <option>Nghệ An</option>
          <option>Thanh Hóa</option>
          <option>Quảng Ninh</option>
          <option>Thái Bình</option>
          <option>TT Huể</option>
          <option>Hà Tĩnh</option>
          <option>Thái Nguyên</option>
        </select>
        <button class="button-search">
          <span class="text-button">Tìm kiếm</span>
          <font-awesome-icon icon="magnifying-glass" class='input-icon'/>
        </button>
      </form>
      <div class="box-user"></div>

    </div>
    <div class="box-buttonjob">
      <div class="list-button" >
        <select class="btn-job" v-model="nganh">
          <option>Ngành nghề</option>
          <option>BỘ PHẬN HỖ TRỢ</option>
          <option>Kế toán</option>
          <option>KHÁCH SẠN DU LỊCH</option>
          <option>DỊCH VỤ</option>
          <option>SẢN XUẤT</option>
          <option>KỸ THUẬT</option>
          <option>GIAO DỊCH KHÁCH HÀNG</option>
          <option>IT - CÔNG NGHỆ THÔNG TIN</option>
          <option>XÂY DỰNG / BẤT ĐỘNG SẢN</option>
        </select>
        <select class="btn-job" v-model="cap">
          <option>Cấp bậc</option>
                                                <option>Fresher</option>
                                                <option>Giám đốc</option>
                                                <option>Nhân viên</option>
                                                <option>Project Manager</option>
                                                <option>Thực tập sinh</option>
                                                <option>Trưởng phòng</option>
                                                <option>Sennior</option>
        </select>
        <select class="btn-job" v-model="kinhNghiem">
          <option>Kinh nghiệm</option>
                                                <option>Không cần kinh nghiệm</option>
                                                <option>Dưới 1 năm</option>
                                                <option>Từ 1 - 3 năm</option>
                                                <option>> 5 năm</option>
        </select>
        <select class="btn-job">
          <option>Mức lương</option>
          <option>Trên 5 triệu</option>
          <option>Trên 10 triệu</option>
          <option>Trên 15 triệu</option>
          <option>Trên 20 triệu</option>
          <option>Trên 30 triệu</option>
        </select>
        <select class="btn-job">
          <option>Học vấn</option>
          <option>Trung cấp</option>
          <option>Cao đẳng</option>
          <option>Đại học</option>
          <option>Không yêu cầu</option>
        </select>
        <select class="btn-job" v-model="hinhThuc">
          <option>Hình thức</option>
                                                <option>Offline</option>
                                                <option>Remote</option>
        </select>
      </div>
      <button class="button-search" @click="search">Bộ Lọc</button>
    </div>
    <div class="content-job">
      <div class="row-content-1">
        <h4>
          <strong>Danh sách các công việc phù hợp</strong>
        </h4>
        <h7>
          {{list.length}} việc làm sẵn có
        </h7>
      </div>
      <div class="job-detail" v-for="(item, index) in list" :style="{cursor: 'pointer'}">
        <div class="logo-company">
            <img  class="logo-company-0" src="https://dxwd4tssreb4w.cloudfront.net/image/91c5b0f7f67e4ebc5f5377b27a157415" alt="">
        </div>
        <div class="row-if-job" @click="moveTo(item.id)">
            <h3 class="row-name-job">{{item.title}}</h3>
            <li>Company {{index+1}}</li> 
            <li>{{item.public_date}} - {{item.expired_date}}</li>
            <li>{{item.field}}</li>
        </div>
        <div class="row-if-job-1">
          <li>Vị trí: {{item.position}}</li>
          <li>Kinh nghiệm: {{item.required_experience}}</li>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { authenticationService } from '../utility/authenticationService';
import Navbar2 from '../components/Navbar.vue';
import Navbar from '../components/Navbar2.vue';
export default {
    components: {
    Navbar,
    Navbar2
  },
  data() {
    return {
      ten: '',
      nganh: 'Ngành nghề',
      cap: 'Cấp bậc',
      kinhNghiem: 'Kinh nghiệm',
      hinhThuc: 'Hình thức',
      queryTen: this.$route.query.ten,
      queryNganh: this.$route.query.nganh,
      queryCap: this.$route.query.cap,
      queryKinhNghiem: this.$route.query.kinhNghiem,
      queryHinhThuc: this.$route.query.hinhThuc,
      list: [],
      userToken: authenticationService.getUserToken()
    };
  },
  methods: {
    toggle() {
      this.isActive = this.isActive ? false : true;
      
    },
    moveTo(id) {
      window.location = '/tim-viec-lam/detail/' + id
    },
    search () {
          let s = ''
    if (this.ten !== '') s += 'ten=' + this.ten + '&'
    if (this.nganh !== 'Ngành nghề') s += 'nganh=' + this.nganh + '&'
    if (this.cap !== 'Cấp bậc') s+= 'cap=' + this.cap + '&'
    if (this.hinhThuc !== 'Hình thức') s+= 'hinhThuc=' + this.hinhThuc + '&'
    if (this.kinhNghiem !== 'Kinh nghiệm') s+= 'kinhNghiem=' + this.kinhNghiem + '&' 
    window.location = '/tim-viec-lam-filter?' + s
    }

  },
  mounted() {

    let config = {
        headers: {
        'Authorization': 'Bearer ' + authenticationService.getUserToken()
        }
    }
    let s = ''
    if (this.queryTen) s += 'title=' + this.queryTen + '&'
    if (this.queryNganh) s += 'field=' + this.queryNganh + '&'
    if (this.queryCap) s+= 'position=' + this.queryCap + '&'
    if (this.queryHinhThuc) s+= 'type=' + this.queryHinhThuc + '&'
    if (this.queryKinhNghiem) s+= 'required_experience=' + this.queryKinhNghiem + '&' 
    if (s !== '') {
    axios.get('http://localhost:8000/api/job/filter?' + s, config)
    .then(data => {
      let temp = data.data
      this.list = [...temp]
    })
    } else {
    axios.get('http://localhost:8000/api/job/list' , config)
    .then(data => {
      let temp = data.data
      this.list = [...temp]
    })
    }
  }
};

</script>

<style>
.box-header {
  margin-top: 0px;
  height: 57px;
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;

}
hr {
  margin: 0 0 0 0;
}
.logo-web {
  height: 55px;
  width: 200px;
  display: block;
  text-align: center;
  color: orange;
  align-items: center;
  padding-top: 4px;
}
.box-search {
  padding-left: 100px;
  height: 57px;
  width: 900px;
  padding-top: 8px;
}
input,select {
  height: 38px;
  box-sizing: border-box;
  width: 300px;
  font-family: inherit;
}
.button-search {
  height: 38px;
  width: 110px;
  box-sizing: border-box;
  margin-left: 15px;
  border: 1px solid transparent;
  color: white;
  background-color: #0069DB;
  text-align: center;
  flex-wrap: wrap;
  flex-direction: row;
  border-radius: 0.25rem;
  font-family: inherit;
}
.input-icon {
  margin-top: 2px;
  padding-left: 0px;
  padding-right: 85px;
}
.text-button {
  box-sizing: border-box;
  padding-left: 17px;
  font-size: 1rem;
}
.search-city, .search-company {
  padding-left: 15px;
  border-radius: 0.25rem;
  border: 1px solid #ced4da;
  font-size: 1rem;
}
.search-city {
  margin-left: 10px;
}
.box-buttonjob {
  margin-top: 0px;
  height: 57px;
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  display: inline block;
  align-items: center;
  padding-left: 300px;

}
.row-content-1 {
    padding-top: 30px;
    
}
.job-detail {
    width: 1000px;
    height: 141px;
    border: 1px ridge #DCDCDC;
    border-radius: 1rem;
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    display: inline block;
}
.logo-company {
    height: 100%;
    width: 150px;
}
.logo-company-0 {
    padding-top: 20px;
}
.row-if-job {
    width: 470px;
    padding-top: 15px;
    padding-left: 30px;
}
.row-if-job-1 {
    width: 300px;
    padding-top: 50px;
    
}
.row-name-job {
    color: red;
}
.unsave{
    background-color: white;
    border: #DCDCDC;
    color: #0069DB;
    margin-left: 260px;
    width: 70px;
    padding-top: 15px;
}
.save{
    background-color: white;
    border: #DCDCDC;
    color: #0069DB;
    margin-left: 260px;
    width: 70px;
    padding-top: 15px;
}
</style>