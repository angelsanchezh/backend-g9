# repositorio del backend de codigo
## este sera el repositorio del curso por las siguientes 10 semanas

toda la info la encontrars en los links  daso pro el discord
markdown tb te da la opcion de usar etiquetas html

levantar mysql en mi terminal de mac
mysql -u root -p  luego hay que poner la clave de la base de datos          usuario root       pass 

se usa.  pip freeze    para saber todas las librerias que hemos instalado manualmente 

se usa    pip freeze > requirements.txt  para crear un archivo que lista todas las librerias que hemos usado
pip install -r requirements.txt   instala todas las librerias con sus versiones indicadas en el archivo 'requirements.txt' que guardamos anteriomente.

pip uninstall -r requirements.txt -y   este comando sirve para desistanlar todas las librerias usadas en el requerimient

1- Chequear si tienes instalado Flask  
pip list , deben aparecer todos los arcchhivos de flask 
2.-pip install flask ( si es que no tienes instalado flask)
3. python3.10 -m venv entorno_flask ( levantar un entorno flask, le pones de nombre entorno flask o el nombre que crees conveniente )
4.source entorno_flask/bin/activate luego activar  el entonro flask
5. en algunos casos hay que escoger cual sera el editor 

--------------------------
trabajando con framework django y python

1  es ideal trabajr dentro de un entorno virtual.

crear entorno virtual con  python3.10 -m venv entorno_flask   , para mac
py -m venv (nombre del entorno)   , para windows


2 activar tu entorno virtual
  source entorno_flask/bin/activate     ,  para mac
  source entorno_flask/Scripts/activate   , para windows 
  
3 instalar django 

pip install Django   chequea version de django   django-admin --version

4 crear proyecto de django 

django-admin startproject (nombredel poryecto) .     se escribe con un espacio y punto al final para no cree una carpeta adicional de tu nuevo proyecto y lo cree en la misma carpeta inicial.

5 correr el poyecto creado

python3.10 manage.py runserver     para mac
python manage.py runserver      para windows 

6 empezar creando una aplicacion 

python manage.py startapp (nombre de la apliacion)     para windows
python3.10  manage.py startapp (nombre de la apliacion)  para mac

7 ahora toca resgistrar tu apliccion dentro de settings de django

dentro de la carpeta settings  buscar la linea que tenga las aplicaciones que usa por defecto django
INSTALLED_APPS  en la ultima linea agregar el nombre de tu aplicacion de esta forma      '(nombre de tu aplicicion)'

8 no olvides crear tu archivo .gitignore  con al finalidad de que no subas a tu repositorio , archvivos que pesan mucho , dependencias, claves o archivos innecesarios
  tambien no olvides crear e instalar tu dependencias ccon un archivo que hs creado de requirements.txt , fijate tambien el interpret que estas usando , y que hayas levantado o activado tu entorno.
  
9  para empezar a mostrar algo, 
primero dentro de tu carpeta del aplicativo ingresa a la carpeta VIEWS importa      from django.http import HttpResponse
ahoravamos a declarar un funcion 
ejemplo

  def inicio(request):
      return HttpResponse("Hol , bienvenido)
      
 Luego dentro de la carpeta de tu aplicativo tienes que crear el archivo      urls.py    dentro vamosa imoprtar   from django.urls import path
 from . import  views (para saber que que vistas vamos a ingresar ) , luego   escribir  
 urlpatterns = [ 
      path('',views.nombre de la funcion de creaste en la carpet views,name='un nombre que le pongas ') ]
 
 por ultimote tienes que ir a las urls del mismo sistema importar    from django.urls import include  y por utlimo especificar dentro de su propio urlspatterns la rta que vas a mostrar   path('',include('gestionVeterinaria.urls')),


<p aling="center" >
<img src='https://codigo.edu.pe/public/img/codigo-logo.png'>

</p>


Cada semana esta en una rama independiente, en la cual se ira detallando a continuación: -
 Semana 01: <a href="https://github.com/angelsanchezh/backend-g9/tree/semana01">LINK</a> - 
 Semana 02: <a href="https://github.com/angelsanchezh/backend-g9/tree/semana02">LINK</a> -
  Semana 03: <a href="https://github.com/ederivero/backend-g9/tree/semana03">LINK</a> - 
  Semana 04: <a href="https://github.com/ederivero/backend-g9/tree/semana04">Link </a>
  Semana 05: <a href="https://github.com/ederivero/backend-g9/tree/semana05">Link </a>
  Semana 06:  <a href="https://github.com/ederivero/backend-g9/tree/semana06">Link </a>
  Semana 07:  <a href="https://github.com/ederivero/backend-g9/tree/semana07">Link </a>
  Semana 08: <a href="https://github.com/ederivero/backend-g9/tree/semana08">Link </a>
  Semana 09: No hay - 
  Semana 10: No ha
