<template>
  <div class="adoptar">
    <div class="head"></div>
    <div class="mascotas">
      <div v-for="mascota in mascotas" :key="mascota.id">
        <div v-if="!mascota.adoptado" class="card">
          <p class="pet-name">{{ mascota.nombre }}</p>
          <div class="card-img-top" alt="Imagen de la mascota" :style="{ backgroundImage: 'url(' + mascota.imagen + ')' }"  ></div>
          <div class="card-body">
            <div class="pet-info">
              Sexo:
              <span v-if="mascota.sexo === 'H'">Hembra</span>
              <span v-else-if="mascota.sexo === 'M'">Macho</span>
              <br />
              Edad: {{ mascota.edad }} años
              <br />
              Tamaño:
              <span v-if="mascota.tamaño === 'P'">Pequeño</span>
              <span v-else-if="mascota.tamaño === 'M'">Mediano</span>
              <span v-else-if="mascota.tamaño === 'G'">Grande</span>
              <br />
              Personalidad: {{ mascota.personalidad }}
              <br />
              Esterilizado:
              <span v-if="mascota.esterilizado">Si</span>
              <span v-else>No</span>
              <br />
              Desparasitado:
              <span v-if="mascota.desparasitado">Si</span>
              <span v-else>No</span>
              <br />
              Salud: {{ mascota.salud }}
              <br />
              Descripcion:
              {{ mascota.descripcion }}
            </div>
            <button class="personality-button"><p>Adoptar</p></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Adoptar",
  data: function () {
    return {
      mascotas: [],
    };
  },
  methods: {
    loadAdoptar: function () {
      this.$router.push({ name: "adoptar" });
    },
    listaMascotas: function () {
      //let url = "https://bancoprue.herokuapp.com/mascotas/";
      let url = "https://adoptame-be.herokuapp.com/mascotas/";
      let config = { Headers: {} };
      axios
        .get(url, config)
        .then((response) => {
          this.mascotas = response.data;
        })
        .catch((error) => {
          swal.fire("", "Error, intente mas tarde", "error");
        });
    },
  },
  created: function () {
    this.listaMascotas();
  },
};
</script>
<style scoped>
.head {
  color: white;
  height: 50vh;
  background-image: url(../assets/perrosBalcon.jpg);
  background-size: cover;
  background-position: center;
}
.mascotas .card > * {
  display: block;
}

.mascotas {
  display: flex;
  flex-wrap: wrap;
  width: 100vw;
  justify-content: center;
  background-color: rgba(255, 244, 224, 0.473);
}

.card {
  border-radius: 30px;
  overflow: hidden;
  width: 20rem;
  margin: 3vh 3vw;
  box-shadow: 8px 4px 4px rgb(236, 208, 130);
}
.card-img-top {
  padding: 1%;
  width: inherit;
  height: 15rem;
  background-size: cover;
  background-position: center;
  margin: 1px auto;
  display: block;
}
.card p {
  margin: 0;
}

.pet-name {
  font-weight: 700;
  font-size: 1.8rem;
  text-align: center;
  color: rgb(118, 104, 241);
  text-shadow: 1px 2px 8px rgb(141, 135, 135);
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
  width: 0 auto;
  height: auto;
  margin: 2vh 0.4vh;
  font-size: 1.3rem;
  font-weight: 600;
  color: white;
  padding: 0;
}

.personality-button:hover {
  background-color: var(--azul-oscuro);
  color: var(--mostaza);
}

.personality-button p {
  margin: 1px 7px;
}
</style>