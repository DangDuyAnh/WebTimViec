<template>
<div class="register-container">
    <div class="khung-dang-ky">
        <h1 :style="{fontSize: '22px', fontWeight: 'bold', color: 'black', marginTop: '70px', marginBottom: '15px'}">
            Nhà tuyển dụng đăng ký
        </h1>
        <h1 :style="{fontSize: '16px', color: 'black', marginBottom: '30px'}">
            Tạo tài khoản đề tìm ứng viên và bắt đầu đăng việc ngay
        </h1>

        <input placeholder="Username" v-model="username"/>
        <input placeholder="Password" type="password" v-model="password"/>
        <h1 :style="{fontSize: '22px', fontWeight: 'bold', color: 'black', marginTop: '40px', marginBottom: '20px'}">
            Thông tin công ty
        </h1>
        <input placeholder="Tên công ty" v-model="companyName"/>
        <input placeholder="Email người tuyển dụng" v-model="email"/>
        <input placeholder="Mô tả Công ty" v-model="desc"/>
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
            <select v-model="city">
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
            <select :style="{width: '168px'}" v-model="quan">
                <option>
                    Chọn quận / huyện
                </option>
                <option v-if="city==='Hà Nội'">
                    Hai Bà Trưng
                </option>
                <option v-if="city==='Hà Nội'">
                    Hoàn Kiếm
                </option>
                <option v-if="city==='Hà Nội'">
                    Đống Đa
                </option>

                <option v-if="city==='Hồ Chí Minh'">
                    Quận 1
                </option>
                <option v-if="city==='Hồ Chí Minh'">
                    Quận 2
                </option>

            </select>
        </div>

        <input placeholder="Số nhà, phố, phường" v-model="address"/>

        <button @click="registerAdmin">Đăng ký ngay</button>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import {post} from '../../utility/api'
import { authenticationService } from '../../utility/authenticationService'
export default {
    data() {
        return{
            email: '',
            password: '',
            companyName: '',
            username: '',
            country: 'Việt Nam',
            province: '1',
            quan: 'Chọn quận / huyện',
            address: '',
            city: 'Chọn tỉnh / thành',
            desc: ''
        }
    }, 
    methods: {
        async registerAdmin() {
            if (this.city === 'Hồ Chí Minh') this.province === '2'
            else this.province === '1'
            let sendData = {name: this.companyName, 
            address: this.address + ' quận ' + this.quan + ' TP. ' + this.city, province_id: this.province,
            desc: this.desc}
            console.log(sendData)
            let res = await axios.post('http://localhost:8000/api/company/register', sendData)
            console.log(res.data.id)
            let company_id = res.data.id
            res = await axios.post('http://localhost:8000/api/user/register', {username: this.username, 
            password: this.password, email: this.email})
            console.log(res.data.access_token)
            let access_token = res.data.access_token
            let admin = res.data.user
            res = await post("/user/set-role", {role_id: '3', company_id: company_id}, access_token);
            authenticationService.loginAdmin(admin, access_token, company_id);
            window.location = '/admin'
        }
    }
}
</script>