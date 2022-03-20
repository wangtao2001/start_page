<template>
  <div class="user">
    <el-popover placement="top" width="180" trigger="click">
      <div class="user-detail" v-if="hasLogin">
        <div class="welcome">
          <p style="font-weight: bold">欢迎 {{ username }}</p>
          <p>进入空间探索更多功能</p>
          <el-button @click="space" class="btn">个人空间</el-button>
          <el-button @click="logout" class="btn">退出登录</el-button>
        </div>
      </div>
      <div class="user-detail" v-else>
        <div class="login">
          <p style="font-weight: bold">您尚未登录</p>
          <p>登陆后探索更多功能</p>
          <el-button @click="login" class="btn">登录</el-button>
        </div>
      </div>

      <i class="iconfont user-button" slot="reference">&#xe628;</i>
    </el-popover>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.withCredentials = true;
export default {
  name: "user",
  methods: {
    // 登录
    login() {
      window.open("/login", "_self");
    },
    // 退出登录
    logout() {
      window.open("/logout", "_self");
    },
    space() {
      window.open("/space", "_blank");
    },
  },
  data() {
    return {
      hasLogin: false,
      username: "",
    };
  },
  created() {
    // 获取登陆状态 如果登录就请求用户名
    const data = {
      mode: "userInfo",
      data: ["username"],
    };
    axios
      .post(`https://shuangchen.info/api/userInfo/`, JSON.stringify(data))
      .then(
        (res) => {
          var resp = res.data;
          if (resp.code == 200) {
            // 有登录
            this.hasLogin = true;
            this.username = resp.data.username;
          }
        },
        (error) => {
          console.log("error", error.message);
        }
      );
  },
};
</script>

<style>
.user-button {
  display: block;
  margin-top: 0.5rem;
  margin-right: 0.7rem;
  font-size: 1.4rem;
  color: rgba(255, 255, 255, 0.35);
  transition: 0.25s;
}

.user-button:hover {
  color: rgba(255, 255, 255, 0.6);
  transition: 0.25s;
  transform: scale(0.9);
  transform-origin: center;
}

.login,
.welcome {
  display: flex;
  flex-direction: column;
}

.login p,
.welcome p {
  text-align: right;
}

.el-button + .el-button {
  margin-left: 0;
}

.btn {
  margin-top: 0.4rem;
}
</style>