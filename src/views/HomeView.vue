<script setup>
import { ref } from "vue";

let message = ref("Share photos of your favourite moments with friends, family and the world.")

</script>

<template>
  <div class="container1">
    <div class="card2">
      <img src="../../public/homepage.jpg" alt="homepage">
    </div>
    <div class="card1">
      <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
                      <h1>{{ message }}</h1> -->

      <h1 class="title" style="font-weight: bold; font-family: Brush Script MT;">
        <i class="fal fa-camera"></i> Photogram
      </h1>
      <div class="gram-line"></div>
      <p class="msg">{{ message }}</p>
      <div class="buttons">
        <router-link to="/register" class="btn btn-secondary">Register</router-link>
        <router-link to="/login" class="btn btn-primary">Login</router-link>
      </div>
    </div>
  </div>
</template>

<style>
.container1 {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-left: 15px;

  margin-right: 15px;
}

.msg {
  max-width: 85%;
}

.gram-line {
  border-bottom: 1px solid #ccc;
  width: 85%;
  margin-top: 10px;
  margin-bottom: 10px;
}

.card1 {
  flex: 1;
  max-height: 450px;
  width: 50%;
  border: 1px solid #ccc;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 2%;
  box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);
  padding: 15px;
}

.card2 {
  flex: 1;
  max-height: 450px;
  width: 50%;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 2%;

}

.card2 img {
  width: 100%;
  height: 100%;
  border-radius: 2%;
}

.buttons {
  display: flex;
  gap: 15px;
}

.btn-secondary {
  background-color: #7ed321;
}
</style>