<script setup>
import { RouterLink, RouterView } from 'vue-router'

import HelloWorld from './components/HelloWorld.vue'

</script>
<template>
  <header>
   

    <div class="navigation-bar">
     <HelloWorld msg="ungenericmart" />
    <div id ="menu dev">
    
       <nav >
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/products">Products</RouterLink>
      </nav>
    </div>
    </div>


    
      

</header>

 

<RouterView/>


</template>
  
  




<style scoped>
 @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');


*{
  font-family: 'Poppins', sans-serif;
}
header {
  overflow: hidden;
  background-color: #d9d9d9;
  line-height: .5;
  max-height: 100vh;
  
}
  
  .logo {
  
    margin: 0 auto 2rem 0;
    width: 5%;
    top :-15px;left:-70px;
  }
  
  nav {
    color: rgb(0, 0, 0);
  font-weight: 300;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-right: 10px;
  }
  
  nav a.router-link-exact-active {
    color: var(--color-text);
  }
  
  nav a.router-link-exact-active:hover {
    background-color: transparent;
  }
  
  nav a {
    display: inline-block;
    padding: 0 1rem;
    border-left: 1px solid var(--color-border);
  }
  
  nav a:first-of-type {
    border: 0;
  }
  
  @media (min-width: 1024px) {
    header {
      
      place-items: center;
    
    }
  
    .logo {
      margin: 0 2rem -10 0;
    }
  
 
  
    nav {
      text-align: left;
      margin-left: -1rem;
      font-size: 1rem;
  
      padding: 1rem 0;
      margin-top: 1rem;
    }
  }
  </style>
  