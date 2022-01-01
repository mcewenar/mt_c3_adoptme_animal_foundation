<template>
  <div class="adoptables">
    <div class="head"></div>
    <div>
      <button v-on:click="loadAgregarMascota" class="yellow-button">
        Añadir mascota
      </button>
    </div>
    <div class="mascotas">
      <table class="tabla">
        <tr>
          <th>Foto</th>
          <th>Nombre</th>
          <th>Sexo</th>
          <th>Edad</th>
          <th>Tamaño</th>
          <th>Personalidad</th>
          <th>Esterilizado</th>
          <th>Desparasitado</th>
          <th>Salud</th>
          <th>Descripcion</th>
          <th>Adoptado</th>
          <th>Actualizar</th>
          <th>Borrar</th>
        </tr>
        <tr v-for="mascota in mascotas" :key="mascota.id">
          <td>
            <img class="img" :src="mascota.imagen" alt="" />
          </td>
          <td>{{ mascota.nombre }}</td>
          <td>
            <span v-if="mascota.sexo === 'H'">Hembra</span>
            <span v-else-if="mascota.sexo === 'M'">Macho</span>
          </td>
          <td>{{ mascota.edad }}</td>
          <td>
            <span v-if="mascota.tamaño === 'P'">Pequeño</span>
            <span v-else-if="mascota.tamaño === 'M'">Mediano</span>
            <span v-else-if="mascota.tamaño === 'G'">Grande</span>
          </td>
          <td>{{ mascota.personalidad }}</td>
          <td>
            <span v-if="mascota.esterilizado">Si</span>
            <span v-else>No</span>
          </td>
          <td>
            <span v-if="mascota.desparasitado">Si</span>
            <span v-else>No</span>
          </td>
          <td>{{ mascota.salud }}</td>
          <td>{{ mascota.descripcion }}</td>
          <td>
            <span v-if="mascota.adoptado">Si</span>
            <span v-else>No</span>
          </td>
          <td>
            <button class="botonActualizar" v-on:click="loadActualizarMascota(mascota.id)">x</button>
          </td>
          <td>
            <button class="botonBorrar" v-on:click="borrarMascota(mascota.id)">x</button>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Adoptables",
  data: function () {
    return {
      mascotas: [],
    };
  },
  methods: {
    loadAgregarMascota: function () {
      this.$router.push({ name: "agregarmascota" });
    },
    loadActualizarMascota: function (id) {
      this.$router.push({ name: "actualizarmascota", params: { Id: id }});
    },
    listaMascotas: function () {
      //  let url = "http://127.0.0.1:8000/mascotas/"
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
    borrarMascota: async function (id) {
      try {
        let url = "https://adoptame-be.herokuapp.com/mascota/" + id;
        let config = { Headers: {} };
        await axios.delete(url, config);
        this.listaMascotas();
        swal.fire("", "Borrado exitoso!!!", "success");
      } catch (error) {
        swal.fire("", "Error inesperado", "error");
      }
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
.botonBorrar {
  background-color: rgb(212, 36, 36);
}
.yellow-button {
  color: var(--azul-oscuro);
  font-size: 1.3vw;
  font-weight: 600;
  background-color: var(--mostaza);
  border-style: none;
  border-radius: 30px;

  width: 30%;
  height: 6.5vh;
  border: 1px solid #e5e7e9;
  padding: 10px 25px;

  margin: 5px 0 25px 0;
  float: right;
}

.yellow-button:hover {
  background-color: var(--azul-oscuro);
  color: var(--mostaza);
}
.img {
  padding: 1%;
  width: 200px;
  height: 200px;
  margin: 1px auto;
  display: block;
}
.tablee {
  border-collapse: collapse;
  padding: 2%;
  margin: 2% auto;
  text-align: center;
}
.tabla {
  border: 3px solid;
  margin-top: 6%;
  margin-left: 30px;
  width: 80%;
  text-align: center;
  border-collapse: collapse;
}
th {
  border-radius: 5px;
  border: 2px solid;
}
td {
  border-radius: 5px;
  border: 1px solid;
}
</style>