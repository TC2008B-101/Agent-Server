# Inicializar el entorno virtual

Configuración del Entorno

Para la ejecución de los servidores, se recomienda configurar un entorno virtual de Python, el cual puede denominarse “server” o “agents-server” para mantener una organización clara del proyecto.

Creación del Entorno Virtual en Python (Mac, Linux, Windows):

Mac/Linux:

```
source server/bin/activate
```

Windows:

```
python3 -m venv server
```


Activación del Entorno Virtual en Python:
Mac/Linux:
```
source server/bin/activate
```
Windows:
```
server\Scripts\activate
```

Instalación de Dependencias:
Dentro del entorno virtual activado, instala las dependencias necesarias:
```
pip install -r requirements.txt
```
Ejecución del Servidor

```
python main.py
python3 main.py
```


Una vez configurado el entorno, el servidor se puede ejecutar mediante el archivo “main.py”, el cual inicia la aplicación del servidor. Por defecto, la aplicación expone sus endpoints en la ruta “http://localhost:5000/api/simulation”. Este endpoint es crucial tanto para obtener datos como para crear nuevas simulaciones.

El proyecto incluye varios archivos, algunos de los cuales son críticos para el funcionamiento del servidor. No se recomienda modificar la configuración de archivos que no sean esenciales. Sin embargo, si se requiere hacer ajustes específicos, los archivos clave a considerar son:
app.py: Este archivo contiene la configuración inicial del servidor Flask y la integración con Flask-CORS para manejar solicitudes entre dominios. También registra las rutas definidas en simulation_routes.py.

simulation_routes.py: Este archivo define las rutas de la API para gestionar las simulaciones. Utiliza un blueprint de Flask para agrupar las rutas relacionadas bajo /api/simulation. Las rutas principales permiten la creación de nuevas simulaciones y la obtención de simulaciones existentes desde la base de datos. Además, incluye la validación de las solicitudes entrantes para asegurar que cumplen con el esquema esperado.

db.py: Este archivo maneja la conexión con la base de datos MongoDB. Se utiliza pymongo para establecer la conexión y realizar operaciones CRUD en la colección de simulaciones. La configuración incluye el uso de un URI seguro obtenido de MongoDB  y el manejo de certificados para la conexión TLS.
Estos archivos son esenciales para la creación del servidor, la definición de rutas y la conexión a la base de datos. Es importante tener precaución al realizar modificaciones en ellos para mantener la integridad y funcionalidad del servidor.
