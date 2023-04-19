<template>
    <div class="container">
        <h1>Login</h1>
        <LoginForms />
    </div>
</template>
  
<script>
    import LoginForms from "../components/LoginForm.vue"
    export default {
        name: "LoginUser",
        components: {
            LoginForms
        }
    };
</script>