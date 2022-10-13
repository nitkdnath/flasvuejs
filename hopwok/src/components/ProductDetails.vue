<script setup>
import {ref, onMounted } from 'vue';

const props =  defineProps({
      msg :{
        type: String,
        required: true

      },
      image: {
        type: String,
        

      },
      Instock:{
        type: Boolean
        
        
      },

      image :{
        type:String
      },
  
        id:{
            type:Number
        }
     
    })
    const productid = ref({id: 0, image: "", product_name: "", product_rate: ""})

  
async function api(url) {
  const response = await fetch(url);
if (!response.ok) {
throw new Error(response.statusText);
}
return await response.json();
}
function getproduct() {
 
api(`http://127.0.0.1:5000/product/${props.id}/`)


   .then((data) => {productid.value = data})
   
   
    .catch(error => {console.log(error.toString())
  }
)  
}
onMounted(() => getproduct())

    </script>
    
    <template>
  
    <section>
      <main>
      <div class = "fetch" >
        <div class="container"> 
          <div class="card">
          <div class="imgBx">
          <p>{{productid.id}}</p>
            <img v-bind:src = "productid.image" >
          </div>
        <div class="contentBx">
           <h2>{{productid.product_name}}</h2>
        <div class="price">
           <h3>Price : ₹{{productid.product_rate}}</h3>
          
          
           
         </div>
         <a class ="a" href="http://127.0.0.1:5173/">Buy Now</a>
        <a class ="a" href="#">Add to cart</a>
    </div>
    </div>

</div> 
</div>

  </main>
  </section>
      
  </template>
    
    
    <style scoped>
    

body{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #131313;

}

.container{
  position: relative;
  display: flex;

 
  margin: 0.2em;
  padding: 0;
  list-style-type: none;

}
.card {


  gap: 2rem;
  padding: 0;
  list-style-type: none;
}
.container .card{
  position: relative;
  width: 320px;
  height: 450px;
  background: rgba(136, 105, 129, 0.39);
  border-radius: 20px;
  overflow: hidden;
  margin: 2em;
  left: -35px;
  flex-direction: row;

  list-style-type: none;
  
  
}

.container .card:before{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #3c383b;
  clip-path: circle(150px at 80% 20%);
  transition: 0.3s ease-in-out;
}

.container .card:hover:before{
  clip-path: circle(300px at 80% -20%);
}

.container .card:after{

  position: absolute;
  top: 30%;
  left: -20%;
  font-size: 12em;
  font-weight: 800;
  font-style: italic;
  color: rgba(101, 101, 100, 0.05)
}

.container .card .imgBx{
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10000;
  width: 50%;
  height: 120px;
  transition: 0.5s;
}

.container .card:hover .imgBx{
  top: 0%;
  transform: translateY(0%);
    
}

.container .card .imgBx img{
  position: absolute;
  top: 35%;
  left: 100%;
  transform: translate(-50%, -50%);
  width: 170px;
}

.container .card .contentBx{
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 100px;
  text-align: center;
  transition: 1s;
  z-index: 10;
}
.fetch {
    list-style: none;
    padding: 0;
    margin: 0;
    width:400px;

  
  
  }
.container .card:hover .contentBx{
  height: 210px;
}

.container .card .contentBx h2{
  position: relative;
  font-weight: 600;
  letter-spacing: 1px;
  color: #000;
  margin: 0;
}

.container .card .contentBx .price, .container .card .contentBx .color {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  transition: 0.5s;opacity: 0;
  visibility: hidden;
  padding-top: 0;
  padding-bottom: 0;
}

.container .card:hover .contentBx .price{
  opacity: 1;
  visibility: visible;
  transition-delay: 0.4s;
}

.container .card:hover .contentBx .color{
  opacity: 1;
  visibility: visible;
  transition-delay: 0.4s;
}

.container .card .contentBx .price h3, .container .card .contentBx .color h3{
  color: rgb(0, 0, 0);
  font-weight: 300;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-right: 10px;

}

.container .card .contentBx .price span{
  width: 26px;
  height: 26px;
  text-align: center;
  line-height: 26px;
  font-size: 14px;
  display: inline-block;
  color: #111;
  background: rgb(121, 102, 102);
  margin: 0 5px;
  transition: 0.5s;
  color: #111;
  border-radius: 4px;
  cursor: pointer;

}

.container .card .contentBx .price span:hover{
  background: #9bdc28;
}

.container .card .contentBx .color span{
  width: 20px;
  height: 20px;
  background: #ff0;
  border-radius: 50%;
  margin: 0 5px;
  cursor: pointer;
}

.container .card .contentBx .color span:nth-child(2){
  background: #9bdc28;
}

.container .card .contentBx .color span:nth-child(3){
  background: #03a9f4;
}

.container .card .contentBx .color span:nth-child(4){
  background: #e91e63;
}

.container .card .contentBx .a{
  display: inline-block;
  padding: 10px 20px;
  background: #23730f;
  border-radius: 4px;
  margin-top: 10px;
  text-decoration: none;
  font-weight: 600;
  color: #111;
  opacity: 0;
  transform: translateY(50px);
  transition: 0.5s;
  margin-right: 0.2cm;
  

}
a{
  color: rgb(0, 0, 0);
  font-weight: 300;
  font-size: 14px;

  letter-spacing: 2px;
  margin-right: 10px;
  top: -5px;
}
.container .card:hover .contentBx .a{
  opacity: 1;
  transform: translateY(0px);
  transition-delay: 0.75s;
  
}

   
    </style>
    
