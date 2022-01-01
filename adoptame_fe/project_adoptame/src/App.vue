<template>
  <div id="app" class="app">
    <header class="navegacion"
    :style = "(expanded) ? { 'background-color': '#e9d458' } : { 'background-color': 'transparent' } "
  >
      <nav class="navbar navbar-expand-md navbar-dark">
        <a href="#" class="navbar-brand">
          <img src="@/assets/logo.svg" v-on:click="loadInicio" alt="Boostrap 5 Logo" height= "80" :style = "expanded ? { 'filter': 'invert(9%) sepia(9%) saturate(4241%) hue-rotate(196deg) brightness(94%) contrast(92%)' } : {'filter': 'invert(98%) sepia(6%) saturate(1788%) hue-rotate(199deg) brightness(118%) contrast(100%)'}"/>
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#toggleMobileMenu"
          aria-controls="toggleMobileMenu"
          aria-expanded="false"
          aria-lable="Toggle navigation"
          v-on:click="isExpanded"
        >
              <span class="" role="button" ><i class="fa fa-bars" aria-hidden="true"  :style = "expanded ? { 'color': '#1b1e37' } : { 'color': 'white' }" ></i></span>

        </button>
        <div class="collapse navbar-collapse"
        :class = "clicked?  clicked=false :'collapse navbar-collapse'"
        id="toggleMobileMenu">
          <ul class="navbar-nav ms-auto text-center">
            <li>
              <a class="nav-link" v-on:click="loadInicio">Inicio</a>
            </li>
            <li>
              <a class="nav-link" v-on:click="loadAdoptar">Adoptar</a>
            </li>
            <li>
              <a class="nav-link" v-if="is_auth" v-on:click="loadAdoptables">Adoptables</a>
            </li>
            <li>
              <a class="nav-link" v-on:click="loadDonanteHome">Donar</a>
            </li>
            <li>
              <a class="nav-link"  v-on:click="loadEventos">Eventos</a>
            </li>
            <li>
              <a class="nav-link" v-on:click="isClicked;">Nosotros</a>
            </li>
            <li>
              <a class="nav-link" v-if="is_auth" v-on:click="logOut">Cerrar Sesión</a>
            </li>
            <li>
              <a class="nav-link" v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</a>
            </li>
            <li>
              <a class="nav-link" v-if="!is_auth" v-on:click="loadSignUp">Registrarse</a>
            </li>
          </ul>
        </div>
      </nav>
    </header>
    <div class="main-component">
      <router-view
        v-on:completedDonacionesHome="completedDonacionesHome"
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logout="logOut"
        v-on:loadInicio="loadInicio"
      ></router-view>
    </div>
    <footer>
      <img src="@/assets/logo.svg" alt="logo" />
      <div class="basic-info">
        <div class="info">
          <h3>Links:</h3>
          <p>google.com</p>
          <p>facebook.com</p>
          <p>instagram.com</p>
        </div>
        <div class="info">
          <h3>Contacto:</h3>
          <p>numero: 1234567890</p>
          <p>fijo: 123456</p>
          <p>email: prueba@gmail.com</p>
        </div>
      </div>
    </footer>
  </div>
</template>
<script>
export default {
  name: "App",
  data: function () {
    return {
      is_auth: false,
      expanded: false,
      clicked: false
    };
  },

  methods: {
    isClicked: function(){
      this.clicked = true;
      this.expanded = false;
    },
    isExpanded: function(){
      this.expanded = !this.expanded
    },
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("is_auth") || false;
      if
       (this.is_auth == false) this.$router.push({ name: "logIn" });
      else
        this.$router.push({ name: "inicio" });
    },
    loadInicio: function () {
      this.$router.push({ name: "inicio" });
      this.isClicked();
    },
    loadDonanteHome: function () {
      this.$router.push({ name: "donantehome" });
      this.isClicked();
    },
    loadListaDonantes: function () {
      this.$router.push({ name: "donantelistado" });
    },
    loadSignUp: function () {
      this.$router.push({ name: "signUp" });
      this.isClicked();
    },
    completedSignUp: function (data) {
      this.$router.push({ name: "inicio" });
    },
    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
      this.isClicked();
    },
    completedLogIn: function (data) {
      this.is_auth = true;
      console.log(data);
      localStorage.setItem('is_auth', true);
      localStorage.setItem('token', data.data.key)
      this.$router.push({ name: "inicio" })
      this.verifyAuth();
    },
    logOut: function () {
      localStorage.clear();
      this.verifyAuth();
      this.loadInicio();
    },
    loadAdoptar: function(){
      this.$router.push({ name: "adoptar" })
      this.isClicked();
    },
    loadEventos: function(){
       this.$router.push({ name: "eventos" })
        this.isClicked();
      },
    loadAdoptables: function(){
      this.$router.push({ name: "adoptables" })
      this.isClicked();
    },
  },
  created: function () {
    this.verifyAuth();
    this.loadInicio()
  },
};
</script>
<style>
:root {
  --mostaza: #e9d458;
  --azul-oscuro: #1b1e37;
}

* {
  font-family: "Dosis", sans-serif;
  margin: 0;
  padding: 0;
}
body {
  color: var(--azul-oscuro);
  background-color:#EAEAEA;
}

/*---------------------Navegación-------------------*/

header {
  position: absolute;
  width: 100%;
  top: 0;
  color:white;
  z-index: 1;
  transition: background-color 0.2s ease-out;
}

header .navbar {
  padding: 0;
  margin-top: 1vh;
}

header img {
  filter: invert(98%) sepia(6%) saturate(1788%) hue-rotate(199deg)
  brightness(118%) contrast(100%);
  margin: 0.2vw 0 0 1.3vw;
  height: 5vw;
}

header ul {
  margin-right: 2vw;
}

.navbar-dark .navbar-nav .nav-link {
  font-size: 1.6rem;
  color: white;
  opacity: 1;
  margin: 0 1vw 0 1vw;
  font-weight: 600;
  text-shadow: 3px 4px 5px black;
  cursor: pointer;
}
header a:hover {
  color:var(--azul-oscuro)!important;
}
.navbar-toggler{
  border: none!important;
  padding: 0;
  margin-right: 3vw;
}

.navbar-toggler:focus,
.navbar-toggler:active,
.navbar-toggler-icon:focus {
    outline: none;
    box-shadow: none;
}

.fa {
  position: absolute;
  top: 1.8rem;
  left: 85vw;
}
.fa-bars {
  font-size:5vh;
}

.collapsing {
  background-color:var(--mostaza);
}
.navbar-collapse {
  z-index: 1;
}



footer {
  background-color: var(--mostaza);
  color: var(--azul-oscuro);
  display:flex;
  justify-content: space-between;
  height: fit-content;
}

footer img {
  width: 8rem;
  filter: invert(9%) sepia(23%) saturate(1843%) hue-rotate(198deg)
  brightness(95%) contrast(92%);
  margin: 1rem 2rem;
}

.basic-info {
  display: flex;
}

.info {
  margin: 1rem 4rem;
}

.info h3 {
  font-weight: 700;
  font-size: 1.3rem;
}

.info p {
  font-weight: 600;
  font-size: 1.3rem;
  margin: 0.5rem 0;
}





@media (max-width: 767px) {
  .navbar-dark .navbar-nav .nav-link {
    font-size: 4.5vh;
    margin: 0;
    padding-top: 4.2vh;
    padding-bottom: 4.2vh;
    color:var(--azul-oscuro);
    text-shadow: none;
    background-color: var(--mostaza);
    border-style:solid;
    border-width: 1px;
    width: 100%;
    border-color: var(--mostaza);
  }
  footer img {
    width: 5rem;
  }
  header img {
  height: 13vw;
  }
}
</style>