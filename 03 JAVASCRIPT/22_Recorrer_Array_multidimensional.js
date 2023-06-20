// Recorre Arrays nultidimensionales. 


var peliculas = ['Batman', 'Cars', 'It', 'Predator'];
var categoria = ['accion', 'infantil', 'Terror'];

var cine = [peliculas, categoria];


for(i=0;i<cine.length;i++){
    for(j=0;j<cine[i].length; j++){
        console.log(cine[i][j]);
    }
}










