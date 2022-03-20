<template>
  <div class="search">
    <input
      placeholder="搜索"
      v-model="content"
      @keyup.enter="search"
      @keyup.down="selectSuggestion"
      @click="searchClick"
    />
    <i class="iconfont enter-search" @click="search">&#xe62d;</i>
    <i class="iconfont clean" @click="clean" v-if="content">&#xe753;</i>
    <engine-select></engine-select>
    <suggestion v-if="content"></suggestion>
  </div>
</template>

<script>
import suggestion from "./suggestion.vue";
import EngineSelect from "./engine-select.vue";
export default {
  name: "search",
  components: { EngineSelect, suggestion },
  data() {
    return {
      content: "",
      engine: "baidu",
    };
  },
  mounted() {
    this.$bus.$on("changeEngine", (newEngine) => {
      this.engine = newEngine;
    });
    // 联想词搜索
    this.$bus.$on("suggestChange", (suggestion) => {
      this.content = suggestion;
      this.search();
    });
  },
  watch: {
    // 输入内容改变
    content: function (newContent) {
      // 这里写延迟是因为content变化是suggesstion才渲染出来，此时其中的$on还没有在注册工作，需要延迟
      setTimeout(() => {
        this.$bus.$emit("contentChange", newContent);
      }, 0);
    },
  },
  methods: {
    search() {
      if (this.engine === "baidu") {
        window.open(`https://www.baidu.com/s?ie=utf-8&word=${this.content}`);
      } else if (this.engine === "bing") {
        window.open(`https://cn.bing.com/search?q=${this.content}`);
      } else if (this.engine === "google") {
        window.open(`https://www.google.com.hk/search?q=${this.content}`);
      }
    },
    // 按住上下键选择建议
    selectSuggestion() {
      this.$bus.$emit("selectSuggestion");
    },
    // 清除输入
    clean() {
      this.content = "";
    },
    // 添加这个方法的原因主要是点一下搜索框，需要将聚焦定位置为-1
    searchClick() {
      this.$bus.$emit("searchClick");
    },
  },
};
</script>

<style>
.search {
  width: 100%;
  max-width: 30rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.search .enter-search {
  position: absolute;
  top: 1.7rem;
  right: 1rem;
}

.search .clean {
  position: absolute;
  top: 1.5rem;
  right: 2.3rem;
  font-size: 1.3rem;
  color: #363636;
}

.search > input {
  width: 100%;
  height: 2.3rem;
  border: none;
  outline: none;
  border-radius: 3rem;
  padding-left: 1rem;
  margin-top: 1rem;
  /*一个模糊效果 但是性能有问题*/
  /* box-shadow: rgb(0 0 0 / 20%) 0 0 10px;
  backdrop-filter: blur(10px);
  background-color: rgba(255, 255, 255, 0.25); */
}
</style>