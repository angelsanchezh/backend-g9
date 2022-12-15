import { Usuario } from "../models/usuarioModel.js";
import bcryptjs from "bcryptjs";


export async function registro (req,res) {
    const data = req.body;
    console.log(data);

    try{ 
        const password = bcryptjs.hashSync(data.password,10);
        const nuevoUsuario = await Usuario.create({...data, password});
        console.log(nuevoUsuario);

        res.status(201).json({
            message:"usuario creado exitosamente",
        });
    } catch(error) {
        res.status(500).json({
            message:"error a crear usuario usuario",
        }); 
    }}

    export async function login(req,res){
        const data =req.body;
        const usuarioEncontrado = await Usuario.findOne({email: data.email  });
        if (!usuarioEncontrado){
            return res.status(404).json({

                message: "el susuario no existe",
        });

    }
    if (bcryptjs.compareSync(data.password,usuarioEncontrado.password)){
        res.json({
            message:"bienvenida",
        });

    }else{
        res.json({
            message:"error al ingresar la contrasena",
        });

    }
    

}