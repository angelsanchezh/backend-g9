import { Usuario } from "../models/usuarioModel.js";

export async function registro (req,res) {
    const data = req.body;
    console.log(data);

    try{ 
        const nuevoUsuario = await Usuario.create(data);
        console.log(nuevoUsuario);

        res.status(201).json({
            message:"usuario creado exitosamente",
        });
    } catch(error) {
        res.status(500).json({
            message:"error a crear usuario usuario",
        });

        
    }}