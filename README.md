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

#Configuración para notificaciones
El sistema soporta la notificación de turnos con anticipación por SMS y Email.
Para ellos precisa se configure el servicio de envío de SMS y los datos de SMTP correspondiente.
En el archivo settings.py (o bien en variables de entorno) se debe configurar:


* `NOTIFICATION_ANTICIPATION_DAYS`: Cuantos días para adelante mirará el sistema para determinar si debe enviar las notificaciones
* `SEND_SMS_NOTIFICATIONS` = Bolean que permite activar o desactivar las notificaciones por SMS
* `SEND_EMAIL_NOTIFICATIONS` = Bolean que permite activar o desactivar las notificaciones por Email
* `EMAIL_HOST` = IP o host del servicio SMTP
* `EMAIL_PORT` = Puerto del servicio SMTP
* `EMAIL_HOST_USER` =  Usuario con el que se indentificara al servicio de envio SMTP (normalmente es el mail)
* `EMAIL_HOST_PASSWORD` = Password del usuario con el que se indentificara al servicio de envio SMTP
* `EMAIL_SENDER_ADDRESS` = Dirección de correo electronico remitente para el envío de notificaciones
* `EMAIL_USE_TLS` = Bolean indicando si se debe utilizar o no TLS en la comunicación
* `EMAIL_USE_SSL` = Bolean indicando si se debe utilizar o no SSL en la comunicación
* `BASE_SMS_URL` = URL base para el servicio de envio de SMS
* `SMS_SERVICE_USER` = Usuario del servicio de SMS
* `SMS_SERVICE_PASSWORD` : Password del servicio de envio de SMS

## Envio de notificaciones
Para configurar el envio de notificaciones diarias se cuenta con tres metodos dependiendo de las posibilidades tanto del sistema operativo como de la modalidad en la que se instale la plataforma:

* Configurar un cronjob con curl: `curl -X POST $URL_BASE/api/notificaciones/createNotifications/`
* Configurar un cronjob con wget: `wget --post-data='' $URL_BASE/api/notificaciones/createNotifications/`
* Configurar un cronjob con el comando de manage: `python manage.py sendReminders`


## Configuration for sending reminders at 10AM
~~~~
#/etc/systemd/reminders.service

[Unit]
Description=Sends turnosReminders

[Service]
Type=oneshot
ExecStart=/usr/bin/sh -c 'curl -X POST $BASE_URL/api/notificaciones/createNotifications/'
~~~~


~~~~
#/etc/systemd/system/reminders.timer

[Unit]
Description=Send reminders at 10AM

[Timer]
OnCalendar=10:00
Unit=reminders.service
~~~~


