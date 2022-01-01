import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import Inicio from './components/Inicio.vue'
import DonanteHome from './components/donacionesHome.vue'
import Donantelistado from './components/listaDonantes'
import SignUp from './components/SignUp.vue'
import LogIn from './components/LogIn.vue'
import Adoptar from './components/Adoptar.vue'
import Quiz from './components/QuizPersonalidad.vue'
import Eventos from './components/Eventos.vue'
import Adoptables from './components/Adoptables.vue'
import AgregarMascota from './components/AgregarMascota.vue'
import ActualizarMascota from './components/ActualizarMascota.vue'

const routes = [{
  path: '/',
  name: 'root',
  component: App
},
{
  path: '/inicio',
  name: 'inicio',
  component: Inicio
},
{
  path: '/inicio/donantehome',
  name: 'donantehome',
  component: DonanteHome
},
{
  path: '/inicio/donantehome/listadonantes',
  name: 'donantelistado',
  component: Donantelistado
},
{
  path: '/user/signUp',
  name: 'signUp',
  component: SignUp
},
{
  path: '/user/logIn',
  name: "logIn",
  component: LogIn
},
{
  path: '/inicio/adoptar',
  name: "adoptar",
  component: Adoptar
},
{
  path: '/inicio/quiz',
  name: "quiz",
  component: Quiz
},
{
  path: '/inicio/eventos',
  name: "eventos",
  component: Eventos
},
{
  path: '/user/adoptables',
  name: "adoptables",
  component: Adoptables
},
{
  path: '/user/adoptables/agregarMascota',
  name: "agregarmascota",
  component: AgregarMascota
},
{
  path: '/user/adoptables/actualizarMascota/:Id',
  name: "actualizarmascota",
  component: ActualizarMascota
},
]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router