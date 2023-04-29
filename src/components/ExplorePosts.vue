<template>
    <div class="explore-container">
        <div class="post-container">
            <div v-for="post in posts.slice().reverse()" :key="post.id">
                <div class="card explore">
                    <h2>{{ post.caption }}</h2>
                    <img :src="post.photo" alt="post image">
                    <p>{{ formatDate(post.created_at) }}</p>
                </div>
            </div>
        </div>
        <div class="postbtn-container">
            <router-link to="/posts/new" class="btn btn-primary">New Post</router-link>
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
    },
    methods: {
        formatDate(date) {
            const d = new Date(date);
            const options = { day: "numeric", month: "short", year: "numeric" };
            const parts = d.toLocaleDateString("en-US", options).split(" ");
            return `${parts[1]} ${parts[0].toUpperCase()}  ${parts[2]}`;
        }
    },
}
</script>

<style>
.explore-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
}

.post-container {
    flex-basis: 70%;
}

.postbtn-container {
    flex-basis: 25%;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin-top: 20px;
}

.card {
    margin-bottom: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,.1);
}

.explore img {
    max-width: 100%;
    margin-bottom: 10px;
}
</style>