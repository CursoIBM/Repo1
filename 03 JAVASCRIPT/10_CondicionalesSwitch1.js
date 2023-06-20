//Condicional Switch

var edad = 50;
var imprime = "";



switch (edad) {
  case 18:
    imprime = "Acabas de cumplir la mayoría de edad";
    break;

  case 25:
    imprime = "Eres un adulto";
    break;

  case 50:
    imprime = "Eres maduro";
    break;

  default:
    imprime = "Otra edad no contemplada";
  }

document.write(imprime);

/* El mismo ejercicio pero hecho con un IF...ELSE

if(edad == 18){
  imprime = "Acabas de cumplir la mayoría de edad";
}else if(edad == 25){
  imprime = "Eres un adulto";
}else if(edad == 50){
  imprime = "Eres maduro";
}else{
  imprime = "Otra edad no contemplada";
}

document.write(imprime);

*/