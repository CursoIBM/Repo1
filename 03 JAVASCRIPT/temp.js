
const peliculas = [
    { pelicula: "El padrino", director: "Coppola", año: 1972 },
    { pelicula: "El Padrino: Parte II", director: "Coppola", año: 1974 },
    { pelicula: "El Caballero de la Noche", director: "Christopher Nolan", año: 2008 },
    { pelicula: "La lista de Schindler", director: "Steven Spielberg", año: 1993 }
];

/*
const nombresPeliculas = peliculas.map(function (pelicula) {
    return pelicula.pelicula;
});
*/

const nombresPeliculas = peliculas.map((x) => x.pelicula);

console.log(nombresPeliculas); 

// ["El padrino", "El Padrino: Parte II", "El Caballero de la Noche", "La lista de Schindler"]


