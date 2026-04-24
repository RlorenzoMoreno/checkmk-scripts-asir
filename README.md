# Monitorización Checkmk - Scripts personalizados

Este repositorio contiene scripts desarrollados en Python para ampliar la monitorización en Checkmk mediante local checks.

## Descripción

Los local checks permiten ejecutar scripts personalizados en los hosts monitorizados y enviar el resultado al servidor Checkmk como un servicio adicional.

Estos scripts se han desarrollado como parte de un proyecto ASIR para extender la monitorización más allá de los chequeos estándar.

## Scripts incluidos

check_logs.py

Analiza el archivo de logs del sistema (/var/log/syslog) y cuenta el número de errores recientes.

Estados:
- OK: sin errores
- WARNING: menos de 5 errores
- CRITICAL: 5 o más errores


check_apache_procs.py

Comprueba si existen procesos activos del servicio Apache.

Estados:
- OK: al menos 1 proceso activo
- CRITICAL: sin procesos (servicio caído)


## Instalación

Copiar los scripts en el directorio del agente:

/usr/lib/check_mk_agent/local/

Asignar permisos de ejecución:

chmod +x /usr/lib/check_mk_agent/local/*.py


## Integración en Checkmk

1. Ejecutar el agente para verificar la salida:
check_mk_agent

2. Acceder a Checkmk

3. Realizar Service Discovery

4. Añadir los nuevos servicios detectados


## Validación

Para validar check_logs.py:
Generar errores en logs con el comando:
logger "ERROR prueba checkmk"

Para validar check_apache_procs.py:
Parar el servicio Apache:
sudo systemctl stop apache2

Y comprobar que el estado cambia a CRITICAL.

Posteriormente arrancar el servicio:
sudo systemctl start apache2


## Proyecto

Desarrollado como parte del proyecto de monitorización de sistemas con Checkmk en ASIR.
