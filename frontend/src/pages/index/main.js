import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';

Vue.use(ElementUI);
Vue.config.productionTip = false;

new Vue({
  el: '#index',
  render: h => h(App),
  beforeCreate() {
      Vue.prototype.$bus = this;
  }
});
