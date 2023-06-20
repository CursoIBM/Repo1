
//Podemos trabajar con números, strings y booleans
// Declaración de variables:
// No puede empezar por un número
// Esto de error:    var 2_cliente;
// Evitar tildes y Ñ

//Variable correctamente declarada
let _numero;

// Inicialización de la variable
_numero = 63;

//Variable declara e inicializada
var numero4 = 647;

// Sepueden declara e inicializar varias variables a la vez.
var a=3, b=4, c=5;

//Sería lo mismo que poner:
/*
var a=3;
let b=4;
var c=5;
*/

// Javascript es Case sensitive. Distingue entre mayúsculas/minúsculas
var numero = 10;
var Numero = 20;

console.log("La variable 'numero' vale:" + numero);
console.log("La variable 'Numero' vale:" + Numero);

//Con variable numéricas podemos operar matemáticamente

var sumando1 = 35;
var sumando2 = 45;

var resultado = sumando1+sumando2;

console.log("El resultado de sumar " + sumando1 + " + " 
             + sumando2 + " es " + resultado);


 // Operador modulo o resto de la división
 var resto = 46 % 5;
 console.log("El resto de 46/5 es " + resto);

 //Operador incremento
 var numeroInicial = 10;
 let numeroIncrementado = ++numeroInicial;

 //Sería como poner que numeroIncrementado = numeroInicial +1;
 console.log("El operador incremento sobre numeroInicial daría " + numeroIncrementado);

 //IMPORTANTE: No es lo mismo ++variable que variable++
 var numero5 = 5;

 document.write("El número antes del incremento vale " + numero5++);
 document.write("<br>");
 document.write("El número después del incremento vale " + numero5);
 
 document.write("<br>");
 document.write("<br>");

 // Ahora al revés
 let numero6 = 5;

 document.write("El número antes del incremento vale " + ++numero6);
 document.write("<br>");
 document.write("El número después del incremento vale " + numero6);

 //Constantes. Como las variables pero no se puede cambiar su valor
 // Se declaran en mayúsculas
 const MICONSTANTE = 4765;
 //MICONSTANTE = 345;   Esto daría error

 // Hay que declararlas e inicializarlas obligatoriamente.
 //const MICONSTANTE2;  Esto daría error


//Declarión de strings
//------------------------
//------------------------
let nombre = "Mi nombre es Angel";
let nombre2 = 'Mi nombre es Angel';

/* Aunque declaremos números, si lo hacemos entre comillas,
nos lo tratará como strings */
let edad2 = "43";
console.log(edad2+20); 

//Las comillas anidadas siempre alternas,
let nombre3 = 'Mi nombre es "Angel" ';
let nombre4 = "Mi nombre es 'Angel' ";

/* Cuando declaremos numeros con los que no vamos a operar
matemáticamente lo haremos como strings */
let telefono = "666666666";

//Los strings no se suman, se concatenan:
let nombre5 = "Angel";
let espacio = " ";
let apellido = "García";
let nombreCompleto = nombre+espacio+apellido;

console.log(nombreCompleto);

//Otra forma de hacerlo
console.log(nombre5 + " " +apellido);

console.log(nombre5 + " " +edad2);

//Booleans. Pueden tomar valores de TRUE o FALSE
var numero7 = true;
let numero8 = false;
let numero9 = false;

//Operador de comparación menor que...
console.log(numero7<numero8);

//Operador de comparación mayor o igual que...
console.log(numero7>=numero9);

//Operador de comparación igual que...OJO, VA CON DOBLE ==
console.log(numero7==numero9);

//Operador de comparación estrictamente igual que...OJO, VA CON triple ===
let numero10 = 34;
let numero11 = "34";
console.log(numero10===numero11);

//Operador diferente que...
let numero12 = 34;
let numero13 = "34";
console.log(numero12 !=  numero13);

console.log(typeof(numero13));

//Operaciones con null
let sueldo3;
let sueldo = null;
var sueldo2 = sueldo + 1000; //null

//IMPORTANTE. La precedencia es la misma que en matemáticas
let resultado3 = 4 + 5 * 6 / 3; //(4 + ((5*6)/3))











