// Funciones

    //Declaración de la función
    let num1 =5;
    let num2 = 10;

    function suma(){
    console.log("La suma de " +num1 + " y " + num2 + " es " + (num1+num2));
    }

    //Llamada a la función
    suma();

//Funciones con parámetros

    function suma2(num1, num2){
        console.log("La suma de " +num1 + " y " + num2 + " es " + (num1+num2));
    }

//Sobrecarga de parámetros
function suma2(num1, num2, num3){
    console.log("La suma de " +num1 + " y " + num2 + " y " + num3+ " es " + (num1+num2+num3));
}

suma2(3,5);
suma2(3,5,6);









