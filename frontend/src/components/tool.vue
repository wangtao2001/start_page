<template>
  <div class="item" @click="open">
    <div class="item-icon">
      <img :src="icon" />
    </div>
    <div class="item-name">
      <div>{{ name }}</div>
      <div class="item-intro">{{ intro }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "tool",
  props: ["link", "icon", "name", "intro"],
  methods: {
    open() {
      window.open(this.link, "_blank");
    },
  },
};
</script>

<style>
@media screen and (max-width: 600px) {
  .item {
    flex-direction: row !important;
  }

  .item-name {
    margin-left: 1rem;
    flex-direction: column;
    align-items: flex-start !important;
  }
}

.item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 1rem 2rem 1rem 2rem;
}

.item-icon {
  height: 6rem;
  width: 6rem;
  background-color: #fff;
  border-radius: 1.3rem;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.item-icon img {
  height: 80%;
  width: auto;
}

.item-name {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.item-name :first-child {
  color: white;
  font-weight: bold;
  margin-top: 0.5rem;
  font-size: 1.2rem;
}

.item-intro {
  color: white;
  font-size: 1rem;
  margin-top: 0.2rem;
  font-weight: 400;
}
</style>