
    //Creamos un número aleatorio entre 0 y 1.
    // Despues lo multiplicamos por 100 para que esté entre 0-100
    //Lo redondeamos para que sea entero
    var numero = 50

    var numero_introducido;
    var contador = 0;
console.log(typeof(numero_introducido));

    while (numero != numero_introducido) {
      numero_introducido = Number(prompt("Introduce número: "));
      contador++;

      if (numero_introducido > numero) {
        alert("Demasiado alto");
      }

      if (numero_introducido < numero) {
        alert("Demasiado bajo");
      }
      
    } 

    
    alert("CORRECTO¡¡¡, el número era el " + numero + ". Has acertado en " + contador + " intentos.");


  
