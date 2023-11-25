#!/usr/bin/env python3
import psutil
import subprocess

def get_system_info():
    # Obtener la información del sistema
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    users_connected = len(psutil.users())
    system_logs = get_last_system_logs()

    # Crear el cuerpo del informe en formato HTML
    report_body = f"""
    <html>
    <body>
    <h2>Informe del Sistema</h2>
    <p>
        Uso de CPU: {cpu_usage}%
        <br>Uso de RAM: {ram_usage}%
        <br>Espacio en disco: {disk_usage}%
        <br>Usuarios conectados: {users_connected}
    </p>
    <h3>Últimos registros del sistema:</h3>
    <p>{system_logs}</p>
    </body>
    </html>
    """

    return report_body

def get_last_system_logs():
    # Obtener los últimos registros del sistema con sudo
    try:
        command_output = subprocess.check_output(['sudo', 'less', '/var/log/messages'], universal_newlines=True)
        last_logs = command_output.splitlines()[-5:]
        return '\n'.join(last_logs)
    except subprocess.CalledProcessError:
        return "Error al leer los registros del sistema."

if __name__ == "__main__":
    system_report = get_system_info()
    print(system_report)
