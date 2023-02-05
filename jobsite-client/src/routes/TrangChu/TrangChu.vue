<script>
import Navbar2 from '../../components/Navbar.vue';
import Navbar from '../../components/Navbar2.vue';
import Chatbot from '../../components/Chatbot.vue';
import { authenticationService } from '../../utility/authenticationService';
export default {
  components: {
    Navbar,
    Navbar2,
    Chatbot
  },
  data() {
    return {
      index: 0,
      congViec: '',
      diaDiem: '',
      userToken: authenticationService.getUserToken(),
      testData: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    }
  }, 
    methods: {
        increment() {
            this.index++
        },
        decrement() {
		    this.index--
		},
        search() {
            window.location = '/tim-viec-lam-filter?ten=' + this.congViec 
        },
        goByTag (tag) {
            window.location = '/tim-viec-lam-filter?nganh=' + tag
        },
        check() {
            if (this.userToken) return 1;
            else return 0;
        }
    },
}
</script>

<template>
    <Navbar v-if="userToken"/>
    <Navbar2 v-else/>

    <Chatbot />
    <!-- <div className="search-container">
        <h1>The Eassiest Way to Get Your New Job</h1>
    </div> -->
        <div class="search_container">
            <h1 class="search_container_title">Your Place to Find a Job</h1>
            <div class="container2">
                <div class="row2">
                    <div class="col-md-12">
                        <form class="search_form" role="form" action="/search" id="search">
                            <div class="search_group_search_group_md_full"><input class="search_input" id="keywords" name="keywords" type="text" placeholder="Job title or keywords"></div>
                            <div class="search_group_search_group_md_50">
                                <span class="twitter-typeahead" style="position: relative; display: inline-block;">
                                    <input class="search_location typeahead tt-hint" type="text" readonly="" autocomplete="off" spellcheck="false" tabindex="-1" dir="ltr" style="position: absolute; top: 0px; left: 0px; border-color: transparent; box-shadow: none; opacity: 1; background: url(&quot;https://careerlink.com/images/img/location-icon.png&quot;) 16px 50% / 19px no-repeat scroll padding-box border-box rgb(255, 255, 255);">
                                    <input class="search_location_typeahead_tt-input" name="location" type="text" placeholder="Location or remote" autocomplete="off" spellcheck="false" dir="auto" style="position: relative; vertical-align: top; background-color: transparent;">
                                    <div class="tt-menu" style="position: absolute; top: 100%; left: 0px; z-index: 100; display: none;">
                                        <div class="tt-dataset tt-dataset-locations"></div>
                                    </div>
                                </span>
                            </div>
                            <div class="search_group_search_group_md_50"><button className="search_btn_new">Search Jobs</button>
                                <div class="search_text_box"></div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    <div class="container">
        <div class="job-part">
            <h1 :style="{marginBottom: '30px', marginLeft: '70px', fontSize: '30px', fontWeight: 'bold'}">
                Việc làm theo ngành nghề
            </h1>
            

            <div v-if="index > 0" class="prev" @click="decrement"><p>&#10094;</p></div>
            <div v-if="index < 2" class="next" @click="increment"><p>&#10095;</p></div>

            <div class="job-series">
                <div class="track" :style="{transform: 'translateX(-'+ (index*186) +'px)'}">
                    <div class="card" :style="{backgroundColor: '#ffa45b'}" @click="goByTag('IT')">
                        <h1>Công nghệ thông tin</h1>
                    </div>
                    <div class="card" :style="{backgroundColor: '#bce6eb'}" @click="goByTag('Kế toán')">
                        <h1>Kế toán / Kiểm toán</h1>
                    </div>    
                    <div class="card" :style="{backgroundColor: '#ffda77'}" @click="goByTag('Ngân hàng')">
                        <h1>Ngân hàng</h1>
                    </div>
                    <div class="card" :style="{backgroundColor: '#fdcfdf'}">
                        <h1>Xây dựng</h1>
                    </div>  
                    <div class="card" :style="{backgroundColor: '#f2dcbb'}">
                        <h1>Y tế</h1>
                    </div>
                    <div class="card" :style="{backgroundColor: '#edf285'}">
                        <h1>Du lịch</h1>
                    </div>    
                    <div class="card" :style="{backgroundColor: '#a1eafb'}">
                        <h1>Nhân sự</h1>
                    </div>
                    <div class="card" :style="{backgroundColor: '#ff91b3'}">
                        <h1>Bảo hiểm</h1>
                    </div>                  
                </div>
            </div>
        </div>
    </div>

    <div className="recommend-job">
        <div className="recommend-paper">
            <div :style="{padding: '20px 20px 0px 20px'}">
                <div class="box-smart-box">
                    <div class="box-label">
                        <p><i class="fa-solid fa-circle"></i>Công việc gợi ý</p>
                    </div>
                </div>
                <p :style="{fontWeight: '700', fontSize: '20px', margin: '15px 0px 7px 0px'}">Tin tuyển dụng, việc làm tốt nhất</p>
            </div>

            <!-- carosel -->
            <div>
                <div id="carouselExampleIndicators" class="carousel slide">
                    <div class="carousel-indicators">
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <div className="da-rc-contain">
                                <div v-for="(item , index) in testData" className="da-rc-card">
                                    <div className="da-inner-card">
                                        <div :style="{display: 'flex'}">
                                            <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg"/>
                                            <div className="da-card-input">
                                                <a><b>Chuyên viên phát triển kinh doanh</b></a>
                                                <a className="a2">Công ty gì đó dài ơi là dài khủng</a>
                                            </div>
                                            <button class="save-job btn-outline-hover" tabindex="-1">
                                                <i class="fa-regular fa-heart icon-first"></i> 
                                            </button>
                                        </div>

                                        <div :style="{display: 'flex', marginTop: '10px'}">
                                            <div class="salary-text_ellipsis">Thoả thuận</div>
                                            <div class="address-text_ellipsis">
                                                Hồ Chí Minh, Hà Nội
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <div className="da-rc-contain">
                                <div v-for="(item , index) in testData" className="da-rc-card">
                                    <div className="da-inner-card">
                                        <div :style="{display: 'flex'}">
                                            <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg"/>
                                            <div className="da-card-input">
                                                <a><b>Chuyên viên phát triển kinh doanh2</b></a>
                                                <a className="a2">Công ty gì đó dài ơi là dài khủng</a>
                                            </div>
                                            <button class="save-job btn-outline-hover" tabindex="-1">
                                                <i class="fa-regular fa-heart icon-first"></i> 
                                            </button>
                                        </div>

                                        <div :style="{display: 'flex', marginTop: '10px'}">
                                            <div class="salary-text_ellipsis">Thoả thuận</div>
                                            <div class="address-text_ellipsis">
                                                Hồ Chí Minh, Hà Nội
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <div className="da-rc-contain">
                                <div v-for="(item , index) in testData" className="da-rc-card">
                                    <div className="da-inner-card">
                                        <div :style="{display: 'flex'}">
                                            <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg"/>
                                            <div className="da-card-input">
                                                <a><b>Chuyên viên phát triển kinh doanh3</b></a>
                                                <a className="a2">Công ty gì đó dài ơi là dài khủng</a>
                                            </div>
                                            <button class="save-job btn-outline-hover" tabindex="-1">
                                                <i class="fa-regular fa-heart icon-first"></i> 
                                            </button>
                                        </div>

                                        <div :style="{display: 'flex', marginTop: '10px'}">
                                            <div class="salary-text_ellipsis">Thoả thuận</div>
                                            <div class="address-text_ellipsis">
                                                Hồ Chí Minh, Hà Nội
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev" >
                        <div class="slick-slick-arrow-left" aria-label="Previous">
                            <font-awesome-icon icon="left-long" class="slick-slick-arrow-icon"/>
                        </div>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                        <div class="slick-slick-arrow-right" aria-label="Next">
                            <font-awesome-icon icon="right-long" class="slick-slick-arrow-icon"/>
                        </div>
                    </button>
                </div>
            </div>

            <!-- <div className="da-rc-contain">
                <div v-for="(item , index) in testData" className="da-rc-card">
                    <div className="da-inner-card">
                        <div :style="{display: 'flex'}">
                            <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg"/>
                            <div className="da-card-input">
                                <a><b>Chuyên viên phát triển kinh doanh</b></a>
                                <a className="a2">Công ty gì đó dài ơi là dài khủng</a>
                            </div>
                            <button class="save-job btn-outline-hover" tabindex="-1">
                                <i class="fa-regular fa-heart icon-first"></i> 
                            </button>
                        </div>

                        <div :style="{display: 'flex', marginTop: '10px'}">
                            <div class="salary-text_ellipsis">Thoả thuận</div>
                            <div class="address-text_ellipsis">
                                Hồ Chí Minh, Hà Nội
                            </div>
                        </div>
                    </div>
                </div>
            </div> -->

        </div>

    </div>
    <div>

    </div>
</template>

<style>
@import './TrangChu.css';
</style>