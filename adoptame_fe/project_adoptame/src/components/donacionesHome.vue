<template>
    <div class="donantes-home">
        <br>
        <div class="portada">
            <h1>Donar</h1>
        </div>
        <h1>¿Cómo Donar?</h1>
        <div class="comoDonar">
            <p> Lorem ipsum dolor sit amet, ne sea tota delicata molestiae. Dolore oportere an vim. 
                Tation noluisse probatus cu has, odio nibh numquam pro no. Vix labitur probatus dissentias an. 
                Pri quodsi bonorum pertinax ei. Ne nec detracto mnesarchum.
                Ius natum ignota docendi an, ea sed possit omittam. His ei inani mentitum, vim an liber indoctum accommodare, 
                an usu quando offendit atomorum. Quo fugit verterem ei, pri ullum accusamus ei. Mea ex atqui essent. 
                No habemus legendos philosophia mea, ne vix alia simul.
                Tation exerci nemore mel ea. Nam ea graeco reprehendunt, ex dolorum dissentiunt nam.</p>
        </div>
        <div v-if="donar_bool" class="container-verDonaciones">
            <br>
            <button type="submit" class="btn-verDonaciones" v-on:click="verFormulario(false)" >Donar insumos</button>
            <br>
            <button type="submit" class="btn-verDonaciones" v-on:click="verFormulario(true)">Donar dinero</button>
            <br>
        </div>


        <div v-if="is_auth" class="container-verDonaciones">
            <br>
            <button type="submit" class="btn-verDonaciones" v-on:click="loadListaDonantes">Ver donaciones</button>
            <br>
        </div>
        <div v-if="!donar_bool" class = "container-donantes-formulario">
            <h1> Formulario Donación: </h1>
            <br>
            <form v-on:submit.prevent="proccessDonanteFormulario">
                <label>Fecha: </label>
                <input type="date" v-model="formularioDonante.fecha" placeholder="Fecha"/>
                <br>
                <label>Email: </label>
                <input type="email" v-model="formularioDonante.email" placeholder="Email"/>
                <br>
                <label>Nombre: </label>
                <input type="text" v-model="formularioDonante.nombre" placeholder="Nombre"/>
                <br>
                <br>
                <label v-if="ocultar_cant" for="tipo_transaccion">Elige el tipo de pago: </label>
                <select v-if="ocultar_cant" v-model="formularioDonante.tipo_transaccion" id="tipo_transaccion" name="tipo_transaccion">
                    <option value="A">Consignación</option>
                    <option value="B">Tarjeta débito</option>
                    <option value="C">Kviplata</option>
                    <option value="D">Xequi</option>
                    <option value="E">Efectivo</option>
                    <option value="F">Otro</option>
                </select>
                <br>
                <br>
                <label v-if="ocultar_cant">Cantidad: </label>
                <input v-if="ocultar_cant" type="number" v-model="formularioDonante.cantidad" placeholder="Cantidad"/>
                <br>
                <br>
                <label>Comentarios: </label>
                <textarea v-model="formularioDonante.comentarios" id="comentarios" name="comentarios" rows="4" cols="50" maxlength="50"/>

                <br>
                <button type="submit">Enviar formulario</button>
            </form>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
    export default {
        name: 'DonanteHome',
        data: function() {
            return {
                formularioDonante: {
                    fecha: "",
                    email: "",
                    nombre: "",
                    tipo_transaccion: "",
                    cantidad: 0,
                    comentarios: ""

                },
                is_auth: localStorage.getItem("is_auth"),
                donar_bool: true,
                ocultar_cant: true
            }
        },
        methods: {
            loadListaDonantes: function() {
                this.$router.push({name: 'donantelistado'})
            },
            proccessDonanteFormulario: async function() {
                try {
                    console.log("INGRESANDO FORMULARIO")
                    console.log(this.formularioDonante)
                    let endpoint = "https://adoptame-be.herokuapp.com/donantes/"
                    let body = this.formularioDonante
                    let params = {header: {}}
                    await axios.post(endpoint,body,params)
                    Swal.fire('¡Buen trabajo!','Gracias por tu donación','success')
                    //Emit (hijo a padre emit, padre a hijo props)
                    this.$emit("loadInicio");
                    //this.loadInicio()
                } catch (error){
                    if(error.response.status==400) {
                            Swal.fire({
                                icon: 'error',
                                title: 'Oops...',
                                text: 'Ingreso de datos erróneo'
                            })
                   } else {
                            console.log(error.response)
                            Swal.fire({
                                icon: 'error',
                                title: 'Oops...',
                                text: 'Ha surgido un error. Inténtalo más tarde'
                            })
                   }

                }
            },
            verFormulario: function(bool) {
                this.donar_bool = false
                if(bool) {
                    console.log("Se muestra cantidad")
                } else {
                    console.log("No se muestra cantidad")
                    this.ocultar_cant = false
                }

            },
        },

        created: function() {
        }
    }
</script>
<style scoped>
    .donantes-home {
        display:flex;
        flex-direction: column;
        justify-content: right;
        align-items: center;
        background-color: #eaeaea;
    }

    .portada {
        position: relative;
        top: -30px;
        width: 100%;
        height: 35vh;
        background-image: url(../assets/donacionPortada.png);
        background-size: cover;
        background-position: center;
        display: flex;
        justify-content: center;
        text-align: center;
        overflow: hidden;
    }
    .portada h1 {
        margin-top: 15vh;
        color: white;
        font-weight: 600;
        font-size: 3rem;
        text-shadow: 3px 4px 8px black;
    }
    .container-donantes-formulario {
        border: 2px solid;
        border-radius: 10px;
        padding: 0%;
        height: auto;
        width: auto;
        display: flex;
        justify-content: right;
        align-items: center;
    }
    .container-donantes-formulario h1 {
        color: var(--azul-oscuro);
        margin-bottom: 80vh;
        margin-left: 80px;
    }
    .container-donantes-formulario form {
        margin-top: 80px;
        margin-right: 300px;
    }
    .container-donantes-formulario input {
        height: 22%;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;
        border: 1px solid #283747;
    }
    .container-verDonaciones {
        height: 60%;
        width: 30%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    button {
        cursor:pointer;
        color: var(--azul-oscuro);
        font-size: 1.3vw;
        font-weight: 600;
        background-color: var(--mostaza);
        border-style: none;
        border-radius: 30px;

        width: 100%;
        height: 8.5vh;
        border: 1px solid #f1f2f3;
        padding: 10px 25px;

        margin: 5px 0 25px 0;
    }
    .comoDonar {
        margin-left:15px;
        margin: 10vh auto;
    }
    .comoDonar p {
        color: var(--azul-oscuro);
        font-weight: 600;
        margin: 0 auto;
        font-size: 1.6vw;
        width: 80%;
        text-align: center;
    }
    .comoDonar h1 {
        text-align: center;
        color:var(--azul-oscuro);
        margin-top: 2vh;
        font-size: 2.5vw;
        font-weight: 500;
        text-shadow: 1px 2px 5px black;
        letter-spacing: 2px;
        top: 29%;
        left: 40%;
    }
    /*Responsive web: */
    @media(max-widht:600px) {
        .comoDonar p {
            font-size: 50px;
            font-weight: 600;
            margin: 0 auto;
            font-size: 1.1vw;
            width: 50%;
            text-align: center;
        }
    }

</style>
