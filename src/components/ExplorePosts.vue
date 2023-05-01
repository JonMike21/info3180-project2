<template>
    <div class="explore-container">
        <div class="post-container">
            <div v-for="post in posts.slice().reverse()" :key="post.id">
                <div class="card explore">
                    <h6>{{ username }}</h6>
                    <img v-bind:src="'http://localhost:8080'+ post.photo" alt="image post" class="card-img-top"> 
                    <p>{{ post.caption }}</p>
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

const username = localStorage.getItem('username')
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
                this.username = username
                this.posts = data.data
                this.posts.forEach(post => {
                    fetch(`http://127.0.0.1:8080/api/v1/photo/${post.photo}`)
                        .then(response => response.blob())
                        .then(blob => {
                            post.photo = URL.createObjectURL(blob)
                        })
                        .catch(error => {
                            console.log(error)
                        })
                })
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