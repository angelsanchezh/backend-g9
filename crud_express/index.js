import express, {json} from "express";



const servidor = express();
servidor.use(json());
const productos = [
    { nombre: "pollada",
     precio : 15.5,
     disponible : true,


    },
    { nombre: "adobada",
    precio : 16.5,
    disponible : true,


   },
   { nombre: "chicharronada",
   precio : 17,
   disponible : true,


  },
  { nombre: "chuletada",
     precio : 12.5,
     disponible : false,


    },

];



servidor.get("/", (req,res)=>{
console.log ("entro aqui");

res.status (200).json ({
    message:"bienvenido a mi api de express",
});

});

servidor 
.route('/productos')
.get((req,res)=>{ 
 const productosdisponibles = productos.filter((producto) => {
    return producto.disponible === true;});

    res.status(200).json({
        content :productosdisponibles,
        
      
    });
})
.post((req,res) => {

    console.log(req.body);
    const  data =req.body;

    productos.push(data)

    res.status(201).json({
        message : "producto creado exitosamnet",
});
});





servidor.listen(5000, ()=> {

    console.log('servidor corriendo exitosamente en el puerto 5000')
});