<script>
import {post} from '../../utility/api'
import { authenticationService } from '../../utility/authenticationService'
import axios from 'axios'
export default {
    data() {
        return {
        username: '',
        password: '',
        email: ''
        }
    },
    methods: {
        async send() {
            // const data =  post("/user/register", {username: this.username, password: this.password, email: this.email});
            // authenticationService.login(data.user, data.access_token)
            // window.location = '/';
            let res = await axios.post('http://localhost:8000/api/user/register', {username: this.username, password: this.password, email: this.email})
            let access_token = res.data.access_token
            let user = res.data.user
            res = await post("/user/set-role", {role_id: '2'}, access_token);
            authenticationService.login(user, access_token);
            window.location = '/'
        },
    }
}
</script>

<template>
    <div class="jobsite">
        <div class="container-login">
            <div class="content-center">
                <div class="form-login">
                    <div class="title">Tạo tài khoản</div>
                    <div class="input-account">
                        <div class="form-fields">
                            <input v-model="username" id="username" name="user" type="text" placeholder="Nhập tài khoản">
                        </div>
                        <div class="form-fields">
                            <input v-model="email" id="email" name="email" type="email" placeholder="Địa chỉ email">
                        </div>
                        <div class="form-fields">
                            <input v-model="password" id="password" name="password" type="password" placeholder="Nhập mật khẩu">
                        </div>
                    </div>
                    <div class="form-fields">
                        <button class="login" name="commit" type="submit" @click="send">
                            Đăng kí
                        </button>
                    </div>
                    <div class="sigin">
                        <a href="/dang-nhap">Đã có tài khoản</a>
                    </div>
                    <div class="login-choice"><span>Đăng nhập bằng</span></div>
                    <div class="signup-buttons">
                        <div id="fb-root"></div>
                        <a href="#" class="google-signup" >
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><title>Google</title><g fill="none" fill-rule="evenodd"><path fill="#4285F4" d="M17.64 9.2045c0-.6381-.0573-1.2518-.1636-1.8409H9v3.4814h4.8436c-.2086 1.125-.8427 2.0782-1.7959 2.7164v2.2581h2.9087c1.7018-1.5668 2.6836-3.874 2.6836-6.615z"></path><path fill="#34A853" d="M9 18c2.43 0 4.4673-.806 5.9564-2.1805l-2.9087-2.2581c-.8059.54-1.8368.859-3.0477.859-2.344 0-4.3282-1.5831-5.036-3.7104H.9574v2.3318C2.4382 15.9832 5.4818 18 9 18z"></path><path fill="#FBBC05" d="M3.964 10.71c-.18-.54-.2822-1.1168-.2822-1.71s.1023-1.17.2823-1.71V4.9582H.9573A8.9965 8.9965 0 0 0 0 9c0 1.4523.3477 2.8268.9573 4.0418L3.964 10.71z"></path><path fill="#EA4335" d="M9 3.5795c1.3214 0 2.5077.4541 3.4405 1.346l2.5813-2.5814C13.4632.8918 11.426 0 9 0 5.4818 0 2.4382 2.0168.9573 4.9582L3.964 7.29C4.6718 5.1627 6.6559 3.5795 9 3.5795z"></path></g></svg>
                            Google
                        </a>
                        <a href="#" class="facebook-signup">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="#3578E5"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/></svg>
                            Facebook
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style >
@import './style.css';
</style>

