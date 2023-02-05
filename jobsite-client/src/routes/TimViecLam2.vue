<template>
    <Navbar v-if="userToken"/>
    <Navbar2 v-else/>

    <div :style="{ backgroundColor: 'white', width: '100%', height: '75px' }">
      <div class="da24-inner2">

        <div class="input-data-search-input" :style="{marginRight: '7px'}">
          <input placeholder="Tên công việc, vị trí bạn muốn ứng tuyển ...">
        </div>

        <div class="input-data-search-input" :style="{marginRight: '7px', width: '19%'}">
          <select class="form-select my-select w-100">
            <option selected>Tất cả ngành nghề</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
          </select>      
        </div>

        <div class="input-data-search-input" :style="{marginRight: '7px', width: '20%'}">
          <select class="form-select my-select w-100">
            <option selected>Tất cả lĩnh vực công ty</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
          </select>      
        </div>

        <div class="input-data-search-input" :style="{marginRight: '7px', width: '19%'}">
          <select class="form-select my-select w-100">
            <option selected>Tất cả địa điểm</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
          </select>      
        </div>

        <div class="input-data-search-submit">
          <button>
            <font-awesome-icon icon="magnifying-glass" class="met-a-nha"/>Tìm kiếm
          </button>
        </div>
      </div>
    </div>

    <div class="da24-container">
      <div class="da24-inner">
          <div class="da24-paper">
              <div class="da24-first-line">
                <font-awesome-icon icon="robot" class="da24-robot"/>
                <h3>Việc làm có thể phù hợp</h3>
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
                          <div :style="{display: 'flex', width: '100%', justifyContent: 'center'}">
                            <div class="da24-card">
                              <div className="da-inner-card2" :style="{marginTop: '10px'}">
                                <div :style="{display: 'flex'}">
                                    <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg" :style="{width: '47px', height: '47px'}"/>
                                    <div className="da-card-input">
                                        <a><b>Chuyên viên phát triển kinh doanh</b></a>
                                        <a className="a2" :style="{marginTop: '20px'}">Công ty gì đó dài ơi là dài khủng</a>
                                    </div>
                                    <button class="save-job2 btn-outline-hover" tabindex="-1">
                                        <i class="fa-regular fa-heart icon-first2"></i> 
                                    </button>
                                </div>

                                <div :style="{display: 'flex', marginTop: '35px'}">
                                    <div class="salary-text_ellipsis">Thoả thuận</div>
                                    <div class="address-text_ellipsis">
                                        Hồ Chí Minh, Hà Nội
                                    </div>
                                </div>
                              </div>
                            </div>

                            <div class="da24-card">
                              <div className="da-inner-card2" :style="{marginTop: '10px'}">
                                <div :style="{display: 'flex'}">
                                    <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg" :style="{width: '47px', height: '47px'}"/>
                                    <div className="da-card-input">
                                        <a><b>Chuyên viên phát triển kinh doanh</b></a>
                                        <a className="a2" :style="{marginTop: '20px'}">Công ty gì đó dài ơi là dài khủng</a>
                                    </div>
                                    <button class="save-job2 btn-outline-hover" tabindex="-1">
                                        <i class="fa-regular fa-heart icon-first2"></i> 
                                    </button>
                                </div>

                                <div :style="{display: 'flex', marginTop: '35px'}">
                                    <div class="salary-text_ellipsis">Thoả thuận</div>
                                    <div class="address-text_ellipsis">
                                        Hồ Chí Minh, Hà Nội
                                    </div>
                                </div>
                              </div>
                            </div>

                            <div class="da24-card">
                              <div className="da-inner-card2" :style="{marginTop: '10px'}">
                                <div :style="{display: 'flex'}">
                                    <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg" :style="{width: '47px', height: '47px'}"/>
                                    <div className="da-card-input">
                                        <a><b>Chuyên viên phát triển kinh doanh</b></a>
                                        <a className="a2" :style="{marginTop: '20px'}">Công ty gì đó dài ơi là dài khủng</a>
                                    </div>
                                    <button class="save-job2 btn-outline-hover" tabindex="-1">
                                        <i class="fa-regular fa-heart icon-first2"></i> 
                                    </button>
                                </div>

                                <div :style="{display: 'flex', marginTop: '35px'}">
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
                        </div>
                        <div class="carousel-item">
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

              <!-- <div :style="{display: 'flex', width: '100%', justifyContent: 'center'}">
                <div class="da24-card">
                  <div className="da-inner-card2" :style="{marginTop: '10px'}">
                    <div :style="{display: 'flex'}">
                        <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg" :style="{width: '47px', height: '47px'}"/>
                        <div className="da-card-input">
                            <a><b>Chuyên viên phát triển kinh doanh</b></a>
                            <a className="a2" :style="{marginTop: '20px'}">Công ty gì đó dài ơi là dài khủng</a>
                        </div>
                        <button class="save-job2 btn-outline-hover" tabindex="-1">
                            <i class="fa-regular fa-heart icon-first2"></i> 
                        </button>
                    </div>

                    <div :style="{display: 'flex', marginTop: '35px'}">
                        <div class="salary-text_ellipsis">Thoả thuận</div>
                        <div class="address-text_ellipsis">
                            Hồ Chí Minh, Hà Nội
                        </div>
                    </div>
                  </div>
                </div>

                <div class="da24-card">
                  <div className="da-inner-card2" :style="{marginTop: '10px'}">
                    <div :style="{display: 'flex'}">
                        <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg" :style="{width: '47px', height: '47px'}"/>
                        <div className="da-card-input">
                            <a><b>Chuyên viên phát triển kinh doanh</b></a>
                            <a className="a2" :style="{marginTop: '20px'}">Công ty gì đó dài ơi là dài khủng</a>
                        </div>
                        <button class="save-job2 btn-outline-hover" tabindex="-1">
                            <i class="fa-regular fa-heart icon-first2"></i> 
                        </button>
                    </div>

                    <div :style="{display: 'flex', marginTop: '35px'}">
                        <div class="salary-text_ellipsis">Thoả thuận</div>
                        <div class="address-text_ellipsis">
                            Hồ Chí Minh, Hà Nội
                        </div>
                    </div>
                  </div>
                </div>

                <div class="da24-card">
                  <div className="da-inner-card2" :style="{marginTop: '10px'}">
                    <div :style="{display: 'flex'}">
                        <img className="da-card-img" src="https://cdn.topcv.vn/44/company_logos/mpX42HbOazypLoJi1ew3Anc96RIEF8Fq_1671097795____b487f431b9f183f361718221a48933f6.jpg" :style="{width: '47px', height: '47px'}"/>
                        <div className="da-card-input">
                            <a><b>Chuyên viên phát triển kinh doanh</b></a>
                            <a className="a2" :style="{marginTop: '20px'}">Công ty gì đó dài ơi là dài khủng</a>
                        </div>
                        <button class="save-job2 btn-outline-hover" tabindex="-1">
                            <i class="fa-regular fa-heart icon-first2"></i> 
                        </button>
                    </div>

                    <div :style="{display: 'flex', marginTop: '35px'}">
                        <div class="salary-text_ellipsis">Thoả thuận</div>
                        <div class="address-text_ellipsis">
                            Hồ Chí Minh, Hà Nội
                        </div>
                    </div>
                  </div>
                </div>
              </div> -->
          </div>

          <div class="da24-paper" :style="{marginTop: '40px', height: 'auto', padding: '0'}">
            <div :style="{padding : '16px'}">
              <h3 class="da24-findjob">Tìm thấy <b>23,577</b> việc làm phù hợp với yêu cầu của bạn.</h3>
            </div>
            <div :style="{width: '100%', height: '1px', backgroundColor: '#eeeeee'}"></div>

            <div :style="{padding : '16px'}">


              <div class="da24-lists" :style="{marginBottom: '40px'}">
                <div class="job-item-bg-highlight" :style="{backgroundColor: '#fff9f0'}">
                  <div :style="{display: 'flex'}">
                  <img src="https://cdn.topcv.vn/80/company_logos/TtErXoY8ibRqIyfk5zrBA8PntCPGy8qQ_1662535504____b352221a8f8b7346490f61058c9b83c3.jpg" :style="{width: '80px', height: '80px', objectFit: 'contain', marginRight: '16px'}">

                  <div :style="{maxWidth: '750px'}" class="da24-taylor">
                    <h3>Nhân Viên Kinh Doanh (Không Yêu Cầu Kinh Nghiệm, Thu Nhập Lên Đến 20 Triệu) </h3>
                    <h4>Công ty cổ phần Grand Nutrition</h4>
                    <div class="da24-swift">
                      <label class="jennie">Tới 20 triệu</label>
                      <label class="jennie">Hà Nội</label>
                    </div>
                  </div>
                  </div>
                  <div :style="{display: 'flex', flexDirection: 'row-reverse'}">
                    <div class="whistle">
                      <h3>
                        01/01/2023
                      </h3>

                      <div :style="{display: 'flex', width: '100%', flexDirection: 'row-reverse'}">
                        <button class="save-job2 btn-outline-hover" tabindex="-1">
                                        <i class="fa-regular fa-heart icon-first2"></i> 
                        </button>
                      </div>

                    </div>
                  </div>
                </div>

                <div class="job-item-bg-highlight" :style="{backgroundColor: '#fff9f0'}">
                  <div :style="{display: 'flex'}">
                  <img src="https://cdn.topcv.vn/80/company_logos/TtErXoY8ibRqIyfk5zrBA8PntCPGy8qQ_1662535504____b352221a8f8b7346490f61058c9b83c3.jpg" :style="{width: '80px', height: '80px', objectFit: 'contain', marginRight: '16px'}">

                  <div :style="{maxWidth: '750px'}" class="da24-taylor">
                    <h3>Nhân Viên Kinh Doanh (Không Yêu Cầu Kinh Nghiệm, Thu Nhập Lên Đến 20 Triệu) </h3>
                    <h4>Công ty cổ phần Grand Nutrition</h4>
                    <div class="da24-swift">
                      <label class="jennie">Tới 20 triệu</label>
                      <label class="jennie">Hà Nội</label>
                    </div>
                  </div>
                  </div>
                  <div :style="{display: 'flex', flexDirection: 'row-reverse'}">
                    <div class="whistle">
                      <h3>
                        01/01/2023
                      </h3>

                      <div :style="{display: 'flex', width: '100%', flexDirection: 'row-reverse'}">
                        <button class="save-job2 btn-outline-hover" tabindex="-1">
                                        <i class="fa-regular fa-heart icon-first2"></i> 
                        </button>
                      </div>

                    </div>
                  </div>
                </div>

                <div class="job-item-bg-highlight" :style="{backgroundColor: '#fff9f0'}">
                  <div :style="{display: 'flex'}">
                  <img src="https://cdn.topcv.vn/80/company_logos/TtErXoY8ibRqIyfk5zrBA8PntCPGy8qQ_1662535504____b352221a8f8b7346490f61058c9b83c3.jpg" :style="{width: '80px', height: '80px', objectFit: 'contain', marginRight: '16px'}">

                  <div :style="{maxWidth: '750px'}" class="da24-taylor">
                    <h3>Nhân Viên Kinh Doanh (Không Yêu Cầu Kinh Nghiệm, Thu Nhập Lên Đến 20 Triệu) </h3>
                    <h4>Công ty cổ phần Grand Nutrition</h4>
                    <div class="da24-swift">
                      <label class="jennie">Tới 20 triệu</label>
                      <label class="jennie">Hà Nội</label>
                    </div>
                  </div>
                  </div>
                  <div :style="{display: 'flex', flexDirection: 'row-reverse'}">
                    <div class="whistle">
                      <h3>
                        01/01/2023
                      </h3>

                      <div :style="{display: 'flex', width: '100%', flexDirection: 'row-reverse'}">
                        <button class="save-job2 btn-outline-hover" tabindex="-1">
                                        <i class="fa-regular fa-heart icon-first2"></i> 
                        </button>
                      </div>

                    </div>
                  </div>
                </div>
              </div>

              <div class="lisa-text-center">
                <nav class="lisa">
                  <ul class="lisa-pagination">
                    <li>
                      <a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=1" :style="{fontSize: '20px', color: '#333'}">‹</a>
                    </li>
                    <li>
                      <a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=1">1</a>
                    </li>
                    <li class="active" aria-current="page">
                      <span>2</span>
                    </li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=3">3</a></li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=4">4</a></li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=5">5</a></li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=6">6</a></li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=7">7</a></li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=8">8</a></li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=9">9</a></li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=10">10</a></li>
                    <li class="disabled" aria-disabled="true"><span>...</span></li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=399">399</a></li>
                    <li><a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=400">400</a></li>
                    
                    <li>
                      <a href="https://www.topcv.vn/tim-viec-lam-moi-nhat?salary=0&amp;exp=0&amp;sort=top_related&amp;page=3" :style="{fontSize: '20px', color: '#333'}">›</a>
                    </li>
                  </ul>
                </nav>
              </div>
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