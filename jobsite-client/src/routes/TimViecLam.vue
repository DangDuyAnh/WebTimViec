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
      <div class="title-content-job">
        <h1>
          <strong>Tìm Kiếm Việc làm Nhanh</strong>
        </h1>
        <h5>
          <a href="#">Việc làm hấp dẫn</a> | <a href="#">Việc làm cao cấp</a> | <a href="#">Việc làm tuyển gấp</a>
        </h5>
      </div>
      <div class="title-content-job">
        <h3>
          <strong>Tìm Kiếm Việc làm theo ngành nghề</strong>
        </h3>
        <hr  width="1000px"/>
      </div>
      <div class="box-list-job" >
        <div class="box-job-0">
          <h6>BỘ PHẬN HỖ TRỢ</h6>
          <li class="text-body"><a class="text-body" href="/tim-viec-lam/phien-dich-vien">Phiên dịch viên</a></li>
          <li class="text-body" href="#">Nhân sự</li>
          <li class="text-body" href="#">Thư kí</li>
          <li class="text-body" href="#">Pháp lý</li>
        </div>
        <div class="box-job-1">
          <h6>TÀI CHÍNH KẾ TOÁN</h6>
          <li class="text-body" href="#">Kế toán</li>
          <li class="text-body" href="#">Kiếm toán</li>
          <li class="text-body" href="#">Quản lý quỹ</li>
        </div>
        <div class="box-job-2">
          <H6>KHÁCH SẠN DU LỊCH</H6>
          <li class="text-body" href="#">Du lịch</li>
          <li class="text-body" href="#">Hướng dẫn viên</li>
          <li class="text-body" href="#">Tiếp tân</li>
          <li class="text-body" href="#">Quản lý nhân sự</li>
        </div>
        <div class="box-job-3">
          <h6>DỊCH VỤ</h6>
          <li class="text-body" href="#">An Ninh / Bảo Vệ</li>
          <li class="text-body" href="#">Dịch vụ chăm sóc khách hàng</li>
          <li class="text-body" href="#">Giáo dục / Đào tạo / Thư viện</li>
          <li class="text-body" href="#">Chăm sóc sức khỏe / Y tế</li>
          <li class="text-body" href="#">Bán lẻ / Bán sỉ </li>
        </div>
        <div class="box-job-4">
          <h6>SẢN XUẤT</h6>
          <li class="text-body">An Toàn Lao Động</li>
          <li class="text-body">Dầu khí / Khoáng sản</li>
          <li class="text-body">Dệt may / Da giày</li>
          <li class="text-body">Đồ Gỗ</li>
          <li class="text-body">Hóa chất / Sinh hóa / Thực phẩm</li>
          <li class="text-body">Nông nghiệp / Lâm nghiệp</li>
        </div>
        <div class="box-job-5">
          <h6>KỸ THUẬT</h6>
          <li class="text-body">Bảo trì / Sửa chữa</li>
          <li class="text-body">Điện lạnh / Nhiệt lạnh</li>
          <li class="text-body">Dược / Sinh học</li>
          <li class="text-body">Điện / Điện tử</li>
          <li class="text-body">Kỹ thuật ứng dụng / Cơ khí</li>
          <li class="text-body">Môi trường / Xử lý chất thải</li>
        </div>
        <div class="box-job-6">
          <h6>GIAO DỊCH KHÁCH HÀNG</h6>
          <li class="text-body">Bán hàng / Kinh doanh</li>
          <li class="text-body">Quảng cáo / Khuyến mãi / Đối ngoại</li>
          <li class="text-body">Thời trang</li>
          <li class="text-body">Tiếp thị</li>
        </div>
        <div class="box-job-7">
          <h6>IT - CÔNG NGHỆ THÔNG TIN</h6>
          <li class="text-body">CNTT - Phần cứng / Mạng</li>
          <li class="text-body">CNTT - Phần mềm</li>
        </div>
        <div class="box-job-8">
          <h6>XÂY DỰNG / BẤT ĐỘNG SẢN</h6>
          <li class="text-body">Bất động sản</li>
          <li class="text-body">Kiến trúc</li>
          <li class="text-body">Nội thất / Ngoại thất</li>
        </div>
      </div>
      
    </div>
  </div>
</template>

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
  height: 60px;
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

}
.box-buttonjob {
  display: inline block;
  align-items: center;
  padding-left: 300px;
}
.btn-job {
 margin-left: 20px;
 width: 120px;
 border-radius: 30px;
 text-align: center;
 font-size: 14px;
 
}
.content-job {
  height: 900px;
  margin: 0 300px 0 300px;
  
}
.title-content-job {
  padding-top: 50px;
  font-weight: 900;
}
.box-list-job {
  width: 1000px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
}
.box-job-0, .box-job-1,.box-job-2, .box-job-3, .box-job-4,
.box-job-5, .box-job-6, .box-job-7, .box-job-8, .box-job-9 {
  margin: 10px;
  display: inline-block;
  width: 300px;
} 
h6 {
  font-size: 1.2rem;
  color: #0069DB;
}
.text-body {
  cursor: pointer;
  color: black;
  text-decoration: none;
  border: 1rem;
  font-size: 1rem;
  margin-top: 5px;
}
</style>


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
    axios.get('http://localhost:8000/api/job/include?' + s, config)
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