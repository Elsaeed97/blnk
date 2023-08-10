<template>
  <v-app>
    <v-main>
      <HelloWorld />
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
  import HelloWorld from '@/components/HelloWorld.vue'
  import Login from '@/components/Login.vue'
</script>
