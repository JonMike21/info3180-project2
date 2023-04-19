<template>
    <div class="container">
        <h1>Register</h1>
        <RegisterForms />
    </div>
</template>
  
<script>
    import RegisterForms from "../components/RegisterForms.vue"
    export default {
        name: "AddRegistry",
        components: {
            RegisterForms
        }
    };
</script>