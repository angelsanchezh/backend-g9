
import express, {json} from "express";
import { productosRouter } from "./routes/productos.routes.js";

const  servidor = express();
servidor.use(json());

//VARIABLES DE entorno 
const PORT = process.env.PORT ??  5000;

servidor.use(productosRouter)

servidor.listen (PORT,()=>{

console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);

});
