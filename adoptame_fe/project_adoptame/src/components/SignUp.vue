<template>
  <div class="signUp">
    <div class="portada">
      <div class="container_imagen"></div>
      <div class="signUpBox">
        <div class="container_signUp">
          <h2>Registrarse</h2>
          <form v-on:submit.prevent="processSignUp">
            <input type="text" v-model="user.username" placeholder="Username" />
            <br />
            <input
              type="password"
              v-model="user.password1"
              placeholder="Password"
            />
            <br />
            <input
              type="password"
              v-model="user.password2"
              placeholder="Password"
            />
            <br />
            <button type="submit" class="yellow-button">Registrarse</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "SignUp",
  data: function () {
    return {
      user: {
        username: "",
        password1: "",
        password2: "",
      },
    };
  },
  methods: {
    processSignUp: function () {
      axios
        .post(
          "https://adoptame-be.herokuapp.com/useradmin/rest-auth/registration/",
          this.user,
          { headers: {} }
        )
        .then((result) => {
          swal.fire("", "Registrado correctamente", "success");
          this.$emit("completedSignUp", result);
        })
        .catch((error) => {
          if(error.response.status == "400")
            swal.fire("Fallo registro", "La contraseña debe tener mínimo 8 caracteres entre números y letras o usuario ya existe", "error");
        });
    },
  },
};
</script>
<style scoped>
.portada {
  color: white;
  height: 81.5vh;
  background-image: url(../assets/perroSofa.jpg);
  background-size: cover;
  background-position: center;
}
.signUpBox {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: right;
  align-items: center;
}
.container_signUp {
  width: 30%;
  height: 68vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.signUp h2 {
  color: #ffffff;
}
.signUp form {
  width: 80%;
}
.signUp input {
  height: 22%;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}
.yellow-button {
  color: var(--azul-oscuro);
  font-size: 1.3vw;
  font-weight: 600;
  background-color: var(--mostaza);
  border-style: none;
  border-radius: 30px;

  width: 100%;
  height: 6.5vh;
  border: 1px solid #e5e7e9;
  padding: 10px 25px;

  margin: 5px 0 25px 0;
}

.yellow-button:hover {
  background-color: var(--azul-oscuro);
  color: var(--mostaza);
}
</style>
