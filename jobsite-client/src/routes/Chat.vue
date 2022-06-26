<script>
import Navbar from '../components/Navbar2.vue';
export default {
  components: {
    Navbar
  },
}
</script>


<template>
    <Navbar />
    <div :style="{width: '100%', height: '60px', backgroundColor: '#2f323e', alignItems: 'center', paddingTop: '5px', paddingLeft: '35px', display:'flex'}">
        <h1 :style="{fontSize: '18px', fontWeight: 'bold', color: 'white'}">Trò chuyện</h1>
    </div>
    <div :style="{width: '104%', height: '78vh'}">
			<div class="chat-container" :style="{margin: 0}">
				<div class="name-list">
					<div class="one-user one-user-active">
						<img src="../assets/img_avatar3.png" class='avatar-circle' st/>
						<div :style="{fontSize: '15px', fontWeight: 'revert'}">Tên gì đó</div>
					</div>
					<div class="one-user">
						<img src="../assets/img_avatar3.png" class='avatar-circle' st/>
						<div :style="{fontSize: '15px', fontWeight: 'revert'}">Tên gì đó</div>
					</div>
				</div>

				<div class="conversation">
					<div class="conversation-title">
						<img src="../assets/img_avatar3.png" class='avatar-circle' st/>
						<div :style="{fontSize: '15px', fontWeight: 'bold'}">Tên gì đó</div>
					</div>

					<div class="conversation-content">
						<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="receiver">
							<div> Hi Aiden, how are you? How is the project coming along? </div>
						</div>
												<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="receiver">
							<div> Hi Aiden, how are you? How is the project coming along? </div>
						</div>
												<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="sender">
						<div >Hi Aiden, how are you? How is the project coming along? </div>
						</div>
						<div class="receiver">
							<div> Hi Aiden, how are you? How is the project coming along? </div>
						</div>
					</div>

					<div class="send-button">
						<input class="send-input"/>
						<font-awesome-icon icon="paper-plane" :style="{color: '#2962ff', width: '20px', height: '20px'}"/>
					</div>
				</div>

			</div>
    </div>
</template>