//Ejemplo 2. Validar si me puedo comprar un coche en función de si tengo el dinero.

var precio = 30000;
var dinero = prompt("Introduce cuanto dinero tienes: ");
var edad2 = prompt("Introduce tu edad: ");
let VIP = true;


if ((dinero >= precio) && (edad2 >= 18)) {
  alert("Te puedes comprar el coche");
}
else if((dinero >= precio) && (edad2 < 18)){
    alert("Tienes el dinero pero no la edad");
}
else if ((dinero < precio) && (edad2 > 18)){
    alert("Tienes la edad pero no el dinero");
}
else if((dinero < precio) && (edad2 < 18)){
    alert("No tienes ni la edad ni el dinero");
}