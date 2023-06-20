// Métodos de los Strings

// Pasamos de String a Number con parseInt() o con Number()

// Pasamos de Number a String con variable.toString()

//Pasar una cadena a mayúsculas
//-----------------------------

//Declaro una variable de tipo String
let cadenaMin = "Mi cadena de prueba";

//Declaro otra variable donde almaceno cadenaMIN pasada a mayúsculas
let cademaMAX = cadenaMin.toUpperCase();

//Imprimo el resultado
console.log(cademaMAX);


//Pasar una cadena a minúsculas
//-----------------------------


//Declaro una variable de tipo String
let cadenaInicial = "Mi Cadena de Prueba";

//Declaro otra variable donde almaceno cadenaInicial pasada a minúsculas
let cadenaFinal = cadenaInicial.toLowerCase();

//Imprimo el resultado
console.log(cadenaFinal);


// Calcular la longitud de una cadena

let miCadena2 = "Calculo la longitud de la cadena";
let longitud = miCadena2.length;
console.log("El String 'micadena2' tiene " + longitud + " caracteres.");

//Concatenar dos cadenas de texto
var text1 = "Primer texto";
var text2 = "Segundo texto";
var text3 = text1.concat(" ", text2);
console.log(text3);

//Se puede hacer con:
console.log(text1 + " " + text2);


// Extraer una serie de caracteres de una cadena

let frase = "Este es la frase de prueba";

/* Tenemos que usar el método substring() en el que pondremos
en la zona de parámetros el primer caracter (incluido) y 
el último (sin incluir).
El primer carácter de un String ocupa la posición cero.
*/
let palabra = frase.substring(11, 16);
console.log(palabra);

//Reemplazar caracteres por otros

let frase2 = "Buenas tardes";

/* Hay que poner el la zona de parámetros el elemento a
sustituir y aquel por el que se sustituye
*/
let frase3 = frase2.replace("tardes", "noches");
console.log(frase3);

// Mostrar el elemento que ocupa una posición en concreto.

let frase4 = "Esta es la frase 4";
console.log(frase4.charAt(6));

//Localizar el último elemento de cualquier String.
// Será el elemento en la posición Longitud-1
console.log(frase4.charAt(frase4.length-1));







