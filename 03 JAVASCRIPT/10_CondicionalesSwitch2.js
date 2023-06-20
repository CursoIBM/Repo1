//Condicional Switch con varios elementos de comparación

let mes = Number(prompt("Introduce mes del año"));
let estacion = "";

switch (mes) {
  case 12:
  case 1:
  case 2:
    estacion = "Invierno";
    break;

  case 3:
  case 4:
  case 5:
    estacion = "Primavera";
 break;

  case 6:
  case 7:
  case 8:
    estacion = "Verano";
    break;

  case 9:
  case 10:
  case 11:
    estacion = "Otoño";
    break;

  default:
    estacion = "Valor incorrecto";
}

console.log(estacion);
