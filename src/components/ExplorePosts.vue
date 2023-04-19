<template>
    <div>
        <div class="postbtn">
            <router-link to="/posts/new" class="btn btn-primary">New Post</router-link>
        </div>
        <div v-for="post in posts" :key="post.id">
            <div class="cards">
                <h2>{{ post.caption }}</h2>
                <img :src="post.photo" alt="post image">
                <p>{{ post.created_at }}</p>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    name: "Explore",
    data() {
        return {
        posts: []
        }
    },
    mounted() {
        fetch('http://127.0.0.1:8080/api/v1/posts')
        .then(response => response.json())
        .then(data => {
            this.posts = data.data
        })
        .catch(error => {
            console.log(error)
        })
    }
}
</script>