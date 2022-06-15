import { createApp } from 'vue'
import App from './App.vue'
import router from './routes' 
import { library } from '@fortawesome/fontawesome-svg-core'

// import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { faMagnifyingGlass, faFloppyDisk, faShareFromSquare, faIdBadge, faEnvelopeOpenText, faLocationDot, faClock, faBuilding, faUser, faFileCirclePlus, faComment, faAngleDown } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// library.add(faUserSecret)
library.add(faMagnifyingGlass, faFloppyDisk, faShareFromSquare, faIdBadge, faEnvelopeOpenText, faLocationDot, faClock, faBuilding, faUser, faFileCirclePlus, faComment, faAngleDown);

createApp(App)
.component('font-awesome-icon', FontAwesomeIcon)
.use(router).mount('#app')
