// Arrays nultidimensionales. Dos dimensiones


var peliculas = ['Batman', 'Cars', 'It'];
var categoria = ['accion', 'infantil', 'Terror'];

var cine = [peliculas, categoria];

//Sería como poner:
//var cine = [['Batman', 'Cars', 'It'] , ['accion', 'infantil', 'Terror']];

console.log(cine);
console.log(cine[1][2]); //Terror
console.log(cine[1][0]); //Accion

//Array de tres dimensiones
var peliculas = ['Batman', 'Cars', 'It'];
var categoria = ['accion', 'infantil', 'Terror'];
var peliculasIT = ['IT1', 'IT2', 'IT3'];

var cine = [peliculas, categoria];

//Sería como poner:
//var cine = [['Batman', 'Cars', ['IT1', 'IT2', 'IT3']], ['accion', 'infantil', 'Terror']];

console.log(cine);
console.log(cine[0][2][2]);

