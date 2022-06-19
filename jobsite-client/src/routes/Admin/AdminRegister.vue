<template>
<div class="register-container">
    <div class="khung-dang-ky">
        <h1 :style="{fontSize: '22px', fontWeight: 'bold', color: 'black', marginTop: '70px', marginBottom: '15px'}">
            Nhà tuyển dụng đăng ký
        </h1>
        <h1 :style="{fontSize: '16px', color: 'black', marginBottom: '30px'}">
            Tạo tài khoản đề tìm ứng viên và bắt đầu đăng việc ngay
        </h1>

        <input placeholder="Email"/>
        <input placeholder="Mật khẩu" type="password"/>
        <h1 :style="{fontSize: '22px', fontWeight: 'bold', color: 'black', marginTop: '40px', marginBottom: '20px'}">
            Thông tin công ty
        </h1>
        <input placeholder="Tên công ty"/>
        <input placeholder="Người liên hệ"/>

        <div :style="{width: '500px'}">
            <h1 :style="{fontSize: '17px', fontWeight: 'bold', color: 'black', marginBottom: '10px'}">Địa chỉ</h1>
        </div>
        
        <div :style="{display:'flex'}">
            <select>
                <option>
                    Việt Nam
                </option>
                <option>
                    Hàn Quốc
                </option>
            </select>
            <select>
                <option>
                    Chọn tỉnh / thành
                </option>
                <option>
                    Hà Nội
                </option>
                <option>
                    Hồ Chí Minh
                </option>
            </select>
            <select :style="{width: '168px'}">
                <option>
                    Chọn quận / huyện
                </option>
                <option>
                    Hai Bà Trưng
                </option>
            </select>
        </div>

        <input placeholder="Số nhà, phố, phường"/>

        <button>Đăng ký ngay</button>
    </div>
</div>
</template>