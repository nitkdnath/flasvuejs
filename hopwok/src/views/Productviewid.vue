<script setup>
import ProductDetails from '@/components/ProductDetails.vue';
</script>
<template>
    <div >
      <ProductDetails :id  = "id" /> 
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
  
