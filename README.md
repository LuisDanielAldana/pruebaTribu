# pruebaTribu
## Desarrollo de la aplicacion
Se opto por un diseñar una aplicacion quew almacena informacion de autores y sus obras.
Se crearon dos modelos de datos diferentes, uno para los autores y otro para los libros, dentro del modelo de libros se creo una relacion con el modelo de autores mediante el campo autor.
Para agregar y editar tanto libros como autores se crearon vistas con formas que deben ser llenadas para proseguir.
Se empleo diseño de aplicacion sensillo para concentrarse en el desarrollo de funcionalidades.
A un lado de cada registro se agregaron botones que permiten editar y eliminar los registros los cuales redirijen al usuario a una ventana nueva.

## Configuracion de aplicacion
Una vez descargado el repositorio es necesario abrir en una terminal la ubicacion del mismo.
Una vez ahi, correr el comando "pip install -r requirements.txt" para instalar las dependencias necesarias.
para correr el proyecto, usar el comando "python manage.py runserver 8000"
Una vez que esta corriendo el proyecto acceder a la direccion "http://127.0.0.1:8000/biblioteca/registro/" donde se podra crear un usuario.
Al crear el usuario, se accedera a la aplicacion.
En la aplicacion se pueden ver una lista de libros y autores, estos se pueden crear, editar y eliminar.
Hay un limite establecido en el codigo de 5 registros por pagina.
