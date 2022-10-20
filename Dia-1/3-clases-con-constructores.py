from email.headerregistry import ContentDispositionHeader


class Documento:
    def __init__(self,tipo,num_paginas,editable,contenido):
        #__init__> sera el metodo que se llame cuando creemmos una instancia de la clases
        #en el cosntructor difinios unn nuevo atributo entonces este se creara para toda la clase.
    
        self.tipo = tipo
        self.num_paginas = num_paginas
        self.editable = editable
        self.contenido = contenido
    def editar_documento(self,nuevo_contenido):

        #si el documento no es editable entonces inidcar que no se pued editar el docuemnto , caso contario modificar la informacion del atrbibuto del contenido 

        if(self.editable==False):
            print('el archivo no puede ser modificado')

        else:
            print('el archivo fue modificado')


mi_curriculum = Documento(tipo='PDF', num_paginas=80, editable=False,contenido='Soy Developer')

proforma_pagina_web = Documento(tipo='word', num_paginas=3, editable=True,contenido='La pagina web vale 2500 soles')

mi_curriculum.editar_documento(nuevo_contenido='Ahora soy disenador')
proforma_pagina_web.editar_documento(nuevo_contenido='La pagina vale 4000 soles, baratooo')