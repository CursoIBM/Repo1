//Sintaxis del operador ternario
// (condicion) ? EjecutarSiTrue : EjecutarSiFalse;

//Averiguar si un número es par

var number = Number(prompt("Introduce número"));
var resultado = (number % 2 == 0) ? "Es par" : "Es impar";

//Sería como poner

if (number % 2 == 0) {
  resultado = "Es par";
} else {
  resultado = "Es impar";
}

console.log(resultado);

// Validar una comparación

let resultado2 = (1 > 2) ? "Verdadero" : "Falso";
console.log(resultado2);


