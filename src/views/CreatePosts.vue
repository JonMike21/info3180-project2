<template>
    <div class="container">
        <h1>New Post</h1>
        <CreatePosts />
    </div>
</template>
  
<script>
    import CreatePosts from "../components/PostForm.vue"
    export default {
        name: "NewPost",
        components: {
            CreatePosts
        }
    };
</script>