<template>
    <div class="container">
        <div class="card">
            <div>
                <p><strong>Username:</strong> {{ user.username }}</p>
                <p><strong>Name:</strong> {{ user.firstname }} {{ user.lastname }}</p>
                <p><strong>Location:</strong> {{ user.location }}</p>
                <p><strong>Biography:</strong> {{ user.biography }}</p>
                <p><strong>Profile Photo:</strong><img v-bind:src="'http://localhost:8080/'+ user.profile_photo" alt="image post" class="card-img-top"></p>
                <p><strong>Joined On:</strong> {{ user.joined_on }}</p>
                <p><strong>Number of Posts:</strong> {{ user.numposts }}</p>
            </div>
        </div>
        <hr>
        <h1>Posts</h1>
        <div>
            <ul>
                <li v-for="post in user_posts" :key="post.id">
                    <p><strong>Caption:</strong> {{ post.caption }}</p>
                    <p><strong>Photo:</strong> <img :src="post.photo" alt="Post Photo"></p>
                    <p><strong>Created At:</strong> {{ formatDate(post.created_at) }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

const user_id = localStorage.getItem('user_id')
const token = localStorage.getItem('token');

export default {
    name: "UserProfiles",
    data() {
        return {
            user: {},
            user_posts: []
        };
    },
    mounted() {
        axios.get(`/api/v1/users/${user_id}/posts`),{
            headers: {
                'Content-Type': 'multipart/form-data',
                'Authorization': `Bearer ${token}`,
                'Access-Control-Allow-Origin': '*',
            }
        }
        .then(response => {
            console.log(response)
            this.user = response.data.data.user_info;
            this.user_posts = response.data.data.user_posts;
        })
        .catch(error => {
            console.log(error);
        });
    },
    filters: {
        formatDate(value) {
            const date = new Date(value);
            const options = {
                year: 'numeric',
                month: 'short',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
            };
            return date.toLocaleString('en-US', options);
        },
    },
};
</script>
