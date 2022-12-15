import express from 'express';
import mongoose  from 'mongoose';
import { usuarioRouter } from './routes/usuarioRouter.js';

const PORT = process.env.PORT ?? 5000;

const server = express();

server.use(express.json());

server.use(usuarioRouter);

server.listen(PORT,async()=>{
    console.log (`servidor corriendo exitosamente en el puerto ${PORT}`);
    try{
        mongoose.set('strictQuery',false);
        await mongoose.connect(process.env.MONGO_URI);
            console.log ('conexion exitosa');
        } catch(error){
            console.log("error al conectarse a la base de datos");
        }

    
});