<template>
  <div class="suggestion">
    <!--翻译-->
    <div
      class="suggest trans"
      @click="trans"
      tabindex="-1"
      ref="trans"
      @keyup.enter="trans"
      @keyup.down="nextSuggest"
      @keyup.up="lastSuggest"
    >
      <i class="iconfont">&#xe619;</i>
      {{ "翻译 " + content }}
    </div>
    <!--联想词-->
    <div
      class="suggest"
      v-for="suggest in suggestions"
      :key="suggest.value"
      @click="search(suggest.value)"
      @keyup.enter="search(suggest.value)"
      tabindex="-1"
      ref="suggestions"
      @keyup.down="nextSuggest"
      @keyup.up="lastSuggest"
    >
      <i class="iconfont">&#xe62d;</i>
      {{ suggest.value }}
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "suggestion",
  data() {
    return {
      // 首先写死建议
      suggestions: [],
      content: "", // 从输入框获取到的搜索关键词
      focusSuggestIndex: -1, // 当前聚焦的建议条目
    };
  },
  mounted() {
    this.$bus.$on("contentChange", (newContent) => {
      this.content = newContent;
      this.focusSuggestIndex = -1; // 聚焦消失
    });
    this.$bus.$on("selectSuggestion", () => {
      // 上下键按动的事件从搜索框传递给了suggestion组件，就不回去了
      // 第一个focus的是翻译
      this.$refs.trans.focus();
      // 之后给到建议列表
    });
    this.$bus.$on("searchClick", () => {
      this.focusSuggestIndex = -1;
    });
  },
  methods: {
    trans() {
      // google翻译
      window.open(
        `https://translate.google.cn/?sl=en&tl=zh-CN&text=${this.content}&op=translate`
      );
    },
    search(suggestion) {
      // 点击联想词搜索 传递给search组件
      this.$bus.$emit("suggestChange", suggestion);
    },
    // 下一个建议聚焦
    nextSuggest() {
      if (this.focusSuggestIndex == this.suggestions.length - 1) {
        this.focusSuggestIndex = -1;
        // 再次聚焦到翻译
        this.$refs.trans.focus();
      } else {
        this.focusSuggestIndex = this.focusSuggestIndex + 1;
        this.$refs.suggestions[this.focusSuggestIndex].focus();
      }
    },
    //上一个建议聚焦
    lastSuggest() {
      if (this.focusSuggestIndex == 0) {
        this.focusSuggestIndex = this.suggestions.length;
        // 第一个建议的上一个是翻译
        this.$refs.trans.focus();
      } else if (this.focusSuggestIndex == -1) {
        this.focusSuggestIndex = this.suggestions.length - 1;
        this.$refs.suggestions[this.focusSuggestIndex].focus();
      } else {
        this.focusSuggestIndex = this.focusSuggestIndex - 1;
        this.$refs.suggestions[this.focusSuggestIndex].focus();
      }
    },
  },
  watch: {
    content: function () {
      // var array = ["CPU", "GPU", "NPU", "LPU", "hhh", "ddd", "ccc"];
      // this.suggestions = [];
      // array.forEach((su) => {
      //   this.suggestions.push({ value: su });
      // });

      // 观察到输入内容的变化 查询后端 更新suggestions 而后渲染出来
      // 使用百度的搜索接口
      var api = "https://shuangchen.info/api/suggestion/?wd=";
      axios.get(api + this.content).then(
        (resp) => {
          var array = resp.data.data;
          this.suggestions = []; // 清空原有
          array.forEach((suggestion, index) => {
            if (index < 9) {
              // 最多9条建议
              this.suggestions.push({ value: suggestion });
            }
          });
        },
        (error) => {
          console.log("error", error.message);
        }
      );
    },
  },
};
</script>

<style>
.suggestion {
  border-radius: 1rem;
  width: 100%;
  height: auto;
  background-color: #fff;
}

.suggest {
  height: 2rem;
  padding-left: 0.8rem;
  line-height: 2rem;
  overflow: hidden; /* 超出的文本隐藏 */
  text-overflow: ellipsis; /*溢出用省略号显示*/
  white-space: nowrap; /*溢出不换行*/
}

.suggest:first-child {
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
}

.suggest:last-child {
  border-bottom-left-radius: 1rem;
  border-bottom-right-radius: 1rem;
}
.suggestion .suggest:hover {
  background-color: #f7f7f7;
}

.suggest:focus {
  background-color: #f7f7f7;
  outline: none;
}

.suggest i {
  color: #999;
  margin-right: 0.2rem;
}
</style>