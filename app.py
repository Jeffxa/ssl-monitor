import socket
import ssl
import requests
from datetime import datetime
import pandas as pd
import click
from rich.console import Console
from rich.markup import escape  # Importar escape
import time  # Importar time para sleep

console = Console()

def get_ssl_info(url):
    try:
        while True:
            # Cargar el archivo Excel
            with open('urls.txt', 'r') as file:
                for urls in file:
                    urls = [line.strip() for line in file if line.strip()]  # Leer líneas no vacías
                    
        response = requests.get(f"http://{url}", timeout=5)  # Agregar timeout
        status_code = str(response.status_code)
        current_time = datetime.now().strftime("%H:%M:%S")  # Hora actual en cada llamada

        # Escapar la URL y el código de estado
        escaped_url = escape(url)
        escaped_status = escape(status_code)

        if status_code.startswith('2'):
            console.print(f"[bold cyan][{current_time}][/bold cyan] [bold bright_white][{escaped_status}][/bold bright_white] [bold green]{escaped_url}[/bold green]")
        elif status_code.startswith('4') or status_code.startswith('5'):
            console.print(f"[bold cyan][{current_time}][/bold cyan] [bold bright_white][{escaped_status}][/bold bright_white] [bold yellow]{escaped_url}[/bold yellow]")
        else:
            console.print(f"[bold cyan][{current_time}][/bold cyan] [bold bright_white][{escaped_status}][/bold bright_white] [bold purple]{escaped_url}[/bold purple]")

    except requests.exceptions.RequestException as e:
        current_time = datetime.now().strftime("%H:%M:%S")
        console.print(f"[bold cyan][{current_time}][/bold cyan] [bold bright_white][UNKNOWN][/bold bright_white] [bold red]{escape(url)}[/bold red]")

@click.command()
@click.option('--mode', '-m', default='monitor', help='Modo de ejecución')
@click.option('--interval', '-i', default=60, help='Intervalo de verificación en segundos')

def monitor_ssl(mode, interval):
    if mode == 'monitor':
        console.print("Iniciando monitoreo...", style="bold blue")
        try:    
            
            get_ssl_info(urls)
            time.sleep(interval)  # Esperar antes de la próxima iteración
            return urls
        except KeyboardInterrupt:
            console.print("\nMonitoreo detenido.", style="bold red")

if __name__ == '__main__':
    monitor_ssl()