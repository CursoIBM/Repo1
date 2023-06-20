

try {
    // Código que puede lanzar una excepción
    let num = 10 / 0; // División por cero
  } catch (error) {
    // Manejo de la excepción
    console.log("Se produjo un error: " + error.message);
  } finally {
    // Código que siempre se ejecuta, independientemente de si se lanzó una excepción o no
    console.log("El bloque try-catch-finally ha terminado.");
  }






  

