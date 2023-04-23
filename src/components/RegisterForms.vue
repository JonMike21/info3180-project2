<template>
  <form class="reg-form" method="POST" enctype="multipart/form-data" @submit.prevent="saveRegistry" id="registerForm">
    
    <div class="short">
      <div class="form-group mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" name="username" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" name="password" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="firstname" class="form-label">Firstname</label>
        <input type="text" name="firstname" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="lastname" class="form-label">Lastname</label>
        <input type="text" name="lastname" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="text" name="email" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="location" class="form-label">Location</label>
        <input type="text" name="location" class="form-control" />
      </div>
    </div>

    <div>
      <div class="form-group mb-3">
        <label for="biography" class="form-label">Biography</label>
        <textarea name="biography" class="form-control"></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="profile_photo" class="form-label">Photo</label>
        <input type="file" name="profile_photo" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <button type="submit" class="btn btn-primary" @change="onFileChange">Submit</button>
      </div>
    </div>

  </form>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "RegisterForms",
  setup() {
    let csrf_token = ref("");

    function getCsrfToken() {
      fetch('http://127.0.0.1:8080//api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          csrf_token.value = data.csrf_token;
        })
    }

    onMounted(() => {
      getCsrfToken();
    });

    function saveRegistry() {
      let registerForm = document.getElementById('registerForm');
      let form_data = new FormData(registerForm);
      console.log('CSRF Token:', csrf_token.value);
      fetch("http://127.0.0.1:8080//api/v1/register", {
        method: 'POST',
        body: form_data,
        headers: {
          'X-CSRFToken': csrf_token.value
        }
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log(data);
        })
        .catch(function (error) {
          console.log(error);
        });
    }

    return {
      csrf_token,
      saveRegistry,
    }
  }
}
</script>