<template>
  <div class="actualizar-mascota">
    <div class="head"></div>
    <div class="container-formulario">
      <h1>Formulario actualizar mascota:</h1>
      <form v-on:submit.prevent="processActualizarMascota({
            nombre:mascota.nombre,
            especie:mascota.especie,
            edad:mascota.edad,
            tamaño:mascota.tamaño,
            sexo:mascota.sexo,
            esterilizado:mascota.esterilizado,
            desparasitado:mascota.desparasitado,
            personalidad:mascota.personalidad,
            descripcion:mascota.descripcion,
            salud:mascota.salud,
            adoptado:mascota.adoptado
        })">
          <br />
        <label>Nombre: </label>
        <input
          v-model="mascota.nombre"
          type="text"
          
          class="entrada"
        />
        <br />
        <label for="especie">Especie: </label>
        <select
          v-model="mascota.especie"
          id="especie"
          name="especie"
        >
          <option value="G">Gato</option>
          <option value="P">Perro</option>
        </select>
        <br />
        <label>Edad (años): </label>
        <input
          v-model="mascota.edad"
          type="number"
          placeholder="Años"
          class="entrada"
        />
        <br />
        <label for="tamaño">Tamaño: </label>
        <select
          v-model="mascota.tamaño"
          id="especie"
          name="especie"
        >
          <option value="P">Pequeño</option>
          <option value="M">Mediano</option>
          <option value="G">Grande</option>
        </select>
        <br />
        <label for="sexo">Sexo: </label>
        <select v-model="mascota.sexo" id="sexo" name="sexo">
          <option value="H">Hembra</option>
          <option value="M">Macho</option>
        </select>
        <br />
        <label>Esterilizado: </label>
        <input
          v-model="mascota.esterilizado"
          type="checkbox"
          name="esterilizado"
          id="esterilizado"
        />
        <br />
        <label>Desparasitado: </label>
        <input
          v-model="mascota.desparasitado"
          type="checkbox"
          name="desparasitado"
          id="desparasitado"
        />
        <br />
        <label>Personalidad: </label>
        <input
          v-model="mascota.personalidad"
          type="text"
          placeholder="Personalidad"
          class="entrada"
        />
        <br />
        <label>Descripción: </label>
        <input
          v-model="mascota.descripcion"
          type="text"
          placeholder="Descripción"
          class="entrada"
        />
        <br />
        <label>Salud: </label>
        <input
          v-model="mascota.salud"
          type="text"
          placeholder="Salud"
          class="entrada"
        />
        <br />
        <label>Adoptado: </label>
        <input
          v-model="mascota.adoptado"
          type="checkbox"
          name="adoptado"
          id="adoptado"
        />
        <br />
        <label>Imagen: </label>
        <img
            class="card-img-top"
            :src="mascota.imagen"
            alt="Card image cap"
          />
        <input
            v-on:change="mascota.imagen"
          class="entrada"
          type="file"
          @change="getImage"
          accept="image/*"
        />
        <br />
        <br />
        <button type="submit">Actualizar</button>
        <input v-on:click="cancelar" type="button" value="Cancelar" class="botonCancelar">
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "ActualizarMascota",
  data: function () {
    return {
      mascota: {
        nombre: "",
        especie: "",
        edad: 0,
        tamaño: "",
        sexo: "",
        esterilizado: "",
        desparasitado: "",
        personalidad: "",
        descripcion: "",
        salud: "",
        adoptado:"",
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
    listaMascota: function () {
      let url = "https://adoptame-be.herokuapp.com/mascota/" + this.$route.params.Id;
      let config = { Headers: {} };
      axios
        .get(url, config)
        .then((response) => {
          this.mascota = response.data;
          console.log(this.mascota);
        })
        .catch((error) => {
          swal.fire("", "Error, intente mas tarde", "error");
        });
    },
    processActualizarMascota: async function(mascota) {
                try{
                    let url = 'https://adoptame-be.herokuapp.com/mascota/' + this.$route.params.Id;
                    let body = mascota
                    let params = {header: {}}
                    await axios.put(url,body,params);
                    console.log("Actualizando") //Buscar promesas then y async
                    Swal.fire('¡Enhorabuena!','Has actualizado un registro existosamente','success')
                    this.$router.push({ name: "adoptables" }); 
                    //Emit (hijo a padre emit, padre a hijo props)
                    //this.$emit('completedDonacionesHome',result)

                }catch(error) {
                    console.log(error)
                    alert(error);
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Error de ingreso. Inténtalo de nuevo'
                    })
                }
            },
    cancelar() {
      history.go(-1);
    },
  },
  created: function () {
    this.listaMascota();
  },
};
</script>
<style scoped>
.card-img-top {
  padding: 1%;
  width: 250px;
  height: 250px;
  margin: 1px auto;
  display: block;
}
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
  margin-bottom: 125vh;
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