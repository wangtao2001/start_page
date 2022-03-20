<template>
  <div class="bg-info">
    {{ info }}
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "bg-info",
  data() {
    return {
      info: "",
    };
  },
  mounted() {
    axios.get("https://shuangchen.info/api/bing?mode=info").then(
      (res) => {
        this.info = res.data.data;
      },
      (error) => {
        console.log("error", error.message);
      }
    );
  },
};
</script>

<style>
@media screen and (max-width: 1220px) {
  /*页面宽度小于这个值壁纸介绍不显示 */
  .bg-info {
    display: none;
  }
}

.bg-info {
  transition: 0.8s;
  color: #8e9094;
  position: absolute;
  top: 0;
  right: 2rem;
  font-size: 0.65rem;
  user-select: none;
  backdrop-filter: blur(2px) brightness(80%);
  border-radius: 1rem;
  padding: 0.1rem 0.5rem 0.1rem 0.5rem;
}
</style>