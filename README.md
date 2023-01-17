# Challenge para la empresa Powermeter

Para el presente repositorio, se siguieron las instrucciones indicadas en este [archivo](Instrucciones.pdf).



## Aclaraciones

### Ejercicio 1

- Si bien es una sola aplicación la que se usa (medidores), se puso en una carpeta llamada *'apps'* para que sea escalable.
- Como no se aclara el tipo de dato que es el consumo de potencia, se definió como flotante.
- Para documentar la API se usa swagger.
- Para desplegar la aplicación se usa uWSGI con nginx.
- El proyecto está construido en un entorno virtual con pipenv.
- Se acompaña el proyecto con una base de datos con datos cargados para tests.
- Se acompaña set de tests unitarios.



## Documentación

Todos los *endpoints* de la aplicación están documentados en `/api/docs`



## Preparación de entorno de trabajo

1) Clonar repositorio

   ```
   $ git clone https://github.com/lcastiglione/challenge-powermeter.git
   ```

2) Para el *ejercicio-1*, entrar en dicha carpeta y ejecutar:

   ```
   $ pipenv shell
   $ pipenv install
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





## Dependencias principales utilizadas

```text
Django==4.1.5
djangorestframework==3.14.0
drf-yasg==1.21.4
```

