# API-Django
Application Programming Interface - Django Rest Framework (DRF)

# **Introducción**

Tendremos dos aplicaciones en nuestro proyecto: la primera será la "core". Esta aplicación contendrá la lógica para nuestro endpoint de contacto. La segunda será de "ecommerce". Esta aplicación contendrá la lógica para nuestros puntos finales de items y orders.


## *Tecnologías utilizadas:*
* **Tecnologías:** 
    * Paython 3.10
    * Django 4.1
    * Django Rest Framework 3.14.0
    * django_extensions 3.2.1

* **Autenticación:**
    * rest_framework.authtoken

* **Documentación:**
    * Swagger UI (drf-yasg 1.21.7) 


## *Estructura del proyecto:*
* **core:** Contiene el modelo `Contact` para gestionar mensajes de contacto.

* **ecommerce:** Incluye los modelos `Item`(productos) y `Order` para gestionar pedidos.

## *Instalación:*
Este repositorio es de acceso **público** se recomienda:
1. Realizar `git clone https://github.com/villarrealfx/API-Django.git`.
2. Crear un entorno virtual de trabajo con alguna herramienta python tal como [venv](https://docs.python.org/3/library/venv.html) y activarlo según su sistema operativo.
3. instalar las dependencias que se encuentran en el archivo `requirements.txt` utilizando el comando `pip install -r requirements.txt`.
4. Configurar la base de datos:
    * Editar el archivo `settings.py` con tus credenciales de base de datos.
    * Realizar las migraciones: `python manage.py migrate`
5. Ejecutar el servidor de desarrollo: `python manage.py runserver`

## Consideraciones adicionales:
Ejecutar Pruebas unitarias.
1. En la raiz del proyecto donde se encuentra el archivo manage.py correr el siguiente código `python manage.py test`esto correrá las pruebas unitarias de los archivos `tests.py`ubicados en cada una de las apps.

Limitaciones.
1. La presente API esta realizada para verificar la funcionabilidad de algunos módulos de `Django Rest Framework, drf-yasg` etc por lo que su funcionalidad está limitada a estos.



