#!/bin/bash

# Ruta al script de Python
python_script="/home/moranciox/Escritorio/lab3/system_report.py"

# Variables para el script de envío de correo
SENDER="edumormu95@gmail.com"
RECIPIENT="eduardoignacio.moran@gmail.com"
SUBJECT="Informe del Sistema"

# Obtener el informe directamente en el script de Bash
system_report=$("$python_script")

# Enviar el correo con el informe HTML adjunto
echo -e "$system_report" | mail -s "${SUBJECT}" -a "MIME-Version: 1.0" -a "Content-Type: text/html" -r "${SENDER}" "${RECIPIENT}"
