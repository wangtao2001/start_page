<template>
  <div
    id="app"
    :style="{
      '--bg': hasBingBG ? defaultBG : BingBG,
    }"
  >
    <div class="header">
      <user></user>
      <settings></settings>
    </div>
    <div class="content">
      <clock></clock>
      <transition name="fade">
        <search v-if="hasSeach"></search>
      </transition>
    </div>
    <div class="footer">
      <site-info></site-info>
      <bg-info v-show="hasBingBG"></bg-info>
    </div>
  </div>
</template>

<script>
import user from "../../components/user.vue";
import settings from "../../components/settings.vue";
import clock from "../../components/clock.vue";
import search from "../../components/search.vue";
import SiteInfo from "../../components/site-info.vue";
import BgInfo from "../../components/bg-info.vue";
export default {
  components: { clock, search, SiteInfo, settings, user, BgInfo },
  name: "app",
  mounted() {
    // 以后这些设置可以一起打包监听过来
    this.$bus.$on("hasSeachSwitch", () => {
      this.hasSeach = !this.hasSeach;
    });
    this.$bus.$on("hasBingBGSwitch", () => {
      this.hasBingBG = !this.hasBingBG;
    });
  },
  data() {
    return {
      hasSeach: true,
      hasBingBG: false,
      defaultBG: 'url("https://shuangchen.info/api/bing?mode=bg")', // 自建api
      BingBG: "url(" + require("../../assets/wallpaper/index.jpg") + ")",
    };
  },
};
</script>

<style>
@font-face {
  font-family: "light";
  src: url("../../assets/font/HARMONYOS_SANS_LIGHT.TTF");
}

@font-face {
  font-family: "iconfont";
  src: url("../../assets/font/iconfont.ttf") format("truetype");
}

@media screen and (max-width: 400px) {
  .content::before {
    height: 5% !important;
  }

  .clock {
    font-size: 2.5rem;
  }
}

.iconfont {
  font-family: "iconfont" !important;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: light;
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
  background-color: rgba(0, 0, 0, 0.8);
}

/* 壁纸以及壁纸叠加的模糊 */
#app::before {
  filter: blur(5px);
  background-image: var(--bg);
  transition: 0.5s;
  background-position: center center;
  background-size: cover;
  background-attachment: fixed;
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  z-index: 1;
}

.header {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  margin-top: 0.3rem;
  padding: 0 0.5rem 0 0.5rem;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-grow: 1;
  width: 80%;
}

.content::before {
  content: "";
  display: block;
  width: 100%;
  height: 15%;
}

.footer {
  display: flex;
  justify-content: center;
  width: 100%;
  position: relative;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
