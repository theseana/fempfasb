<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <Card name='Elahe Mohammadi' jobTitle="Industrial Engineer"  :isPrivate="true"/>
  <Card name='Sepehr Saie' jobTitle="Security EXpert" :isPrivate="false"/>
  <Card name='Foads' jobTitle="Space Engineer" :isPrivate="true"/>
</template>

<script>
import Card from './components/Card.vue'

export default {
  name: 'App',
  components: {
    Card
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
