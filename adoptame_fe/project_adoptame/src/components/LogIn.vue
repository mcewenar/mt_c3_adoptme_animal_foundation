<template>
  <div class="logIn">
    <div class="portada">
      <div class="logIn_user">
        <div class="container_logIn_user">
          <h2>Iniciar sesión</h2>
          <form v-on:submit.prevent="processLogInUser">
            <input type="text" v-model="user.username" placeholder="Username" />
            <br />
            <input type="password" v-model="user.password" placeholder="Password" />
            <br />
            <button type="submit" class="yellow-button">Iniciar Sesion</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
    name: "LogIn",
    data: function(){
        return {
            user: {
                username:"",
                password:""
            }
        }
    },
    methods: {
        processLogInUser: function(){
            axios.post(
            "https://adoptame-be.herokuapp.com/useradmin/rest-auth/login/",
            this.user,
            {headers: {}}
            )
            .then((result) => {
                swal.fire('','Inició sesión correctamente','success');           
                this.$emit('completedLogIn', result)
                
            })
            .catch((error) => {
                if (error.response.status == "400")
                    swal.fire('','Credenciales incorrectas','error');
            });
        }
    }
}
</script>
<style scoped>
.portada {
  color: white;
  height: 81.5vh;
  background-image: url(../assets/perroSofa.jpg);
  background-size: cover;
  background-position: center;
}
.logIn_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: right;
  align-items: center;
}
.container_logIn_user {
  border-radius: 10px;
  width: 30%;
  height: 68vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.logIn_user h2 {
  color: #ffffff;
}
.logIn_user form {
  width: 80%;
}
.logIn_user input {
  height: 28%;
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
