<template>
  <div class="clock">
    <div class="day">{{ day }}</div>
    <div class="second">{{ second }}</div>
  </div>
</template>

<script>
import dayjs from "dayjs";

export default {
  name: "clock",
  data() {
    return {
      day: "21-12-31",
      second: "23:59:59",
    };
  },
  mounted() {
    setInterval(() => {
      this.day = dayjs().format("YY-MM-DD");
      this.second = dayjs().format("HH:mm:ss");
    }, 1000);
  },
};
</script>

<style>
.clock {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-end;
  color: #fff;
  font-size: 3rem;
  user-select: none;
  font-family: Light;
}

.day,
.second {
  margin: 0 1.2rem 0 1.2rem;
  white-space: nowrap;
}
</style>