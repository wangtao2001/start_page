<template>
  <div class="register login-card">
    <img src="../assets/logo/logo.jpg" />
    <el-input
      class="username"
      v-model="username"
      placeholder="用户名：2-10位字母、数字、下划线"
    ></el-input>
    <el-input
      class="password"
      placeholder="密码：必须包含大小写字母和数字"
      v-model="password"
      show-password
      maxlength="10"
    ></el-input>
    <el-input
      class="password2"
      placeholder="重复密码"
      v-model="password2"
      show-password
      maxlength="10"
    ></el-input>
    <div class="options">
      <p class="tips">{{ tips }}</p>
      <el-link type="primary" style="font-size: 1rem" @click="login"
        >去登陆</el-link
      >
    </div>
    <el-button class="register-button" type="primary" @click="register"
      >注册</el-button
    >
  </div>
</template>

<script>
import axios from "axios"; // 使用axios库进行请求
axios.defaults.withCredentials = true;
export default {
  name: "register",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      tips: "",
    };
  },
  methods: {
    usernameCheck(name) {
      // 用户名格式验证
      // 2-10位字母、数字、下划线
      var regex = /^[a-zA-Z0-9_]{2,10}$/;
      return !regex.test(name);
    },
    passwordCheck(pwd) {
      // 密码格式验证
      // 必须包含大小写字母、数字、不能使用特殊字符
      var regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{2,10}$/;
      return !regex.test(pwd);
    },
    login() {
      this.$router.push({
        name: "login",
      });
    },
    register() {
      // 非空验证
      if (
        this.username === "" ||
        this.password === "" ||
        this.password2 === ""
      ) {
        this.$notify.error({
          title: "错误",
          message: "用户名或密码不能为空",
          position: "top-left",
        });
        this.password = "";
        this.password2 = "";
      }
      // 用户名格式验证
      else if (this.usernameCheck(this.username)) {
        this.$notify.error({
          title: "错误",
          message: "用户名格式错误",
          position: "top-left",
        });
        this.username = "";
        this.password = "";
        this.password2 = "";
      }
      // 密码格式验证
      else if (this.passwordCheck(this.password)) {
        this.$notify.error({
          title: "错误",
          message: "密码格式错误",
          position: "top-left",
        });
        this.password = "";
        this.password2 = "";
      }
      // 两次密码不一致
      else if (this.password != this.password2) {
        this.$notify.error({
          title: "错误",
          message: "两次密码不一致",
          position: "top-left",
        });
        this.password2 = "";
      }
      // 向服务器发请求
      else {
        const data = {
          mode: "register",
          data: {
            username: this.username,
            password: this.password,
          },
        };
        axios
          .post(`https://shuangchen.info/api/register/`, JSON.stringify(data))
          .then(
            (res) => {
              var resp = res.data;
              if (resp.code != 200) {
                // 注册失败
                this.$notify.error({
                  title: "错误",
                  message: resp.message,
                  position: "top-left",
                });
                this.password = "";
                this.password2 = "";
              } else {
                // 注册成功
                this.$notify({
                  title: "成功",
                  message: resp.message,
                  position: "top-left",
                  type: "success",
                });
                // 注册成功 跳转登录
                this.$router.push({
                  name: "login",
                });
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

<style scoped>
/*样式使用login组件的公用样式*/
.tips {
  color: #f56c6c;
  font-size: 0.8rem;
}
</style>