<template>
    <div class="total">
        <div class="table-responsive">
            <h1>Donantes</h1>
            <table class="table">
                <tr>
                    <th>
                          Id
                    </th>
                    <th>
                          Fecha
                    </th>
                    <th>
                          Email
                    </th>
                    <th>
                          Nombre
                    </th>
                    <th class="tipo_pago">
                          Tipo de pago
                    </th>
                    <th>
                          Cantidad
                    </th>
                    <th>
                          Comentarios
                    </th>
                    <th>
                        Actualizar
                    </th>
                    <th>
                        Borrar
                    </th>
                </tr>
                <tr v-for="donacion in listaDonantes" :key="donacion.registro_donante">
                    <td>
                        {{donacion.registro_donante}}
                    </td>
                    <td>
                        <input type="date" v-model="donacion.fecha" />
                    </td>
                    <td>
                        <input type="email" v-model="donacion.email"  />
                    </td>
                    <td>
                        <input type="text" v-model="donacion.nombre"  />
                    </td>
                    <td class="tipo_pago">
                        <input type="text" v-model="donacion.tipo_transaccion" id="tipo_transaccion" name="tipo_transaccion" />
                        <select v-model="donacion.tipo_transaccion" id="tipo_transaccion" name="tipo_transaccion">
                            <option value="A">Consignación</option>
                            <option value="B">Tarjeta débito</option>
                            <option value="C">Kviplata</option>
                            <option value="D">Xequi</option>
                            <option value="E">Efectivo</option>
                            <option value="F">Otro</option>
                        </select>
                    </td>
                    <td>
                        <input type="number" v-model="donacion.cantidad" />
                    </td>
                    <td>
                        <textarea maxlength="50" v-model="donacion.comentarios" />
                    </td>
                    <td>
                        <button v-if="prueba" v-on:click="actualizarDonacion({
                            registro_donante:donacion.registro_donante,
                            fecha:donacion.fecha,
                            email:donacion.email,
                            nombre:donacion.nombre,
                            tipo_transaccion:donacion.tipo_transaccion,
                            cantidad: donacion.cantidad,
                            comentarios: donacion.comentarios
                        })" class="botonActualizar">X</button>
                    </td>
                    <td>
                        <button v-on:click="borrarDonacion(donacion.registro_donante)" class="botonBorrar">X</button>
                    </td>
                </tr>
            </table>
            
        </div>

        <div class="promedio-donantes">
            <br>
                <h1>Promedio Donantes:</h1>
                <h2> {{Promedio.Promedio_donante}} $</h2>
            <br>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
    export default {
        name: "Donantelistado",
        data: function() {
            return {
                listaDonantes: [],
                Promedio: 0,
                bool_editable: true,
                donacion: {
                    fecha: "",
                    email: "",
                    nombre: "",
                    tipo_transaccion: "",
                    cantidad: 0,
                    comentarios: ""

                },
                prueba: true
            };
        },
        methods: {
            listarDonantes: function() {
                let url = 'https://adoptame-be.herokuapp.com/donantes/'
                let config = {headers: {}}
                axios.get(url,config)
                    .then((response)=>{
                        console.log(response)
                        this.listaDonantes = response.data
                    }).catch((error) => {
                        console.log(error)
                        Swal.fire({
                                icon: 'error',
                                title: 'Oops...',
                                text: 'Ha surgido un error. Inténtalo más tarde'
                        })
                    })
            },
            borrarDonacion: async function(id) {
                try{
                    let url = 'https://adoptame-be.herokuapp.com/donante/' + id
                    let config = {headers: {}}
                    await axios.delete(url,config)
                    Swal.fire('¡Enhorabuena!','Has eliminado un registro existosamente','success')
                    this.listarDonantes()
                }catch(error) {
                    console.log(error)
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Ha surgido un error. Inténtalo más tarde'
                    })
                }
            },
            actualizarDonacion: async function(donacion) {
                try{
                    let url = 'https://adoptame-be.herokuapp.com/donante/' + donacion.registro_donante
                    let body = donacion
                    let params = {header: {}}
                    await axios.put(url,body,params)
                    console.log("Actualizando") //Buscar promesas then y async
                    Swal.fire('¡Enhorabuena!','Has actualizado un registro existosamente','success')
                    this.listarDonantes()
                    //Emit (hijo a padre emit, padre a hijo props)
                    //this.$emit('completedDonacionesHome',result)

                }catch(error) {
                    console.log(error)
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Error de ingreso. Inténtalo de nuevo'
                    })
                }
            },
            verPromedioDonante: async function() {
                let url = 'https://adoptame-be.herokuapp.com/donantesavg/'
                let config = {headers: {}}
                axios.get(url,config)
                    .then((response)=>{
                        console.log(response)
                        this.Promedio = response.data
                    }).catch((error) => {
                        console.log(error)
                        Swal.fire({
                                icon: 'error',
                                title: 'Oops...',
                                text: 'Ha surgido un error. Inténtalo más tarde'
                            })
                    })
            }
        },
        created: function () {
            this.listarDonantes()
            this.verPromedioDonante()

        },

    }
</script>

<style scoped>
    .total {
        background-color: #eaeaea;
    }
    button {
        text-align: center;
        border-radius: 30px;
        border-style: none;
        width: 50px;
    }
    .botonBorrar {
        background-color: rgb(212, 36, 36);
    }
    .botonActualizar {
        background-color: var(--mostaza);
    }
    .table {
        border: 3px solid;
        margin-top: 6%;
        margin-left: 30px;
        width: 80%;
        
    }
    th {
        border-radius: 5px;
        border: 2px solid;
    }
    td {
        border-radius: 5px;
        border: 1px solid;
    }
    .table-responsive h1 {
        margin-top:80px;
        text-align: center;
    }
    .promedio-donantes {
        text-align: center;
    }

</style>