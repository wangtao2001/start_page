<template>
  <div class="account-manage">
    <div class="wel">
      <p style="font-weight: bold">欢迎：</p>
      <p>{{ username }}</p>
    </div>
    <div class="manage">
      <p>更多账号设置敬请期待</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "account-manage",
  data() {
    return {
      username: "",
    };
  },
  mounted() {
    const data = {
      mode: "userInfo",
      data: ["username"],
    };
    axios
      .post(`https://shuangchen.info/api/userInfo/`, JSON.stringify(data))
      .then((res) => {
        this.username = res.data.data.username;
      });
  },
};
</script>

<style>
.account-manage {
  padding-left: 1.3rem;
}
.wel {
  display: flex;
  margin-bottom: 1rem;
}

.manage {
  color: #83868b;
}
</style>