<template>
  <div class="agregar-mascota">
    <div class="head"></div>
    <div class="container-formulario">
      <h1>Formulario agregar mascota:</h1>
      <form v-on:submit.prevent="processAgregarMascota">
        <br />
        <label>Nombre: </label>
        <input
          v-model="formularioAgregarMascota.nombre"
          type="text"
          placeholder="Nombre"
          class="entrada"
        />
        <br />
        <label for="especie">Especie: </label>
        <select
          v-model="formularioAgregarMascota.especie"
          id="especie"
          name="especie"
        >
          <option value="G">Gato</option>
          <option value="P">Perro</option>
        </select>
        <br />
        <label>Edad (años): </label>
        <input
          v-model="formularioAgregarMascota.edad"
          type="number"
          placeholder="Años"
          class="entrada"
        />
        <br />
        <label for="tamaño">Tamaño: </label>
        <select
          v-model="formularioAgregarMascota.tamaño"
          id="especie"
          name="especie"
        >
          <option value="P">Pequeño</option>
          <option value="M">Mediano</option>
          <option value="G">Grande</option>
        </select>
        <br />
        <label for="sexo">Sexo: </label>
        <select v-model="formularioAgregarMascota.sexo" id="sexo" name="sexo">
          <option value="H">Hembra</option>
          <option value="M">Macho</option>
        </select>
        <br />
        <label>Esterilizado: </label>
        <input
          v-model="formularioAgregarMascota.esterilizado"
          type="checkbox"
          name="esterilizado"
          id="esterilizado"
        />
        <br />
        <label>Desparasitado: </label>
        <input
          v-model="formularioAgregarMascota.desparasitado"
          type="checkbox"
          name="desparasitado"
          id="desparasitado"
        />
        <br />
        <label>Personalidad: </label>
        <input
          v-model="formularioAgregarMascota.personalidad"
          type="text"
          placeholder="Personalidad"
          class="entrada"
        />
        <br />
        <label>Descripción: </label>
        <input
          v-model="formularioAgregarMascota.descripcion"
          type="text"
          placeholder="Descripción"
          class="entrada"
        />
        <br />
        <label>Salud: </label>
        <input
          v-model="formularioAgregarMascota.salud"
          type="text"
          placeholder="Salud"
          class="entrada"
        />
        <br />
        <label>Imagen: </label>
        <input
          class="entrada"
          type="file"
          @change="getImage"
          accept="image/*"
        />
        <br />
        <br />
        <button type="submit">Guardar</button>
        <input v-on:click="cancelar" type="button" value="Cancelar" class="botonCancelar">
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "agregarmascota",
  data: function () {
    return {
      formularioAgregarMascota: {
        nombre: "",
        especie: "",
        edad: 0,
        tamaño: "",
        sexo: "",
        esterilizado: "",
        desparasitado: "",
        personalidad: "",
        //personalidades: "",
        descripcion: "",
        salud: "",
        imagen: null,
      },
    };
  },
  methods: {
    crear(file) {
      var image = new Image();
      var reader = new FileReader();
      var vm = this;
      console.log("otro " + file);
      reader.onload = (e) => {
        vm.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    getImage(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      console.log(files);
      crear(files[0]);
    },

    processAgregarMascota: async function () {
      try {
        let url = "https://adoptame-be.herokuapp.com/mascotas/";
        let body = this.formularioAgregarMascota;
        let config = { header: {} };
        let result = await axios.post(url, body, config);
        swal.fire("", "Mascota añadida", "success");
        this.$router.push({ name: "adoptables" });
        //this.$emit("agregarCompleted", result);
      } catch (error) {
        if (error.response.status == 400)
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Ingreso de datos erróneo",
          });
        else {
          console.log(error.response);
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Ha surgido un error. Inténtalo más tarde",
          });
        }
      }
    },
    cancelar(){
        history.go(-1);
    },
  },
  created: function () {},
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
.container-formulario {
  border: 10px solid;
  border-radius: 10px;
  padding: 0%;
  height: auto;
  width: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(235, 235, 215, 0.452);
}
.container-formulario h1 {
  color: rgb(4, 4, 245);
  text-align: center;
  margin-bottom: 100vh;
  margin-left: 80px;
}
.container-formulario form {
  margin-top: 80px;
  margin-right: 300px;
}
.entrada {
  height: 22%;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  border: 1px solid #283747;
}
select {
  margin: 8px;
  height: 22%;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  border: 1px solid #283747;
}
.container-formulario input:checked + label {
  color: red;
}
.container-formulario input[type="checkbox"]:checked {
  box-shadow: 0 0 0 3px rgb(252, 252, 255);
}
button {
  cursor: pointer;
  color: var(--azul-oscuro);
  font-size: 1.3vw;
  font-weight: 600;
  background-color: var(--mostaza);
  border-style: none;
  border-radius: 30px;
  width: 100%;
  height: 8.5vh;
  border: 1px solid #e5e7e9;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}
.botonCancelar {
  cursor: pointer;
  font-size: 1.3vw;
  font-weight: 600;
  background-color: rgb(107, 107, 245);
  border-style: none;
  border-radius: 30px;
  width: 100%;
  height: 8.5vh;
  border: 1px solid #e5e7e9;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}
</style>