<template>
    <div class="container3">
        <h1 class="h1">Login</h1>
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

<style>
.container3 {
    display: flex;
    flex-direction: column;
    margin-left: 15px;
    margin-right: 15px;
    margin: 0 auto;
    background-color: white;
    flex: 1;
    max-height: 450px;
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: left;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 2%;
    box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);
    padding: 15px;
}
</style>