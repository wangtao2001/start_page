<template>
  <div class="engine">
    <div>
      <input type="radio" id="baidu" value="baidu" v-model="engine" />
      <label for="baidu" class="iconfont">&#xe67b;</label>
    </div>
    <div>
      <input type="radio" id="bing" value="bing" v-model="engine" />
      <label for="bing" class="iconfont">&#xeddb;</label>
    </div>
    <div>
      <input type="radio" id="google" value="google" v-model="engine" />
      <label for="google" class="iconfont">&#xe692;</label>
    </div>
  </div>
</template>

<script>
export default {
  name: "engine",
  data() {
    return {
      engine: "baidu",
    };
  },
  watch: {
    engine: function (newVal) {
      this.$bus.$emit("changeEngine", newVal);
    },
  },
};
</script>

<style>
.engine {
  width: 100%;
  user-select: none;
  display: flex;
  justify-content: center;
}

.engine div {
  margin: 0.8rem 5% 0.8rem 5%;
  padding: 0.3rem 1.5rem 0.3rem 1.5rem;
  border-radius: 1rem;
  /*性能有问题*/
  /* backdrop-filter: blur(0.1rem) brightness(80%); */
}

.engine input {
  display: none;
}

.engine label {
  color: rgba(255, 255, 255, 0.5);
  font-size: 1.5rem;
}

.engine input:checked + label {
  color: #fff;
  transition: 0.3s;
}
</style>