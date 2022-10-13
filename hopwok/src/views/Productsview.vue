<script setup>
import TryComp from '@/components/TryComp.vue';
import Productviewid from './Productviewid.vue';
</script>
<template>
    <div > 
     <Productviewid id  = "id" />
    </div>
</template>
  
<style>

  @media (min-width: 1024px) {
    .products {
      min-height: 20vh;
      position: relative;
      left: -250px; top: -250px;
      display: flex;
      align-items: center;
    }
    

   
  }
</style>
  