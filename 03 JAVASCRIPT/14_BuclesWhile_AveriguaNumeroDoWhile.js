
    //Creamos un número aleatorio entre 0 y 1.
    // Despues lo multiplicamos por 100 para que esté entre 0-100
    //Lo redondeamos para que sea entero
 
    var numero = parseInt(Math.random() * 100);
    var numero_introducido;
    var contador = 0;

    do {
      numero_introducido = prompt("Introduce número: ");
      contador++;
      if (numero_introducido > numero) {
        alert("Demasiado alto");
      }
      if (numero_introducido < numero) {
        alert("Demasiado bajo");
      }
    } while (numero != numero_introducido);
    alert("CORRECTO¡¡¡, el número era el " + numero + ". Has acertado en " + contador + " intentos.");


    
    


  
