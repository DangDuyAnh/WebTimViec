//import Vue from 'vue'

import { createApp } from 'vue'
import App from './App.vue'
import router from './routes' 
import { library } from '@fortawesome/fontawesome-svg-core'

// import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { faMagnifyingGlass, faFloppyDisk, faShareFromSquare, faIdBadge, faEnvelopeOpenText, faLocationDot, faClock, faBuilding, faUser, faFileCirclePlus, faComment, faAngleDown, faComments, faCheck, faXmark, faPaperPlane, faTrash, faStar} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import GAuth from 'vue3-google-oauth2'

const gauthOption = {
  clientId: '884962095696-1nljcnopsmtsug7enqtfhuf4f02ofq8t.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
} */
//Vue.use(GAuth, gauthOption)

// library.add(faUserSecret)
library.add(faMagnifyingGlass, faFloppyDisk, faShareFromSquare, faIdBadge, faEnvelopeOpenText, faLocationDot, faClock, faBuilding, faUser, faFileCirclePlus, faComment, faComments,faAngleDown, faCheck, faXmark,
  faPaperPlane, faTrash, faStar);

createApp(App)
.component('font-awesome-icon', FontAwesomeIcon)
//.use(GAuth, gauthOption)
.use(router).mount('#app')
