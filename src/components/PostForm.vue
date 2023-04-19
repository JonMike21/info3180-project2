<template>
    <form method="POST" enctype="multipart/form-data" @submit.prevent="postData" id="postForm" action="/api/v1/users/{{ user_id }}/posts">
        
        <div class="form-group mb-3">
            <label for="photo" class="form-label">Photo</label>
            <input type="file" name="photo" class="form-control"  />
        </div>

        <div class="form-group mb-3">
            <label for="caption" class="form-label">Caption</label>
            <textarea name="caption" class="form-control"></textarea>
        </div>

        <div class="form-group mb-3">
            <button type="submit" class="btn btn-primary" @change="onFileChange">Submit</button>
        </div>
    </form>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
    name: "CreatePosts",
    props: {
        user_id: {
        type: Number,
        required: true
        }
    },
    setup(props) {
        let csrf_token = ref("");

        function getCsrfToken() {
            fetch('http://127.0.0.1:8080/api/v1/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    csrf_token.value = data.csrf_token;
            })
        }

        onMounted(() => {
            getCsrfToken();
        });

        function postData() {
            let postForm = document.getElementById('postForm');
            let form_data = new FormData(postForm);
            console.log('CSRF Token:', csrf_token.value);  
            fetch(`http://127.0.0.1:8080/api/v1/users/${props.user_id}/posts`, {
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
            postData,
        }
    }
}
</script>
