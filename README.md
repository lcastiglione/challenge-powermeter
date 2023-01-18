# Challenge para la empresa Powermeter

Para realizar este challenge se siguieron las instrucciones indicadas en este [archivo](Instrucciones.pdf).

Tabla de contenido
=================

<!--ts-->

* [Aclaraciones](#Aclaraciones)
* [Documentación](#Documentación)
* [Preparación de entorno de trabajo](#Preparación de entorno de trabajo)
* [Dependencias](#Dependencias)
* [Tests](#tests)
* [Despliegue](#Despliegue)
     * [Ejercicio 1](#Ejercicio 1)
       * [Desarrollo](#Desarrollo)
       * [Producción](#Producción)
     * [Ejercicio 2](#Ejercicio 2)

<!--te-->

## Aclaraciones

- Si bien para este proyecto solo se usa una aplicación (medidores), la puse en una carpeta llamada `apps` porque considero una buena práctica colocar todas las aplicaciones en un solo lugar y separarlas de la configuración del proyecto y otros archivos.
- Para el consumo en kWh, elegí que el tipo de dato sea flotante para incluir consumos chicos. 
- Para la documentación de la API usé swagger que permite, además, realizar test a los endpoints. Utilizo la dependencia `drf-yasg`.
- Django sirve para crear una aplicación, manejar su lógica y gestionar sus datos, pero no se encarga de servir el contenido. Para eso, opté por usar uWSGI como servidor de la aplicación y Nginx como proxy inverso al servidor de la aplicación.
- Adjunto una pequeña base de datos para hacer algunos test. La misma se puede ver a través del panel administrador (`user: admin pass: 1234`).
- Paso las credenciales de administrador por un tema de simplicidad, pero NUNCA hay hacer esto. Para eso, usaría un gestor de credenciales como Vault o GitGuardian.
- Los parámetros `DEBUG` y `ALLOW_HOST` del archivo `settings.py`reciben su valor desde docker al construir la imagen. Si no los encuentran, usa los valores por default para desarrollo.
- Utilizo una configuración básica de Nginx donde le paso algunos parámetros para que funcione en conjunto con uWSGI. Elegí la imagen `nginxinc/nginx-unprivileged:1-alpine` para tenerlo sin privilegios root.
- En los modelos `Measurer` y `Measurement` uso la clase `CreateModelMixin` para generar automáticamente los endpoint para crear medidores y mediciones, respectivamente y la clase `GenericViewSet` para crear los endpoint personalizados de consumo de potencia.
- Con respecto al desarrollo usé pipenv y docker.
- La API posee las siguientes restricciones: 
  - No se permiten números negativos
  - No se puede cargar una medición en un medidor que no existe
  - No pueden haber dos medidores con el mismo ID
  - Si no existen mediciones para un medidor que si existe, devuelve consumo 0.

- Si bien se trata de runa aplicación simple, no pueden faltar los tests unitarios. Se adjunta el set de test para los modelos `Measurer` y `Measurement`.
- Por último, pero no menos importante, no agregué documentación en las funciones porque ya están los tests y no quedaban muchas funciones para hacer esto (se hacía un poco redundante). Pero para proyectos más complejos considero que son necesarias porque le da al desarrollador las herramientas para entender el código y hasta hacer micropruebas para entender cómo funciona (por ejemplo con `doctest`).



## Documentación

Todos los *endpoints* de la aplicación están documentados en `/api/docs`



## Preparación de entorno de trabajo

1. Clonar repositorio

   ```
   $ git clone https://github.com/lcastiglione/challenge-powermeter.git
   ```

2. Instalar la dependencia `pipenv`

   ```
   pip3 install pipenv
   ```

3. Para el *ejercicio-1*, entrar en dicha carpeta y ejecutar:

   ```
   $ pipenv shell
   $ pipenv install
   ```



## Dependencias

```text
Django==4.1.5
djangorestframework==3.14.0
drf-yasg==1.21.4
```



## Tests

Está hecho un set de pruebas unitarias para el modelo Measure y Measurement. Para ejecutarlos, se puede aprovechar la imagen ya construida y usar el siguiente comando:

```bash
$ docker run powermeter sh -c "python manage.py test apps.medidores.tests" 
```

O sino usando el entorno virtual dentro de la carpeta *ejercicio-1*:

```shell
$ python powermeter/manage.py test apps.medidores.tests
```





## Despliegue



### Ejercicio 1

Se puede ejecutar la aplicación en modo desarrollo y/o en producción con uWSGI y NGINX.

#### Desarrollo

Con el entorno virtual cargado, entrar a la carpeta *ejercicio-1*:

```shell
$ python powermeter/manage.py runserver 3000
```

Luego entrar al link `http://localhost:3000`



#### Producción

1. Dentro de la carpeta *ejercicio-1* ejecutar:

   ```bash
   $ docker compose up --build
   ```

2. Entrar al link `http://localhost:8080`

3. También se puede entrar al panel administrador  `http://localhost:8080/admin`, usando el usuario `admin` y contraseña `1234`.

   > Nota
   >
   > Se muestra el usuario y contraseña para poder realizar pruebas con datos ya cargados en la base de datos.

4. Para iniciar de nuevo los contenedores ejecutar:

   ```bash
   $ docker start powermeter-nginx powermeter
   ```

   

### Ejercicio 2

Para este punto no se usa entorno virtual. Dentro de la carpeta *ejercicio-2* ejecutar:

```bash
$ python main.py
```


