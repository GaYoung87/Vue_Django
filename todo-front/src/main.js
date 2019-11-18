import Vue from 'vue'
import App from './App.vue'
import router from './router'
// 만약 폴더만 지정해놓고 어떤 파일인지 등록하지 않았으면 폴더 안의 index.js파일을 찾아감
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
