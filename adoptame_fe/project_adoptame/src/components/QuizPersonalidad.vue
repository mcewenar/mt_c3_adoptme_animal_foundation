<template>
        <div class="quiz">
            <div class="contenedor">
                <div class="quiz-personalidad">
            <h1>Quiz de personalidad</h1>
            <div class="pregunta" v-if = "index < 10">
                <h2>{{preguntas[index]}}</h2>
                <button class="yellow-button" v-on:click="añadirPuntos">Si</button>
                <button class="yellow-button" v-on:click="(index+1 ==  10)?topPersonalidades():index++">No</button>
            </div>
            <div class="resultado" v-else >
                <h2>Resultados</h2>
                <div class="resultados" v-for="personalidad in resultado" :key="personalidad">
                    <h3>{{personalidad}}</h3>
                </div>
                <h2 style="font-size: 2rem; font-weight: 600">Encuentra una mascota con estas cualidades</h2>
            </div>
            <button class="yellow-button" v-if ="index != 0 && index < 10" v-on:click="eliminarPuntos">Volver</button>
            </div>
            </div>
        </div>
</template>

<script>
export default {
  name: "App",
  data: function () {
    return {
        preguntas: [
            'Eres una persona social',
            'Sueles viajar mucho',
            'Te gusta resolver acertijos',
            'Te gusta el ejercicio',
            'Te gusta ayudar a las personas',
            'Te gusta dar paseos largos',
            'Sueles pasar mucho tiempo en lugares con mucha naturaleza',
            'Te gusta tener todo organizado',
            'Prefieres quedarte en casa que salir a eventos',
            'Te encanta escuchar musica a todo volumen'
        ],
        personalidades: {
            'Activo':0,
            'Alegre': 0,
            'Dormilon':0,
            'Energetico':0,
            'Inteligente': 0,
            'Juguetón': 0,
            'Cariñoso': 0
        },
        respuestas: [
            ['Alegre', 'Cariñoso', 'Inteligente'],
            ['Inteligente','Activo','Cariñoso'],
            ['Inteligente', 'Activo', 'Juguetón'],
            ['Energetico', 'Activo', 'Alegre'],
            ['Alegre', 'Dormilon', 'Cariñoso'],
            ['Energetico', 'Activo', 'Juguetón'],
            ['Activo', 'Juguetón', 'Energetico'],
            ['Inteligente', 'Dormilon', 'Cariñoso'],
            ['Dormilon', 'Cariñoso', 'Juguetón'],
            ['Alegre', 'Inteligente', 'Activo']
            ],
        index : 0,
        resultado: []

    };
  },
  methods: {
    loadQuiz: function () {
      this.$router.push({ name: "quiz" });
    },
    añadirPuntos: function(){
        for(let i=0; i < 3; i++){
            let personalidad = (this.respuestas[this.index])[i]
            this.personalidades[personalidad]++;
        }
        if((this.index+1) < 10){
            this.index++;
        }else{
            this.topPersonalidades();
        }
    },
    eliminarPuntos: function(){
        this.index--
        for(let i=0; i < 3; i++){
            let personalidad = (this.respuestas[this.index])[i]
            this.personalidades[personalidad]--;
        }
    },
    topPersonalidades: function(){
        this.index++;
        let entries = Object.entries(this.personalidades);
        let sorted = entries.sort((a, b) => b[1]-a[1]);
        console.log(sorted);
        for(let i=0; i < 3; i++){
            this.resultado[i] = sorted[i][0]
        }
    }
  },
  created: function () {
    this.loadQuiz();
  },
};
</script>

<style scoped>

        *{
            margin: 0;
            padding: 0;
            font-family: "Dosis", sans-serif;
            color: var(--azul-oscuro);
        }
        :root {
            --mostaza: #e9d458;
            --azul-oscuro: #1b1e37;
        }
        .quiz{
             background-image: url('../assets/DogCute.jpg');
            background-size:cover;
        }
        .contenedor {

            padding: 28vh 0;
        }
        .quiz-personalidad {
            width: 50rem;
            height: 45vh;
            padding: 2rem 0;
            background-color: var(--mostaza);
            border-radius: 30px;
            display: flex;
            margin: 0 auto;
            flex-direction: column;
            justify-content:center;
            text-align: center;
            box-shadow: 10px 5px 15px var(--azul-oscuro);
        }
@keyframes rainbow-bg{
		100%,0%{
			color: rgb(102, 1, 1);
		}
		8%{
			color: rgb(105, 53, 0);
		}
		16%{
			color: rgb(122, 122, 0);
		}
		25%{
			color: rgb(65, 129, 0);
		}
		33%{
			color: rgb(0, 100, 0);
		}
		41%{
			color: rgb(0, 105, 53);
		}
		50%{
			color: rgb(0, 95, 95);
		}
		58%{
			color: rgb(0, 49, 99);
		}
		66%{
			color: rgb(0, 0, 117);
		}
		75%{
			color: rgb(57, 0, 114);
		}
		83%{
			color: rgb(92, 1, 92);
		}
		91%{
			color: rgb(155, 3, 79);
		}
}

        .quiz-personalidad h1 {
            font-size: 3rem;
            margin-bottom: 3rem;
            animation-name: rainbow-bg;
            animation-duration: 5s;
            animation-iteration-count: infinite;
            animation-direction: alternate ;
        }
        .pregunta h2 {
            font-size: 2.3rem;
        }
        .quiz-personalidad .yellow-button {
        font-size: 3vh;
        font-weight: 700;
        background-color: var(--mostaza);
        width: 6rem;
        height: auto;
        border-color: var(--azul-oscuro);
        margin: 1rem 3rem;
        border-radius: 30px!important;
        -webkit-border-radius: 30px!important;
        -moz-border-radius: 30px!important;
        -ms-border-radius: 30px!important;
        -o-border-radius: 30px!important;
        transition: all 300ms ease-in-out;
        color:var(--azul-oscuro)!important;
        }

        .pregunta .yellow-button {
            margin: 2rem 3rem;
            font-size: 3.5vh;
        }

        .quiz-personalidad .yellow-button:hover {
        background-color: var(--azul-oscuro);
        color: var(--mostaza)!important;
        border-color: var(--mostaza);
        }

        .resultado h2{
            font-size: 2.3rem;
            font-weight: 600;
        }

        .resultado h3 {
            font-size: 2rem;
            margin: 20px 0;
            font-weight: 600;
            animation-name: rainbow-bg;
            animation-duration: 3s;
            animation-iteration-count: infinite;
            animation-direction: alternate ;
        }

</style>