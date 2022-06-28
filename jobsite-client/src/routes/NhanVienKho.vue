<template>
    <div class="box-header">
      <div class="logo-web">
        <h1 color="orange">
          <a class="logo-web" href="#">JOBSITE</a>
        </h1>
      </div>
      <form class="box-search">
        <input class="search-company" placeholder="Nhập tên vị trí, công ty, từ khóa">
        <select class="search-city" type="text" name="country" placeholder="Nhập tỉnh, thành phố" >
            <option value="HI">Hà Nội</option>
            <option value="CA">TP Hồ Chí Minh</option>
            <option value="NV">Hải Dương</option>
            <option value="OR">Hải Phòng</option>
            <option value="WA">Bắc Ninh</option>
            <option value="AZ">Đà Nẵng</option>
            <option value="CO">Nghệ An</option>
            <option value="ID">Thanh Hóa</option>
            <option value="MT">Quảng Ninh</option>
            <option value="NE">Thái Bình</option>
            <option value="NM">TT Huể</option>
            <option value="ND">Hà Tĩnh</option>
            <option value="UT">Thái Nguyên</option>
        </select>
        <button class="button-search">
          <span class="text-button">Tìm kiếm</span>
          <font-awesome-icon icon="magnifying-glass" class='input-icon2'/>
        </button>
      </form>
      <hr  width="100%"/>
    </div>
    <div class="box-body">
        <div class="container-if-company-0">
            <div class="pannel">
                <img src="https://dxwd4tssreb4w.cloudfront.net/web/images/default-banner.png" alt="">
            </div>
            <div class="info-company">
                <div class="logo-header">
                    <img class="logo-size" src="https://dxwd4tssreb4w.cloudfront.net/image/91c5b0f7f67e4ebc5f5377b27a157415" alt="">
                </div>
                <div class="info-detal-company">
                    <div class="name-company">
                        <strong><h2 id="job-name">NHÂN VIÊN KHO (Tiếng Trung cơ bản)</h2></strong>
                        <li id="company-name">Công Ty TNHH Cửu Tinh Việt Nam</li>
                        <strong><li id="salary">$ Thương lượng</li></strong>
                        <li id="location">Thị xã phú mỹ, Bà Rịa - Vũng tàu</li>
                        <div class="row-btn-save">
                            <button
                                :class="[isActive ? 'blue' : 'white']"
                                @click="toggle"
                                >{{isActive ? 'Lưu' : 'Đã lưu'}}</button>
                            <button id="send-cv">Nộp đơn</button>
                        </div>
                    </div>
                </div>
                <div class="meta-job">
                    <h3 :style="{color:'#0069DB'}">Mô tả công việc</h3>
                    <br/>
                    <p style="text-align: justify;">- Kiểm tra h&agrave;ng nhập: Số lượng v&agrave; chất lượng h&agrave;ng.</p>
                    <p style="text-align: justify;">- Xuất h&agrave;ng: theo đơn h&agrave;ng do bộ phận sản xuất cung cấp</p>
                    <p style="text-align: justify;">- Kiểm k&ecirc; h&agrave;ng h&oacute;a, lập b&aacute;o c&aacute;o v&agrave; chịu tr&aacute;ch nhiệm trước Ban gi&aacute;m đốc về việc xuất nhập tồn định kỳ cuối th&aacute;ng.</p>
                    <p style="text-align: justify;">- L&ecirc;n danh s&aacute;ch h&agrave;ng tồn kho định mức để kịp thời l&agrave;m đơn mua h&agrave;ng phục vụ sản xuất</p>
                    <p style="text-align: justify;">- C&aacute;c c&ocirc;ng việc kh&aacute;c được cấp tr&ecirc;n giao.</p>
                    <p style="text-align: justify;">- C&ocirc;ng việc cụ thể sẽ trao đổi th&ecirc;m khi phỏng vấn.</p>
                    <p style="text-align: justify;"><strong>* Quyền lợi:</strong></p>
                    <p style="text-align: justify;">- Hưởng đầy đủ quyền lợi BHXH, BHYT, BHTN theo luật lao động</p>
                    <p style="text-align: justify;">+ Mức đ&oacute;ng BHXH tuỳ vị tr&iacute;: c&ocirc;ng nh&acirc;n 6.000.000; Tổ trưởng 7.000.000; Nh&acirc;n vi&ecirc;n VP 9.000.000</p>
                    <p style="text-align: justify;">- Thưởng lễ : Giỗ tổ 10/3 AL, Giải ph&oacute;ng miền Nam v&agrave; Quốc tế LĐ 30/4-1/5&hellip;</p>
                    <p style="text-align: justify;">- Thưởng tết</p>
                    <p style="text-align: justify;">- Phụ cấp: suất ăn 30.000/bữa</p>
                    <p style="text-align: justify;">- Được tham dự c&aacute;c kh&oacute;a đ&agrave;o tạo nội bộ v&agrave; kh&oacute;a bồi dưỡng.</p>
                    <p style="text-align: justify;">- Được l&agrave;m việc trong m&ocirc;i trường chuy&ecirc;n nghiệp, s&aacute;ng tạo</p>
                    <br/>
                    <h3 :style="{color:'#0069DB'}">Kinh nghiệm / Kỹ năng chi tiết</h3>
                    <br/>
                    <p>- Kinh nghiệm 1 năm trở l&ecirc;n ở vị tr&iacute; tương đương</p>
                    <p>- Giao tiếp được tiếng Trung hoặc tiếng Trung cơ bản</p>
                    <p>- Biết vi t&iacute;nh văn ph&ograve;ng.</p>
                    <p>- L&agrave;m việc nhiệt t&igrave;nh, trung thực, năng động, hoạt b&aacute;t.</p>
                    <br/>
                    <h3 :style="{color:'#0069DB'}">Thông tin liên hệ</h3>
                    <br/>
                    <p>Tên liên hệ: <strong>Phòng Nhân Sự</strong> </p>
                    <p>Địa chỉ: KCN Mỹ xuân A2 , Thị xã Phú Mỹ , Bà Rịa - Vũng Tàu , Viet Nam</p>
                    <p> <strong>- Các ứng viên quan tâm vui lòng nộp hồ sơ trực tuyến qua hệ thống CareerLink, qua email hoặc nộp trực tiếp tại công ty.</strong> </p>
                    <p>Nhận hồ sơ bằng ngôn ngữ:<strong>Tiếng Việt</strong> </p>
                    <p><strong>Ngày đăng tuyển:</strong> 27-06-2022</p>
                    <p><strong>Ngày hết hạn:</strong> 27-07-2022</p>
                    <p></p>
                </div>
            </div>
        </div>
        <div class="container-if-company-1">
            <div id="info-content">
                <div id="logo-company">
                    <img id="logo-1" src="https://dxwd4tssreb4w.cloudfront.net/image/91c5b0f7f67e4ebc5f5377b27a157415" alt="">
                </div>
                <div id="name-1">
                    <span ><a href="#" :style="{color:'black'}"><strong>Công Ty TNHH Cửu <br/>Tinh Việt Nam</strong></a> </span>
                    <p></p>
                    <li>25-99 Nhân sự</li>
                    <p></p>
                    <li>Liên hệ: Phòng Nhân Sự</li>
                </div>
                <div id="meta-company">
                    <p><strong>Công Ty TNHH Cửu Tinh Việt Nam trực thuộc Tập Đoàn cổ phần khống chế Cửu Tinh Trung Quốc.Công ty chúng tôi có cơ sở sản xuất Công Ty TNHH Cửu Tinh Việt Nam thành lập từ năm 2013 trực thuộc Tập Đoàn cổ phần Cửu Tinh Trung Quốc</strong></p>
                </div>
            </div>
            <div class="job-company-df">
                <div id="job-df">
                    <h3>Việc làm cùng công ty</h3>
                    <hr width="95%">
                </div>
                <div class="list-job-df">
                    <div id="logo-company">
                    <img id="logo-1" src="https://dxwd4tssreb4w.cloudfront.net/image/91c5b0f7f67e4ebc5f5377b27a157415" alt="">
                </div>
                <div id="name-1">
                    <span ><a href="#" :style="{color:'black'}"><strong>TRỢ LÝ (BIẾT TIẾNG <br/> TRUNG)</strong></a> </span>
                    <p></p>
                    <li>Bà Rịa - Vũng Tàu</li>
                    <strong><li id="salary">$ Thương lượng</li></strong>
                </div>
                </div>
                <hr width="99%">
                <div class="list-job-df">
                    <div id="logo-company">
                    <img id="logo-1" src="https://dxwd4tssreb4w.cloudfront.net/image/91c5b0f7f67e4ebc5f5377b27a157415" alt="">
                </div>
                <div id="name-1">
                    <span ><a href="#" :style="{color:'black'}"><strong>KỸ SƯ IT</strong></a> </span>
                    <p></p>
                    <li>Bà Rịa - Vũng Tàu</li>
                    <strong><li id="salary">$ Thương lượng</li></strong>
                </div>
                </div>
                <hr width="99%">
                <div class="list-job-df">
                    <div id="logo-company">
                    <img id="logo-1" src="https://dxwd4tssreb4w.cloudfront.net/image/91c5b0f7f67e4ebc5f5377b27a157415" alt="">
                </div>
                <div id="name-1">
                    <span ><a href="#" :style="{color:'black'}"><strong>KIẾM TOÁN</strong></a> </span>
                    <p></p>
                    <li>Bà Rịa - Vũng Tàu</li>
                    <strong><li id="salary">$ Thương lượng</li></strong>
                </div>
                </div>
            </div>
        </div>
    </div>
        
    
</template>

<script>
export default {
  data() {
    return {
      isActive: false,
    };
  },
  methods: {
    toggle() {
      this.isActive = this.isActive ? false : true;
    },
  },
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
.input-icon2 {
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
.box-body {
    background-color:#FFFAFA;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
}
.container-if-company-0 {
    background-color: white;
    padding-top: 20px;
    margin-left: 300px;
    height: 2000px;
    width: 832px;
    padding-right: 10px;
}
.pannel {
    height: 165px;
}
.info-company {
    height: 250px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    
}
.logo-header {
    height: 100%;
    width: 200px;
}
.logo-size {
    padding: 40px 0 0 20px;
}
.info-detal-company {
    padding-top: 20px;
    
}
#job-name {
    color: #0069DB;
    font-weight: 1000;
    
}
#company-name {
    font-weight: 1000;
    
}
#salary {
    font-weight: 900;
    color: #0069DB;
    padding-top: 5px;
}
#location {
    padding-top: 5px;
    font-weight: 600;
}
.row-btn-save {
    padding-top: 30px;
    padding-left: 200px;
    text-align: center;
}
.blue {
    margin-right: 20px;
    height: 45px;
    width: 180px;
    border: 1px solid transparent;
    border-radius: 0.5rem;
    font-size: 18px;
    border-color: #0069DB;
    font-weight: 400;
    color: #0069DB;
}
.white {
    margin-right: 20px;
    height: 45px;
    width: 180px;
    border: 1px solid transparent;
    border-radius: 0.5rem;
    font-size: 18px;
    border-color: #0069DB;
    font-weight: 400;
    color: white;
    background-color:#87CEFA;
}
#send-cv{
    color: white;
    background-color: #0069DB;
    height: 45px;
    width: 180px;
    border: 1px solid transparent;
    border-radius: 0.5rem;
    font-size: 18px;
    border-color: #0069DB;
}
.meta-job {
    padding: 30px 0 0 30px;
    font-family: "Montserrat", sans-serif;
}
h3 {
    font-weight: 600;
}
p {
    font-size: 16px;
}
.container-if-company-1 {
    margin-left: 10px;
    width: 315px;
    background-color:#FFFAFA;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
}
#info-content {
    margin-top: 20px;
    background-color: white;
    width: 315px;
    height: 450px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
}
#logo-1 {
    height: 120px;
    padding: 50px 0 0 0px;
}
#name-1 {
    height: 120px;
    padding: 30px 0 0 15px;

}
#meta-company {
    padding: 0 20px 0 20px;
}
.job-company-df {
    margin-top: 20px;
    background-color: white;
    width: 315px;
    height: 550px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;

}
#job-df {
    padding: 20px 0 0 10px;
}
.list-job-df {
    width: 300px;
    height: 150px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
}
</style>