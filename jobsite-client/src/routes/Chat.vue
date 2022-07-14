<script>
import Navbar from '../components/Navbar2.vue';
import axios from 'axios';
import { authenticationService } from '../utility/authenticationService';
export default {
  components: {
    Navbar
  },
    data() {
    return {
      user : authenticationService.getUser(),
      chatList: [],
      roomIds: [],
      chatUsers: {},
      active: 0,
      title: '',
      conversation: [],
      text: ''
    }
  },
    mounted() {
    let config = {
    headers: {
    'Authorization': 'Bearer ' + authenticationService.getUserToken()
    }
    }
        axios.get('http://localhost:8000/api/chat-room/list', config)
        .then(res => {
            console.log(res.data)
            this.roomIds = [...res.data]
            this.active = res.data[0]
            let array = {}
            async function getUser(id) {
            let res2 = await axios.get('http://localhost:8000/api/chat-room/members-detail-list?room_id=' + id , config);
            let data = res2.data
            data = data.filter(item => item.id !== authenticationService.getUser().id)[0]
            array[id] = data
            console.log('array user')
            console.log(array)
            }
            Promise.all(res.data.map(x => getUser(x))).then(item => {
                this.chatUsers = {...array}});
        })       
        },
	methods: {
	setRoomId(item) {
		this.active = item
	},
	sendText() {
		let config = {
		headers: {
		'Authorization': 'Bearer ' + authenticationService.getUserToken()
		}
		}
		axios.post('http://localhost:8000/api/chat-room/send', {room_id: this.active, text: this.text}, config)
		.then(res => {
			console.log(res.data)
			this.conversation = [ {text: this.text, sender_user: authenticationService.getUser().id},...this.conversation]
			this.text = ''
			}
		)
	}
	},
    watch: {
        active(newQuestion, oldQuestion) {
            let config = {
            headers: {
            'Authorization': 'Bearer ' + authenticationService.getUserToken()
            }
            }
            axios.get('http://localhost:8000/api/chat-room/conversation?room_id=' + this.active, config)
            .then(res => {
                console.log(res.data)
                this.conversation = [...res.data.reverse()]
                }
            )

                this.intervalid1 = setInterval(function(){
                    axios.get('http://localhost:8000/api/chat-room/conversation?room_id=' + this.active, config)
                    .then(res => {
                        this.conversation = [...res.data.reverse()]
                        }
                    )
                }.bind(this), 1500);
        }
    }
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
					<div v-for="(item , index) in roomIds">
                        <div v-if="item === active" class="one-user-active">
                        <div class="one-user">
                            <img src="../assets/img_avatar3.png" class='avatar-circle' st/>
                            <div :style="{fontSize: '15px', fontWeight: 'revert'}">{{chatUsers[item].username}}</div>
                        </div>
                        </div>

                        <div v-else>
                        <div class="one-user" @click="setRoomId(item)">
                            <img src="../assets/img_avatar3.png" class='avatar-circle' st/>
                            <div :style="{fontSize: '15px', fontWeight: 'revert'}">{{chatUsers[item].username}}</div>
                        </div>
                        </div>
					</div>
				</div>

				<div class="conversation">
					<div class="conversation-title">
						<img src="../assets/img_avatar3.png" class='avatar-circle' st/>
						<div v-if="chatUsers[active]" :style="{fontSize: '15px', fontWeight: 'bold'}">{{chatUsers[active].username}}</div>
					</div>

					<div class="conversation-content">
                        <div v-for="item in conversation">
                            <div v-if="String(item.sender_user) == String(user.id)" class="sender">
                            <div>{{item.text}}</div>
                            </div>

                            <div v-else class="receiver">
                            <div>{{item.text}}</div>
                            </div>
                        </div>
					</div>

					<div class="send-button">
						<input class="send-input" v-model="text" @keyup.enter="sendText"/>
						<font-awesome-icon icon="paper-plane" :style="{color: '#2962ff', width: '20px', height: '20px', cursor: 'pointer'}" @click="sendText"/>
					</div>
				</div>

			</div>
    </div>
</template>