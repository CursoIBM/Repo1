//Métodos de los Arrays

var articulos = ["balon", "botas", "camiseta", "pantalon"];

document.write("<p>El primer articulo es<strong> "+articulos[0]+"</strong ></p> ");

document.write("<P>La longitud del array es " + articulos.length + "</p>");

document.write("<p>El último articulo es <strong>" + articulos[articulos.length - 1] + "</strong></p>");

//Añadir elemento en la primera posición
articulos.unshift("pelota");

// En este punto el array quedaría así:
//var articulos = ["pelota", "balon", "botas", "camiseta", "pantalon"];

//Añadir elemento en la última posición
//Sería como poner: articulos[articulos.length] = "canasta";
articulos.push("canasta");

//var articulos = ["pelota", "balon", "botas", "camiseta", "pantalon", "canasta"];

//Sustituir elemento en una posición determinada
document.write("<p>Añadimos el artículo <strong>" + articulos[0] + "</strong></p>");

document.write("<p>El primer articulo ahora es <strong>" + articulos[0] + "</strong></p>");

document.write("<p>El último articulo ahora es <strong>" + articulos[articulos.length - 1] + "</strong></p>");

document.write("<P>La longitud del array ahora es " + articulos.length + "</p>");

document.write(articulos);
console.log(articulos);

articulos.push(prompt("introduce nuevo articulo"));

document.write("<br>");

document.write(articulos);

//Para averiguar la poción de un elemento
var posicion = articulos.indexOf("botas");
//var posicion = articulos.search("botas");
console.log('El elemento "botas" ocupa la posición: ' + posicion);

//Pasar un array a String
var articulos3 = ["balon", "botas", "camiseta", "pantalon"];
var miString=articulos.join(" - ");
console.log(miString);
//El resultado sería:
//miString = "pelota,balon,botas,camiseta,pantalon,canasta,dfghdf";


//Crear un array con un número limitado de elementos
//var miArray5 = articulos.split(",",4);

//Ordenar un Array numérico
var numeros=[3,43,34,32,345,6];
//console.log(myString.sort(function(a,b){return a-b}));

//Contatenar Arrays
var miArray5 = ["moto", "coche", "camion"];
var miArray6 = ["rojo", "azul", "verde"];
var miArray7 = miArray5.concat(miArray6);
document.write("<h2>" + miArray7 + "<h2>");
console.log(miArray7);


//Parámetro Rest
var oscarizadas = ['Fargo', 'Espartaco', 'Titanic'];
var peliculas = ['Truly', ...oscarizadas, 'Pulp Fiction'];


//Métodos de los Arrays

let frutas = ["Manzana", "Banana"];

//Longitud del Array
console.log(frutas.length)

//Último elemento de un Array
console.log(frutas[frutas.length - 1]);

//Método Push. Añade un elemento al final del Array
let nuevaLongitud = frutas.push('Naranja');

//Ahora el Array sería: ["Manzana", "Banana", "Naranja"]

//Método Pop. Quita el último elelento de un Array
frutas.pop();
//Ahora el Array sería: ["Manzana", "Banana"]

//Añadir elementos al principio del un Array
frutas.unshift('Fresa');
//Ahora el Array sería: ["Fresa", "Manzana", "Banana"]

//Quitar el primer elemento de un Array
frutas.shift();
//Ahora el Array sería: ["Manzana", "Banana"]

//Para saber la posición que ocupa un elemento
console.log("El elemento Banana ocupa la posición: " + frutas.indexOf('Banana')); 

//Borrar un elemento en concreto según su posición
frutas.splice(pos, 1);
//Ahora el Array sería: ["Manzana"]

//Copiar un array
let frutas2 = frutas.slice();





























