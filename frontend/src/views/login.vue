<template>
  <div class="login login-card">
    <img src="../assets/logo/logo.jpg" />
    <el-input
      class="username"
      v-model="username"
      placeholder="请输入用户名"
    ></el-input>
    <el-input
      class="password"
      placeholder="请输入密码"
      v-model="password"
      show-password
    ></el-input>
    <div class="options">
      <el-switch v-model="remember" active-text="记住登录"> </el-switch>
      <el-link type="primary" style="font-size: 1rem" @click="register"
        >注册账号</el-link
      >
    </div>
    <el-button @click="login" class="login-button" type="primary"
      >登录</el-button
    >
  </div>
</template>

<script>
import axios from "axios"; // 使用axios库进行请求
axios.defaults.withCredentials = true;
export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      remember: false,
    };
  },
  methods: {
    // 获取当前url参数
    // 主要是为了获取next的参数值，即登陆后下一步跳转
    getQueryString(name) {
      let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
      let r = window.location.search.substr(1).match(reg);
      if (r != null) {
        return decodeURIComponent(r[2]);
      }
      return null;
    },
    register() {
      this.$router.push({
        name: "register",
      });
    },
    login() {
      // 非空验证
      if (this.username === "" || this.password === "") {
        this.$notify.error({
          title: "错误",
          message: "用户名或密码不能为空",
          position: "top-left",
        });
      } else {
        // 向服务器发送数据
        const data = {
          mode: "login",
          data: {
            username: this.username,
            password: this.password,
            remember: this.remember.toString(),
          },
        };
        axios
          .post(`https://shuangchen.info/api/login/`, JSON.stringify(data))
          .then(
            (res) => {
              var resp = res.data;
              if (resp.code != 200) {
                // 登录失败
                this.$notify.error({
                  title: "错误",
                  message: resp.message,
                  position: "top-left",
                });
                this.password = "";
              } else {
                // 登陆成功
                this.$notify({
                  title: "成功",
                  message: resp.message,
                  position: "top-left",
                  type: "success",
                });
                // 登录成功 跳转首页
                setTimeout(() => {
                  var next = this.getQueryString("next");
                  if (next) {
                    window.open(next, "_self");
                  } else {
                    window.open("/", "_self");
                  }
                }, 1000);
              }
            },
            (error) => {
              console.log("error", error.message);
            }
          );
      }
    },
  },
};
</script>

<style>
.login-card {
  /*宽度写死不要动哦 */
  width: 20rem;
  height: 22rem;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.05);
  box-shadow: rgb(0 0 0 / 10%) 0 20px 50px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.login-card img {
  height: 20%;
  width: auto;
}

.login-card > * {
  width: 90%;
}
.options {
  display: flex;
  justify-content: space-between;
}
</style>