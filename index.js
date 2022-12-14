import mongoose from "mongoose"
import express from "express"

const productoSchema = new mongoose.Schema({
nombre : {
    type: mongoose.Schema.Types.String,
    unique: true,
    maxLength: 50,
    required: true,
},
precio :{
    type: mongoose.Schema.Types.Decimal128,
    max:100.0,

}

});

const producto = mongoose.model('Producto',productoSchema);

const servidor = express();
const PORT = process.env.PORT || 5000;

servidor.listen (PORT,async()=>{

    console.log(`Servidor corriendo exitosamente en el ${PORT}`);
    try{
        await mongoose.connect("mongodb://localhost:27017/express");
        console.log("conexion a la base de datos exitosa");
    } catch(e){
       console.log(e);
       console.log("error al conectarse a la base de datos");
    }

})

