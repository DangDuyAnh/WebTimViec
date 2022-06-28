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
          <font-awesome-icon icon="magnifying-glass" class='input-icon'/>
        </button>
      </form>
      
    </div>
    <hr  width="100%"/>
    <div class="tag-btn">
        <div class="box-btn-function">
            <button class="btn-function">
                <font-awesome-icon icon="floppy-disk" class='dropdownout-icon'/>
                <a href="/viec-da-luu"><span :style="{color: 'gray'}">Việc đã lưu</span></a>
            </button>
            <button class="btn-function1">
                <font-awesome-icon icon="share-from-square" class='dropdownout-icon'/>
                <a href="/viec-da-ung-tuyen"><span :style="{color: 'gray'}">Việc đã ứng tuyển</span></a>
            </button>
        </div>
    </div>
    <hr  width="100%"/>
    <div class="container-list-job">
        <div id="title-page">
            <h3>Việc đã lưu (1)</h3>
        </div>
        <div class="list-job-submit">
            <hr  width="100%"/>
            <img id="logo-2" src="https://dxwd4tssreb4w.cloudfront.net/image/91c5b0f7f67e4ebc5f5377b27a157415" alt="">
            <div class="if-job-save">
                <a href="/tim-viec-lam/nhan-vien-kho"><h4 id="namejob">NHÂN VIÊN KHO (Tiếng Trung cơ bản)</h4></a>
                <li>Công Ty TNHH Cửu Tinh Việt Nam</li>
            </div>
            <button id="delete-job">
                <font-awesome-icon icon="xmark" class='icon-delete'/>
            </button>
            <button id="send-cv-1">
                <font-awesome-icon icon="share-from-square" :style="{color:'white'}" class='icon-send-cv'/>
            </button>
        </div>
        <hr  width="100%"/>
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
.tag-btn {
    margin-top: 0px;
    height: 57px;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
}
.box-btn-function {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    padding: 0 300px 0 300px;
    background-color: #FFFAFA;
    
}
.btn-function, .btn-function1 {
    border: 0px  #ced4da;
    margin-left: 30px;
    background-color: #FFFAFA;
    font-size: 1rem;
    color: gray;
}
.btn-function1 {
    margin-left: 200px;
}
.dropdownout-icon {
    padding-right: 9px;
}
button:focus {outline:0;}
.container-list-job {
    height: 700px;
    width: 1000px;
    margin-left: 300px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    
}
#title-page {
    padding-top: 50px;
}
#logo-empty {
    height: 100px;
    padding: 10px 0 0 450px;
}
#text-empty {
    padding-top: 20px;
    text-align: center;
    font-weight: 900;
    font-size: 20px;
}
#btn-empty {
    margin: 10px 0 0 400px;
    color: white;
    background-color: #0069DB;
    width: 185px;
    height: 35px;
    border: 1px solid;
    border-radius: 1rem;
}
.list-job-submit {
    margin-top: 20px;
    width: 100%;
    height: 82px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
}
#logo-2 {
    padding-top: 5px;
    height: 70px;
}
.if-job-save {
    padding: 15px 0 0 15px;
    height: 82px;
}
#namejob {
    font-weight: 800;
    color: black;
}
#delete-job {
    margin-top: 20px;
    margin-left: 420px;
    width: 40px;
    height: 40px;
    border-radius: 99rem;
    background-color: white;
    border: 1px solid white;
}
.icon-delete {
    padding-top: 2px;
    height: 20px;
    color: black;
    align-items: center;
}
#send-cv-1 {
    margin-top: 20px;
    margin-left: 30px;
    width: 40px;
    height: 40px;
    border-radius: 99rem;
    background-color: #0069DB;
    border: 1px solid white;
}

</style>