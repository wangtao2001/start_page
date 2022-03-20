<template>
  <div class="site-info">
    版权所有©
    <a
      href="https://github.com/wangtao2001"
      style="margin-right: 0.3125rem"
      target="_blank"
      >王涛
    </a>
    <a href="https://beian.miit.gov.cn/">鄂ICP备2021017520号</a>
  </div>
</template>

<script>
export default {
  name: "site-info",
};
</script>

<style>
.site-info {
  color: #8e9094;
  margin-bottom: 1rem;
  font-size: 0.65rem;
  user-select: none;
  backdrop-filter: blur(2px) brightness(80%);
  padding: 0.1rem 0.5rem 0.1rem 0.5rem;
  border-radius: 1rem;
}

a,
a:link,
a:visited,
a:hover,
a:active {
  text-decoration: none;
  color: inherit;
  transition: 0.25s;
}

.site-info a:hover {
  color: #fff;
  transition: 0.25s;
}
</style>