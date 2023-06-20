// Definir una cadena
const cadena = "¡Hola, mundo!";

// length(): devuelve la longitud de la cadena
console.log(cadena.length); // Output: 13

// indexOf(): devuelve el índice de la primera aparición de una subcadena
console.log(cadena.indexOf("mundo")); // Output: 6

// lastIndexOf(): devuelve el índice de la última aparición de una subcadena
console.log(cadena.lastIndexOf("o")); // Output: 8

// charAt(): devuelve el carácter en un índice específico
console.log(cadena.charAt(0)); // Output: "¡"

// concat(): concatena dos o más cadenas
console.log(cadena.concat(" Adiós, mundo!")); // Output: "¡Hola, mundo! Adiós, mundo!"

// slice(): devuelve una subcadena entre dos índices
console.log(cadena.slice(0, 4)); // Output: "¡Hol"

// substr(): devuelve una subcadena desde un índice específico
console.log(cadena.substr(6)); // Output: "mundo!"

// substring(): devuelve una subcadena entre dos índices
console.log(cadena.substring(6, 11)); // Output: "mundo"

// replace(): reemplaza una subcadena por otra
console.log(cadena.replace("mundo", "universo")); // Output: "¡Hola, universo!"

// toUpperCase(): convierte la cadena a mayúsculas
console.log(cadena.toUpperCase()); // Output: "¡HOLA, MUNDO!"

// toLowerCase(): convierte la cadena a minúsculas
console.log(cadena.toLowerCase()); // Output: "¡hola, mundo!"

// trim(): elimina los espacios en blanco al principio y al final de la cadena
console.log("   Hola, mundo!   ".trim()); // Output: "Hola, mundo!"







