<script>
import Navbar2 from '../components/Navbar.vue';
import Navbar from '../components/Navbar2.vue';
import axios from 'axios';
import { authenticationService } from '../utility/authenticationService';
export default {
    components: {
    Navbar,
    Navbar2
  }, 
  data() {
    return {
      userToken: authenticationService.getUserToken()
    };
  },
};
</script>

<template>
    <Navbar v-if="userToken"/>
    <Navbar2 v-else/>

    <div class="da24-container" :style="{display: 'flex', justifyContent: 'center'}">

        <!-- <div :style="{display: 'flex', width: '1100px'}">
            <div class="da24-inner" :style="{width: '500px'}">
                <div class="da24-paper" :style="{height: 'auto'}">
                    <div :style="{width: '100%', display: 'flex', justifyContent: 'center', marginTop: '20px'}">
                        <h3 class="thong-tin-cua-ban">CV của bạn</h3>
                    </div>

                </div>
            </div>

            <div class="da24-inner" :style="{width: '500px'}">
            <div class="da24-paper" :style="{height: 'auto'}">
                <div :style="{width: '100%', display: 'flex', justifyContent: 'center', marginTop: '20px'}">
                    <h3 class="thong-tin-cua-ban">Thông tin của bạn</h3>
                </div>

                <p class="text-highlight" :style="{marginTop: '40px'}">
                    <strong>Thông tin cá nhân</strong>
                </p>

                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Họ và tên </label>
                    <div class="da24-gaga-col-sm-8">
                        <input type="text" name="fullname" class="form-control" value="Duy Anh Đặng">
                    </div>
                </div>
                
                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Số điện thoại</label>
                    <div class="da24-gaga-col-sm-8">
                        <input type="text" name="fullname" class="form-control" value="Duy Anh Đặng">
                    </div>
                </div>  

                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Email</label>
                    <div class="da24-gaga-col-sm-8">
                        <input type="text" name="fullname" class="form-control" value="Duy Anh Đặng">
                    </div>
                </div>  

                <p class="text-highlight">
                    <strong>MONG MUỐN CỦA BẠN</strong>
                </p>

                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Ngành nghề</label>
                    <div class="da24-gaga-col-sm-8">
                        <input type="text" name="fullname" class="form-control" value="Duy Anh Đặng">
                    </div>
                </div>  


                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Về bạn</label>
                    <div class="da24-gaga-col-sm-8">
                        <textarea class="form-control" name="note" rows="5" placeholder="Giới thiệu ngắn gọn về bản thân để giúp bạn tăng sức thu hút với nhà tuyển dụng. VD: Tôi có chuyên môn trong lĩnh vực Tự động hóa, mong muốn của tôi là tìm được một môi trường làm việc chuyên nghiệp, với chế độ đãi ngộ tốt."></textarea>
                    </div>
                </div>  

                <div class="da24-gaga-text-center">
                    <button type="submit" class="btn-da24-gaga-text-center">Cập nhật</button>
                </div>
                    
                    
            </div>
            </div>
        </div> -->

        <div class="da24-inner" :style="{width: '1000px'}">
            <div class="da24-paper" :style="{height: 'auto'}">
                <div :style="{width: '100%', display: 'flex', justifyContent: 'center', marginTop: '20px'}">
                    <h3 class="thong-tin-cua-ban">Thông tin của bạn</h3>
                </div>

                <p class="text-highlight" :style="{marginTop: '40px'}">
                    <strong>Thông tin cá nhân</strong>
                </p>

                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Họ và tên </label>
                    <div class="da24-gaga-col-sm-8">
                        <input type="text" name="fullname" class="form-control" value="Duy Anh Đặng">
                    </div>
                </div>
                
                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Số điện thoại</label>
                    <div class="da24-gaga-col-sm-8">
                        <input type="text" name="fullname" class="form-control" value="Duy Anh Đặng">
                    </div>
                </div>  

                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Email</label>
                    <div class="da24-gaga-col-sm-8">
                        <input type="text" name="fullname" class="form-control" value="Duy Anh Đặng">
                    </div>
                </div>  

                <p class="text-highlight">
                    <strong>MONG MUỐN CỦA BẠN</strong>
                </p>

                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Ngành nghề</label>
                    <div class="da24-gaga-col-sm-8">
                        <input type="text" name="fullname" class="form-control" value="Duy Anh Đặng">
                    </div>
                </div>  


                <div class="da24-gaga-form-group">
                    <label class="da24-gaga-control-label">Về bạn</label>
                    <div class="da24-gaga-col-sm-8">
                        <textarea class="form-control" name="note" rows="5" placeholder="Giới thiệu ngắn gọn về bản thân để giúp bạn tăng sức thu hút với nhà tuyển dụng. VD: Tôi có chuyên môn trong lĩnh vực Tự động hóa, mong muốn của tôi là tìm được một môi trường làm việc chuyên nghiệp, với chế độ đãi ngộ tốt."></textarea>
                    </div>
                </div>  

                <div class="da24-gaga-text-center">
                    <button type="submit" class="btn-da24-gaga-text-center">Cập nhật</button>
                </div>
                    
                    
            </div>
        </div>
    </div>
</template>

<style>

</style>