<template>
  <div id="app">
    <header></header>
    <div class="content">
      <router-view></router-view>
    </div>
    <footer>
      <site-info></site-info>
    </footer>
  </div>
</template>

<script>
import SiteInfo from "../../components/site-info.vue";
export default {
  name: "App",
  components: { SiteInfo },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  /*所有文字不可选*/
  user-select: none;
}

html,
body,
#app {
  width: 100%;
  height: 100%;
}

#app * {
  z-index: 2;
}

#app {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  position: relative;
  background-color: #000;
}

/* 壁纸以及壁纸叠加的模糊 */
#app::before {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  z-index: 1;
  filter: blur(10px);
  background: url("../../assets/wallpaper/login.jpg");
  background-position: center center;
  background-size: cover;
  background-attachment: fixed;
}
</style>
