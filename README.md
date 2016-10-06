# Turnos Backoffice

Proyecto que contiene las APIS para el sistema de turnos:

## Tecnologías y frameworks

El sistema se encuentra construido utilizando principalmente :

* Postgres
* Django
* Django Rest Framework
* Django Rest Framework-Filters

## Requisitos
* Python v2/3
* Pip
* Postgres

## Instalación
1. Clonar el repositorio
2. Ejecutar la instalacion de paquetes de python 
```bash
	pip install -r requirements.txt
```
3. Configurar variables de entorno (Revisar sección especifica sobre este tema)
4. Ejecutar migraciones
```bash
	python manage.py migrate
```
5. Crear super usuario
```bash
	python manage.py createsuperuser
```
6. Ejecutar aplicación. (Revisar sección)

## Variables de entorno
El sistema toma de variables de entorno la configuración de la base de datos.
Las variables necesarias son:

* `DB_NAME`: Nombre de la instancia de la base de datos
* `DB_USER`: Nombre del usuario de la base de datos
* `DB_PASSWORD`: Password del usuario de la base de datos
* `DB_HOST`: Host donde se encuentra la base de datos (Ej: 127.0.0.1)
* `DB_PORT`: Puesto donde se encuentra corriendo la base de datos (EJ: 5432) 

## Ejecucion de la aplicación de forma manual
Ejecutar el siguiente comando deja corriendo el sistema en el puerto 8000

```bash
	python manage.py runserver localhost:8000
```

## Datos iniciales
La migración ejecutada en el paso 4 de la instalación carga los datos iniciales de las entidades

* province
* district
* location
* sexType
* documentType
* civilStatusType
* educationType

Para ingresar los datos de la entidad socialService se debe generar un sql y ejecutarlo contra la base de datos. (Referirse a la carpeta formatos_carga_inicial)

## Módulos

### hc_common
Contiene las entidades generales del sistema:

* activeModel
* abstractType
* province
* district
* location
* sexType
* documentType
* civilStatusType
* educationType
* socialService
* persona


### hc_core
Contiene funcionalidades comunes al resto del sistema:

* PaginateListAPIView
* PaginateCreateListAPIView
* user_view
* Definición de la excepción "failedDependencyException"

### hc_pacientes
Contiene las funcionalidades referentes a los pacientes del sistema.
Maneja la entidad Paciente

### hc_practicas
Contiene las funcionalidades referentes a los profesionales, agendas, etc. del sistema.
Maneja las entidades

* especialidad
* prestacion
* profesional
* agenda
* period
* dayOfWeek
* turnoSlot
* turno
* ausencia

### huesped_backend
Core de la sistema. Contiene las configuraciones propias del sistema.


## Estructura general de directorios

Cada modulo cuenta con los directorios

