<template>
<div class="evento">
<div class=head>
</div>
<div class="container">
  <ul class="slider">
    <li id="slide1">
      <img src="@/assets/fiestadisfraces.jpeg"/>
    </li>
    <li id="slide2">
      <img src="@/assets/jornadaesterilizacion.jpg"/>
    </li>
    <li id="slide3">
      <img src="@/assets/donacionalimentos.jpg"/>
    </li>
  </ul>
  <ul class="menu">
    <li>
      <a href="#slide1" class="yellow-button">Fiesta de disfraces</a>
    </li>
    <li>
      <a href="#slide2"  class="yellow-button">Jornada de esterilización</a>
    </li>
     <li>
      <a href="#slide3" class="yellow-button">Donación de alimentos</a>
    </li>
  </ul>
</div>
</div>
</template>
<style scoped>
.head {
  height: 28vh;
  background-image: url(../assets/perroSofa.jpg);
  background-size: cover;
  background-position: center;
}
body{
  background-color: lightgrey;
  font-family: sans-serif;
}

.container{
  margin: 5vh auto;
  background-color: white;
  width:70rem;
  padding: 30px;
}

ul, li {
    padding: 0;
    margin: 0;
    list-style: none;
}

ul.slider{
  position: relative;
  width: 735px;
  height: 300px;
  overflow: hidden;
  margin: 0 auto;
}




ul.slider li {
    position: absolute;
    left: 0px;
    top: 0px;
    opacity: 0;
    width: inherit;
    height: inherit;
    transition: opacity .5s;
    background:#fff;
}
ul.slider li img{
  width: 100%;
  height: 300px;
  object-fit: cover;
}

ul.slider li:first-child {
    opacity: 1; /*Mostramos el primer <li>*/
}

ul.slider li:target {
    opacity: 1; /*Mostramos el <li> del enlace que pulsemos*/
}

.menu{
  text-align: center;
  margin: 20px;
}

.menu li{
  display: inline-block;
  text-align: center;
  margin: 20px 5px;
}
.yellow-button {
  text-decoration: none;
  font-size: 3vh;
  font-weight: 700;
  background-color: var(--mostaza);
  width: auto;
  height: auto;
  border-style: none;
  border-radius: 30px!important;
  margin: 0 auto;
  padding: 2px 10px;
  -webkit-border-radius: 30px!important;
  -moz-border-radius: 30px!important;
  -ms-border-radius: 30px!important;
  -o-border-radius: 30px!important;
  transition: all 300ms ease-in-out;
  color:var(--azul-oscuro)!important;
}

.yellow-button:hover {
  background-color: var(--azul-oscuro);
  color: var(--mostaza)!important;
  font-size: 3.2vh;
}



</style>