<template>
  <div class="settings">
    <el-popover placement="top" width="200" trigger="click">
      <div class="settings-detail">
        <div class="detail">
          <p title="纯时钟">是否显示搜索框</p>
          <el-switch
            v-model="hasSeach"
            active-color="#13ce66"
            inactive-color="#dcdfe6"
          >
          </el-switch>
        </div>
        <div class="detail">
          <p title="来源：必应">是否使用每日一图</p>
          <el-switch
            v-model="hasBingBG"
            active-color="#13ce66"
            inactive-color="#dcdfe6"
          >
          </el-switch>
        </div>
      </div>
      <i class="iconfont settings-button" slot="reference">&#xe654;</i>
    </el-popover>
  </div>
</template>

<script>
export default {
  name: "setup",
  data() {
    return {
      hasSeach: true,
      hasBingBG: false,
    };
  },
  computed: {
    // 这一个计算属性的作用是获取所有设置同时去监听变化
    // 如果设置有变化就需要更新本地存储的值
    allSettings() {
      const { hasSeach, hasBingBG } = this;
      return {
        hasSeach,
        hasBingBG,
      };
    },
  },
  watch: {
    // 是否显示搜索框
    hasSeach: function () {
      this.$bus.$emit("hasSeachSwitch");
    },
    // 是否显示每日一图
    hasBingBG: function () {
      this.$bus.$emit("hasBingBGSwitch");
    },
    // 设置变化，更新本地存储
    allSettings: function (newSettings) {
      localStorage.removeItem("settings");
      localStorage.setItem("settings", JSON.stringify(newSettings));
    },
  },
  mounted() {
    // 查看历史设置
    var history = localStorage.getItem("settings");
    if (history === null) {
      // 没有历史设置 存入默认设置
      const defaultSettings = {
        // 填充所有默认设置
        hasSeach: true,
        hasBingBG: false,
      };
      localStorage.setItem("settings", JSON.stringify(defaultSettings));
    } else {
      const newSettings = JSON.parse(localStorage.getItem("settings"));
      // 搜索框设置
      this.hasSeach = newSettings.hasSeach;
      // 每日一图设置
      this.hasBingBG = newSettings.hasBingBG;
    }
  },
};
</script>

<style>
.settings-button {
  display: block;
  margin-top: 0.5rem;
  margin-right: 0.3rem;
  font-size: 1.4rem;
  color: rgba(255, 255, 255, 0.35);
  transition: 0.25s;
}

.settings-button:hover {
  color: rgba(255, 255, 255, 0.6);
  transition: 0.25s;
  transform: scale(0.9);
  transform-origin: center;
  transform: rotate(45deg);
}

.settings-detail {
  display: flex;
  flex-direction: column;
  font-size: 0.9rem;
}

.settings-detail .detail {
  display: flex;
  justify-content: space-between;
  margin-top: 0.2rem;
  margin-bottom: 0.2rem;
}
</style>