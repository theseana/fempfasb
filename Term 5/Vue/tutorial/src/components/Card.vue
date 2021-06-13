<template>
    <div class="card">
        <img src="img_avatar.png" alt="Avatar" style="width:100%">
        <div class="container">
            <h4><b>{{ name }}</b>
            
            </h4>
            <span v-if="isPrivate">&#128274;</span>
            <span v-else>(Open)</span>
            <p>{{ jobTitle }}</p> 

        </div>
    </div>
</template>

<script>
export default {
    name: 'Card',
    props:{
        name: String,
        jobTitle: String,
        isPrivate: Boolean
    }
}
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 300px;
  float: left;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.container {
  padding: 2px 16px;
}
</style>