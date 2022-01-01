<template>
  <div class="inicio">
    <div class="portada">
      <div class="texto-centrado">
        <h1>Encuentra tu compañero ideal!</h1>
        <p>
          Realiza el test de personalidad para<br />
          encontrar a tu amigo de vida
        </p>
        <a v-on:click="loadQuiz"><button class="yellow-button">Empezar</button></a>
      </div>
      <div class="opciones-iniciales" v-if="!is_auth">
        <button v-on:click="loadAdoptar" class="yellow-option">
          <img src="@/assets/catNdog.svg" alt="Perro y Gato" />
          <p>Adoptar</p>
        </button>
        <button v-on:click="loadDonanteHome" class="yellow-option">
          <img src="@/assets/donar.svg" alt="Perro y Gato" />
          <p>Donar</p>
        </button>
        <button v-on:click="loadEventos" class="yellow-option">
          <img src="@/assets/calendario.svg" alt="Perro y Gato" />
          <p>Eventos</p>
        </button>
      </div>
    </div>

    <div class="adopcion">
      <h2>Amigos buscando un hogar</h2>
      <div class="mascotas">
        <div class="card" v-for="(mascota, index) in mascotas" :key="mascota.id ">
          <div v-if="index <= 5">
          <div class="card-img-top" :style="imagenMascota(index)" ></div>
          <div class="card-body">
            <p class="pet-name">{{ mascota.nombre }}</p>
            <p class="pet-info" v-if="mascota.edad != 1">{{ mascota.edad }} Años - <span v-if="mascota.sexo === 'H'">Hembra</span><span v-else>Macho</span></p>
            <p class="pet-info" v-else>{{ mascota.edad }} Año - <span v-if="mascota.sexo === 'H'">Hembra</span><span v-else>Macho</span> </p>
            <div class="card-line"></div>
            <div class="personality">
              <button class="personality-button"><p>Jugeton</p></button>
              <button class="personality-button"><p>Jugeton</p></button>
              <button class="personality-button"><p>Jugeton</p></button>
            </div>
          </div>
        </div>
        </div>
      </div>
      <button v-on:click="loadAdoptar" class="yellow-button boton-centrado">Ver mas</button>
    </div>
    <section>
      <h1>Ellos tambien merecen ser amados</h1>
    </section>
    <hr class="yellow-line" />
    <div class="eventos">
      <h2>Eventos</h2>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col">
          <div class="card h-100">
            <h4 class="card-date">Mes dia, año</h4>
            <img
              src="@/assets/perroEvento.png"
              class="card-img-top"
              alt="..."
            />
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-author">Autor</p>
              <div class="card-line"></div>
              <p class="card-text">
                This is a longer card with supporting text below as a natural
                lead-in to additional content. This content is a little bit
                longer.
              </p>
              <button class="card-button">Leer mas</button>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card h-100">
            <h4 class="card-date">Mes dia, año</h4>
            <img
              src="@/assets/perroEvento.png"
              class="card-img-top"
              alt="..."
            />
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-author">Autor</p>
              <div class="card-line"></div>
              <p class="card-text">
                This is a longer card with supporting text below as a natural
                lead-in to additional content. This content is a little bit
                longer.
              </p>
              <button class="card-button">Leer mas</button>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card h-100">
            <h4 class="card-date">Mes dia, año</h4>
            <img
              src="@/assets/perroEvento.png"
              class="card-img-top"
              alt="..."
            />
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-author">Autor</p>
              <div class="card-line"></div>
              <p class="card-text">
                This is a longer card with supporting text below as a natural
                lead-in to additional content. This content is a little bit
                longer.
              </p>
              <button class="card-button">Leer mas</button>
            </div>
          </div>
        </div>
      </div>
      <button class="yellow-button">Ver mas</button>
    </div>
    <hr class="yellow-line" />
    <div class="opiniones">
      <div class="opinion-usuario">
        <div class="imagen-circular">
          <img src="@/assets/señor.png" alt="Señor sonriendo" />
        </div>
        <h2>
          "Durante la pandemia me senti muy solo, pero despues de realizar el
          test encontre un amigo de vida"
        </h2>
      </div>
      <div class="opinion-usuario">
        <div class="imagen-circular">
          <img src="@/assets/mujer1.png" alt="Mujer joven sonriendo" />
        </div>
        <h2>
          “Realice el test y me hicieron match con la mascota mas perfecta del
          mundo, nunca me habia sentido tan completa”
        </h2>
      </div>
      <div class="opinion-usuario">
        <div class="imagen-circular">
          <img src="@/assets/mujer2.png" alt="Señora sonriendo" />
        </div>
        <h2>“Se sintio como encontrar mi media naranja”</h2>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data: function () {
    return {
      is_auth: false,
      mascotas: [],
      estilo: {},
    };
  },
  methods: {
    loadInicio: function () {
      this.$router.push({ name: "inicio" });
    },
    loadDonanteHome: function () {
      this.$router.push({ name: "donantehome" });
    },
    loadQuiz: function () {
      this.$router.push({ name: "quiz" });
    },
    loadAdoptar: function () {
      this.$router.push({ name: "adoptar" });
    },
    loadEventos: function(){
      this.$router.push({ name: "eventos" })
    //Para los props y emit
    },
    completedIniciarSesion: function () {
      this.is_auth = true;
    },
    logoutSesion: function () {
      this.is_auth = false;
    },
    listaMascotas: function () {
      let url = "https://adoptame-be.herokuapp.com/mascotas/";
      let config = { Headers: {} };
      axios
        .get(url, config)
        .then((response) => {
          this.mascotas = response.data;
          this.mascotas = this.shuffleArray(this.mascotas);
          console.log(this.mascotas);
        })
        .catch((error) => {
          swal.fire("", "Error, intente mas tarde", "error");
        });
    },
    shuffleArray:function(array) {
      for (let i = array.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [array[i], array[j]] = [array[j], array[i]];
      }
      return array
    },
    imagenMascota:function(index){
      let imagen = {
        'background-image': 'url('+ this.mascotas[index].imagen + ')'
      }
      if(this.mascotas[index].nombre == "otto") {
          imagen['background-position'] = 'center 22rem';
      }else if(this.mascotas[index].nombre == "rex"){
          imagen['background-position'] = 'center -5rem';
      }
      return imagen
    }
  },
  created: function () {
    this.loadInicio();
    this.listaMascotas();
  },
};
</script>


<style scoped>


:root {
  --mostaza: #e9d458;
  --azul-oscuro: #1b1e37;
}

body {
  overflow-x: hidden;
}
*{
  opacity: 1;
}

.portada {
  color: white;
  height: 88.5vh;
  width: 100%;
  background-image: url(../assets/perroSofa.jpg);
  background-size: cover;
  background-position: center;
}

.texto-centrado {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  letter-spacing: 2px;
  height: inherit;
  align-content: center;
}

.texto-centrado h1 {
  font-size: 8vh;
  font-weight: 600;
  text-shadow: 1px 2px 8px black;
}

.texto-centrado p {
  font-size: 3vh;
  font-weight: 500;
  text-shadow: 2px 1.5px 5px black;
}

.yellow-button {
  font-size: 3.5vh;
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
  font-size: 3.6vh;
}

.yellow-option {
  background-color: var(--mostaza);
  color: var(--azul-oscuro);
  width: auto;
  height: auto;
  border-style: none;
  border-radius: 30px;
  -webkit-border-radius: 30px;
  -moz-border-radius: 30px;
  -ms-border-radius: 30px;
  -o-border-radius: 30px;
}
.yellow-option img {
  margin: 1vh 2.8vw;
  width: 10rem;
}

.yellow-option p {
  font-weight: 700;
  font-size: 5vh;
}

.opciones-iniciales {
  display: flex;
  justify-content: center;
  position: relative;
  top: -18vh;
  width: 100%;
}

.opciones-iniciales button {
  margin: 0 2vw;
}

.adopcion {
  margin-top: 20vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.adopcion h2 {
  color: var(--azul-oscuro);
  font-size: 5vh;
  font-weight: 600;
  text-align: center;
}

/*--------------------------Tarjeta de mascotas-------------------*/

.mascotas .card>*{
  display: block;
}

.mascotas {
  display: flex;
  flex-wrap: wrap;
  width: 85.46vw;
  justify-content: center;
}
.card-img-top {
  width: inherit;
  height: 12rem;
  background-color:red;
    background-size: cover;
  background-position: center;
}

.card {
  border-radius: 30px;
  overflow: hidden;
  width: 303.7px;
  margin: 3vh 3vw;
}

.card p {
  margin: 0;
}

.pet-name {
  font-weight: 700;
  font-size: 1.8rem;
}
.pet-info {
  font-weight: 700;
  font-size: 1.3rem;
}

.card-line {
  width: inherit;
  height: 3px;
  border-radius: 30px;
  background-color: var(--azul-oscuro);
}

.personality-button {
  border: none;
  background-color: rgb(118, 104, 241);
  border-radius: 20px;
  width: auto;
  height: auto;
  margin: 2vh 0.4vh;
  font-size: 1.3rem;
  font-weight: 600;
  color: white;
  padding: 0;
}

.personality-button p {
  margin: 1px 7px;
}

/*--------------------------Imagen Divisora-------------------*/

section {
  height: 30vh;
  background-image: url(../assets/perroAcariciando.jpg);
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 15vh;
}

section h1 {
  color: white;
  font-size: 6vh;
  text-shadow: 3px 4px 10px black;
}

.yellow-line {
  border: none;
  height: 6px;
  width:35vw;
  background-color: var(--mostaza);
  margin: 70px auto;
}

/*--------------------------Tarjeta de eventos-------------------*/


.eventos {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  margin: 0 auto;
  width: 70%;
}

.eventos h2 {
  font-weight: 600;
  font-size: 2rem;
}


.row>* {
  padding: 0;
  text-align: left;
  margin-top: 5vh;
  margin-bottom: 5vh;
}

.h-100 {
  padding: 0 0;
  width: 303.7px;
}

.col .card-text {
  font-size: 1.2rem;
}

.col .card {
  border-radius: 0;
  margin:0 auto;
}

.card-date {
  position: absolute;
  top: 10rem;
  padding: 0 1rem;
  color: white;
  text-shadow: 3px 2px 4px black;
}

.col .card-title {
  font-weight: 600;
  font-size: 1.5rem;
  margin-bottom: 0;
}

.col .card-author {
  font-weight: 600;
  color: rgb(65, 65, 65);
}
.col .card-line {
  background-color: rgb(65, 65, 65);
  height: 1.7px;
  margin-bottom:10px;
}

.col .card-button {
  border:none;
  background: transparent;
  font-weight: 600;
  font-size: 1.4rem;
  width: auto;
  height: auto;
  padding: 0;
}

/*--------------------------Opiniones-------------------*/

.opiniones {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  text-align: center;
}

.opinion-usuario {
  margin: 2rem 5vw;
}

.imagen-circular {
  width: 15vw;
  border-radius: 100%;
  overflow: hidden;
  -webkit-border-radius: 100%;
  -moz-border-radius: 100%;
  -ms-border-radius: 100%;
  -o-border-radius: 100%;
}

.imagen-circular img {
  width: inherit;
}

.opinion-usuario h2 {
  width: 13vw;
  margin: 1rem 1vw;
  font-weight: 600;
  font-size: 1.5rem;
  text-align: center;
}



/*--------------------------Responsive-------------------*/

@media (max-width: 1316px){
  .imagen-circular {
  width: 19vw;
}

.opinion-usuario h2 {
  width: 17vw;
  font-size: 1.3rem;
}

    .yellow-line {
    width: 60vw;
  }
    .mascotas .card:nth-child(-n+2){
    display: none;
  }
    section {
    height: 20vh;
  }
  .eventos {
  width: 100%;
}
}

@media (max-width: 767px) {
    .imagen-circular {
  width: 30vw;
}

.opinion-usuario h2 {
  width: 28vw;
  font-size: 1.2rem;
}
  .yellow-line {
    width: 80vw;
  }
    .mascotas .card:nth-child(-n+3){
    display: none;
  }
  .opciones-iniciales {
    top: -19%;
  }
  .yellow-option img {
    width: 21vw;
  }

  .yellow-option p {
    font-size: 4vw;
  }
    section h1 {
    font-size: 7vw;
  }
}

@media (max-width: 536px) {

  .opiniones .opinion-usuario:nth-child(2){
    display: none;
  }

      .imagen-circular {
  width: 40vw;
}

.opinion-usuario h2 {
  width: 38vw;
  font-size: 1.3rem;
}

  .opciones-iniciales {
    top: -15%;
  }
  .yellow-option {
    width: auto;
    height: auto;
    top: -10vh;
  }
  .yellow-option img {
    margin: 1vh 2.8vw;
    width: 23vw;
  }

  .yellow-option p {
    font-weight: 700;
    font-size: 5.5vw;
  }
  .h-100 {
  margin: 0;
  }

}
</style>
