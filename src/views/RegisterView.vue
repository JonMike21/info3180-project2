<template>
    <div class="container4">
        <h1 class="h1">Register</h1>

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

<style>
.h1{
    margin: 0 auto;
}

.container4 {
    display: flex;
    flex-direction: column;
    margin-left: 15px;
    margin-right: 15px;
    margin: 0 auto;
}


.reg-form {
    display: flex;
    flex-wrap: wrap;
    width: 500px;
    max-width: 80%;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 2%;
    flex-direction: column;
    box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);
    padding-left: 15px;
    padding-right: 15px;
    margin: 0 auto;
    background-color: white;
    margin-bottom: 40px;
}

.form-label {
    font-weight: bold;

}

.short {
    display: flex;
    flex-wrap: wrap;
}

.form-group {
    flex-basis: 50%;
    padding: 10px;
}

.reg-btn-primary{
  background-color: #7ed321;
  width: 100%;
}
</style>