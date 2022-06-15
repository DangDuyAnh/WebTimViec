<template>
    <div class="Navbar">

        <div class="Navbar-inner">
            <a class="Home">
                Home
            </a>

            <ul class='Navbar-tab'>
                <li class="Navbar-dropdown">
                    <a class="Navbar-dropbtn">Việc làm</a>
                    <div class="dropdown-content">
                        <div class="dropdown-line">
                            <font-awesome-icon icon="magnifying-glass" class='dropdown-icon'/>
                            <a class="dropdown-line-a">Tìm việc làm</a>
                        </div>
                        <div class="dropdown-line">
                            <font-awesome-icon icon="floppy-disk" class='dropdown-icon'/>
                            <a class="dropdown-line-a">Việc làm đã lưu</a>
                        </div>
                        <div class="dropdown-line">
                            <font-awesome-icon icon="share-from-square" class='dropdown-icon'/>
                            <a class="dropdown-line-a">Việc làm đã ứng tuyển</a>
                        </div>
                    </div>
                </li>

                <li class="Navbar-dropdown">
                    <a class="Navbar-dropbtn">Hồ sơ & CV</a>
                        <div class="dropdown-content">
                            <div class="dropdown-line">
                                <font-awesome-icon icon="id-badge" class='dropdown-icon'/>
                                <a class="dropdown-line-a">Quản lý CV</a>
                            </div>
                            <div class="dropdown-line">
                                <font-awesome-icon icon="envelope-open-text" class='dropdown-icon'/>
                                <a class="dropdown-line-a">Thư xin việc</a>
                            </div>
                        </div>
                </li>

                <li class="Navbar-dropdown">
                    <a class="Navbar-dropbtn">Công ty</a>
                </li>          
            </ul>
        </div>

        <div :style="{marginRight: '22px'}">
            <button class="navbar-button" :style="{backgroundColor: 'white', border: '1px solid #e65100', color: '#e65100' }">Đăng nhập</button>
            <button class="navbar-button" :style="{backgroundColor: '#e65100', border: '1px solid #e65100', color: 'white'}">Đăng ký</button>
            <button class="navbar-button" :style="{backgroundColor: 'black', border: '1px solid black', color: 'white'}">Nhà tuyển dụng</button>
        </div>
    </div>
</template>

<style>
.Navbar {
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #eeeeee;
}

.Navbar-inner{
    display: flex;
    align-items: center;
}

.Home {
    margin: 0px 30px;
    cursor: pointer;
    text-decoration: none;
    padding: 0;
    font-size: 50px;
    font-weight: 700;
    color: #ff7b00;
}

.Home:hover {
    color: #ff7b00;
}

.Navbar-tab {
    list-style-type: none;
    margin: 0px;
    padding: 0px;
    position: relative;
}

.Navbar-tab li {
    float: left
}

.Navbar-dropdown {
    display: block;
    border-radius: 5px;
    margin: 0px 5px;
}

.Navbar-tab a, .Navbar-dropbtn {
    cursor: pointer;
    display: block;
    color: black;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    font-weight: 600;
    padding: 15px 15px;
  }

.Navbar-tab a:hover, .Navbar-dropdown:hover .Navbar-dropbtn {
    color: #ff7b00;
}

.Navbar-dropdown:hover {
    background-color: #f5f5f5;
    cursor: pointer;
}

.dropdown-content {
    position: absolute;
    display: none;
    z-index: 2;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    background-color: white;
    left: 0px;
    border-radius: 5px;
    padding: 14px;
}

.dropdown-content a{
    text-align: left;
    padding: 10px 15px;
    text-decoration: none;
    font-size: 15px;
    font-weight: 450;
    border-radius: 5px;
}

.Navbar-dropdown:hover .dropdown-content {
    display: block;
  }

.dropdown-line {
    display: flex;
    align-items: center;
    min-width: 300px;
    background-color: #fafafa;
    border-bottom: 1px solid #eeeeee;
}

.dropdown-line:hover{
    background-color: #f5f5f5;
}

.dropdown-line:hover .dropdown-line-a {
    color: #ff7b00;
}

.dropdown-icon {
    color: #ff7b00;
    margin-left: 15px;
}

.navbar-button {
    font-weight: 600;
    padding: 13px 15px;
    font-size: 15px;
    border-radius: 6px;
    cursor: pointer;
    margin: 4px 4px;
    opacity: 0.8
}

.navbar-button:hover {
    opacity: 1;
}
</style>