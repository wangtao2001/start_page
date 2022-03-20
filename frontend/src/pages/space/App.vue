<template>
  <div id="app">
    <header class="header">
      <space-head></space-head>
    </header>
    <div class="content">
      <tool
        v-for="tool in tools"
        :key="tool.name"
        :name="tool.name"
        :intro="tool.intro"
        :icon="tool.icon"
        :link="tool.link"
      ></tool>
    </div>
    <footer>
      <site-info></site-info>
    </footer>
  </div>
</template>

<script>
import SiteInfo from "../../components/site-info.vue";
import SpaceHead from "../../components/space-head.vue";
import Tool from "../../components/tool.vue";
export default {
  name: "App",
  components: { SiteInfo, SpaceHead, Tool },
  data() {
    return {
      tools: [
        {
          name: "起始页",
          intro: "简洁的浏览器起始页",
          icon: require("../../assets/logo/logo.jpg"),
          link: "/",
        },
        {
          name: "云笔记",
          intro: "在线查看并编辑笔记",
          icon: require("../../assets/logo/notepad.png"),
          link: "/cloudnote",
        },
      ],
    };
  },
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
  background: url("../../assets/wallpaper/space.jpg");
  background-position: center center;
  background-size: cover;
  background-attachment: fixed;
}

.header {
  width: 100%;
}

.content {
  width: 90%;
  height: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 2rem;
  padding-bottom: 2rem;
}

@media screen and (max-width: 600px) {
  .content {
    flex-direction: column;
    width: 100%;
  }
}
</style>
