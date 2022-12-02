// import isodd from "is-odd";
const informacion = require("./infoAdicional")
const isodd = require("is-odd");
const esPar = isodd(15);

console.log("hola");

console.log(esPar);

console.log(informacion.edad);
const saludo = informacion.saludar("rigoberto");
console.log(saludo);