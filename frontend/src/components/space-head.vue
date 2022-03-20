<template>
  <div class="space-head">
    <div class="title">
      <img src="../assets/logo/logo.jpg" />
      <div class="name">
        <div class="a">个人空间</div>
        <div class="b">Personal Space</div>
      </div>
    </div>
    <div round class="account" @click="drawer = true" type="primary">
      账号管理
    </div>
    <el-drawer
      class="drawer"
      title="账号管理"
      :visible.sync="drawer"
      direction="rtl"
      :append-to-body="true"
      :modal-append-to-body="false"
    >
      <account-manage></account-manage>
    </el-drawer>
  </div>
</template>

<script>
import accountManage from "./account-manage.vue";
export default {
  components: { accountManage },
  name: "space-head",
  data() {
    return {
      drawer: false,
    };
  },
};
</script>

<style>
.space-head {
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: 5rem;
  color: white;
}

.title {
  display: flex;
  align-items: center;
  height: 100%;
  margin-left: 1rem;
}

.title img {
  height: 60%;
  width: auto;
}

.title .name {
  margin-left: 1.2rem;
  font-weight: bold;
  font-size: 1.3rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.title .name .b {
  font-size: 0.9rem;
  font-weight: 400;
}

.space-head .account {
  margin-right: 1rem;
  margin-top: 1.2rem;
  height: 2.5rem;
  width: 6rem;
  color: white;
  background-color: rgba(255, 255, 255, 0.2);
  transition: 0.2s;
  padding-left: 0.8rem;
  padding-right: 0.8rem;
  border-color: white;
  border-radius: 2rem;
  text-align: center;
  line-height: 2.3rem;
}

.account:hover {
  color: #409eff;
}

@media screen and (max-width: 600px) {
  .el-drawer {
    width: 100% !important;
  }
}
</style>