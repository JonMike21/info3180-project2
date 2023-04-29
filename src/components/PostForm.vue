<template>
    <form method="POST" enctype="multipart/form-data" @submit.prevent="postData" id="postForm" >
        <div v-if="postStatus === 'success'" class="alert alert-success" role="alert">
            Post made successfuly! Redirecting to the explore page!
        </div>
        <div v-if="postStatus === 'failed'" class="alert alert-danger" role="alert">
            Something weng wrong in posting, try again...
        </div>
        <div v-if="postStatus === 'fail-safe'" class="alert alert-danger" role="alert">
            This user is not logged in. You will now be redirected...
        </div>
        <div class="form-group mb-3">
            <label for="photo" class="form-label">Photo</label>
            <input type="file" name="photo" class="form-control" required/>
        </div>

        <div class="form-group mb-3">
            <label for="caption" class="form-label">Caption</label>
            <textarea name="caption" class="form-control" required></textarea>
        </div>

        <div class="form-group mb-3">
            <button type="submit" class="form-control btn btn-primary">Submit</button>
        </div>
    </form>
</template>


<script setup>
import axios from 'axios'
import { ref, onMounted, defineEmits } from "vue";
import { RouterLink } from "vue-router";

const emit = defineEmits(['notification', 'type']);


const token = localStorage.getItem('token');
const userId = localStorage.getItem('user_id');
const postStatus = ref(null);

function postData() {
    let postForm = document.getElementById("postForm");
    let formData = new FormData(postForm);

    axios.post(`http://127.0.0.1:8080/api/v1/users/${userId}/posts`, formData, {
        headers: {
        'Content-Type': 'multipart/form-data',
        'Authorization': `Bearer ${token}`,
        'Access-Control-Allow-Origin': '*',
        }
    })
    .then(response => {
        console.log(response.data);
        postStatus.value = 'success';
        setTimeout(() => {
            console.log('Timer completed!');
            window.location.href='/explore';
        }, 3000);
    })
    .catch(error => {
        if (userId != null) {
            postStatus.value = 'failed';
        } else {
            postStatus.value = 'fail-safe';
            setTimeout(() => {
                window.location.href='/login';
            }, 3000);
        }
    });
    return{
        postStatus,
    }
}
function onFileChange(e) {
    this.photo = e.target.files[0]
}

</script>