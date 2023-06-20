//CASTING O PASO DE TIPOS


//------------------------------
//Paso de String a Number
//------------------------------

//Declaro e inicializo una variable de tipo string
let numeroInicial = "43";

//Le concateno a la variable el numero 17
console.log(numeroInicial + 17);

/* Paso la variable numeroInicial, que era un string, 
a Number y la almaceno en otra variable que he creado 
con el nombre de numeroReal
*/
let numeroReal = Number(numeroInicial);

//También se puede hacer con parseInt:
// let numeroReal = parseInt(numeroInicial);

// numeroReal ahora vale = 43

//Le sumo 17 a numeroReal
console.log(numeroReal + 17);

//------------------------------
//Paso de Number a String
//------------------------------

//Declaro una variable de tipo Number
let miNumero = 55;

//Paso la variable Number a String y la almaceno en miCadena
let miCadena = miNumero.toString();

//Compruebo que realmente es una cadena
console.log(miCadena + 17);

/*Un uso muy extendido de Number() es para pasar a numérico 
Lo que un usuario nos introduzca por PROMPT
*/

// Pido una edad por prompt, con lo que será de tipo STRING
let edad = prompt("Introduzca su edad:");

/* Paso la variable edad a Number y la almaceno en una
variable que he creado y a la que llamo edadNumerica
*/

let edadNumerica = Number(edad);

//Opero con la variable
console.log("El año que viene tendrás " + (edadNumerica + 1) + " años.");






