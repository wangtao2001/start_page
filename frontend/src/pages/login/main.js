import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';
import VueRouter from "vue-router";
import Router from "./router/index"

Vue.use(ElementUI);
Vue.use(VueRouter);

new Vue({
  el: '#login',
  render: h => h(App),
  router: Router
});