<template>
    <form method="POST" enctype="multipart/form-data" @submit.prevent="loginUser" id="loginUser">
        <div v-if="loginStatus === 'success'" class="alert alert-success" role="alert">
            Login successful! You will be redirected shortly!
        </div>
        <div v-if="loginStatus === 'failed'" class="alert alert-danger" role="alert">
            Login failed. Please check your credentials.
        </div>
        <div class="form-group mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" name="username" class="form-control" />
        </div>

        <div class="form-group mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" name="password" class="form-control"  />
        </div>

        <div class="form-group mb-3">
            <button type="submit" class="btn btn-primary">Login</button>
        </div>
    </form>
</template>

<script>
import { ref, onMounted } from "vue";
let username = ref("");
let password = ref("");

export default {
    name: "LoginForm",
    setup() {
        let loginStatus = ref(null);

        function loginUser() {
            let loginUser = document.getElementById("loginUser");
            let formData = new FormData(loginUser);
            fetch("http://127.0.0.1:8080/api/v1/auth/login", {
                method: "POST",
                body: formData,
                headers: {
                    username: username.value,
                    password: password.value,
                },
            })
                .then((response) => {
                    if(response.ok){
                        return response.json()
                    } else{    
                        loginStatus.value = "failed";
                    }

                    
                })
                .then((data) => {
                    const userid =data.id
                    localStorage.setItem("user_id",userid)
                    const token = data.token
                    localStorage.setItem("token",token)
                    loginStatus.value = 'success';
                    setTimeout(() => {
                        console.log('Timer completed!');
                        window.location.href='/explore';
                    }, 3000);
                    console.log(data);
                })
                .catch((error) => {
                    console.log(error)
                });
        }

        return {
            loginStatus,
            loginUser,
        };
    },
};
</script>
