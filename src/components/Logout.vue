<template>
    <div class="container">
        <h2>Logout</h2>
        <p>Are you sure you would like to logout?</p>
        <div class="row col-md-12">
            <div class="col-md-6">
                <button class="form-control btn btn-primary" @click="logoutUser">Logout</button>
            </div>
            <div class="col-md-6">
                <button class="form-control" @click="lastPage">Go Back</button>
            </div>
        </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineEmits } from "vue";
  
  const emits = defineEmits(['notification' , 'type']);
  </script>
  
  <script>
  
  export default {
    name: 'Logout',
    methods: {
      logoutUser() {
        fetch('http://127.0.0.1:8080/api/v1/auth/logout', {
                method: "POST",
            })
                .then(response => {
                    localStorage.removeItem('token')
                    localStorage.removeItem('user_id')
                    setTimeout(() => {
                        console.log(localStorage.getItem('token'))
                        console.log('Timer completed!');
                        window.location.href = '/';
                    }, 3000);
                })
                .catch(error => {
                    console.log(error.response.data)
                })
      },
      lastPage() {
        this.$router.back()
      },
      
    }
  }
  </script>