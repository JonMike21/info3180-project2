<template>
    <form method="POST" enctype="multipart/form-data" @submit.prevent="loginuser" id="loginUser">
        
        <div class="form-group mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" name="username" class="form-control" />
        </div>

        <div class="form-group mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" name="password" class="form-control"  />
        </div>

        <div class="form-group mb-3">
            <button type="submit" class="btn btn-primary" @change="onFileChange">Login</button>
        </div>
    </form>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
    name: "LoginForms",
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

        function loginuser() {
            let loginUser = document.getElementById('loginUser');
            let form_data = new FormData(loginUser);
            console.log('CSRF Token:', csrf_token.value);  
            fetch("http://127.0.0.1:8080//api/v1/auth/login", {
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
            loginuser,
        }
    }
}
</script>