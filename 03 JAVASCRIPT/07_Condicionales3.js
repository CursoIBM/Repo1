//Condicional con un OR lógico

let procedencia1 = "Sevilla";
var procedencia2 = prompt("Introduce la procedencia2: ");

if((procedencia1 == "Malaga") || (procedencia2 == "Madrid")){
    alert("Acceso permitido");
}else{
    alert("Acceso no permitido");
}