<script setup>
import { ref } from "vue";

let message = ref("Share photos of your favourite moments with friends, family and the world.")

</script>

<template>
    <div class="container">
      <div class="card">
        <img src="../../public/homepage.jpg" alt="homepage">
      </div>
      <div class="card">
        <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
        <h1>{{ message }}</h1> -->
          <h1 class="title">Photogram</h1>
          <hr>
          <p>{{ message }}</p>
          <div class="buttons">
            <router-link to="/login" class="btn btn-primary">Login</router-link>
            <router-link to="/register" class="btn btn-secondary">Register</router-link>
          </div>
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
</style>