import socket
import ssl
import requests
from datetime import datetime
import click
from rich.console import Console
from rich.markup import escape  # Importar escape
import time  # Importar time para sleep

console = Console()

# user agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

def get_http_status(url):
    try:
        response = requests.get(f"http://{url}", timeout=5, headers=headers)  # Agregar timeout
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
@click.option('--mode', '-m', default='monitor', help='Execution mode')
@click.option('--interval', '-i', default=60, help='Intervalo de verificación en segundos')
@click.option('--alert', '-a', default='No', help='show notification in desktop')

def monitor_ssl(mode, interval, alert):
    # Leer las URLs desde un archivo .txt
    with open('urls.txt', 'r') as file:
        urls = [line.strip() for line in file if line.strip()]

    if mode == 'monitor':
        console.print("Is monitoring... !", style="bold blue")
        try:
            while True:
                for url in urls:
                    get_http_status(url)
                time.sleep(interval)  # Esperar antes de la próxima iteración

        except KeyboardInterrupt:
            if alert == 'yes':
                exec(open('./notify/keyBoardInterrupted.py').read())

    if mode == 'audit':
        # Leer las URLs desde un archivo .txt
        with open('urls.txt', 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
        
        console.print('[bold cyan]Is auditing... ![/bold cyan]')

        for url in urls:
            current_time = datetime.now().strftime("%H:%M:%S")  # Hora actual en cada llamada
            try:
                # Create a context object for SSL/TLS connections
                context = ssl.create_default_context()

                # Connect to the server using the context
                with socket.create_connection((url, 443), timeout=3) as sock:
                    with context.wrap_socket(sock, server_hostname=url) as ssock:
                        cert = ssock.getpeercert()

                        # Extract and print the expiration date of the certificate
                        exp_date_str = cert['notAfter']
                        exp_date = datetime.strptime(exp_date_str, '%b %d %H:%M:%S %Y %Z')
                        
                        date_difference = abs((exp_date - datetime.now()).days)
                                                
                        #SSL not expired
                        if date_difference >= 31 :
                            console.print(f"[bold cyan][{current_time}][/bold cyan] [bold green]{url} [{exp_date}][/bold green]")

                        #SSL soon expire
                        if date_difference < 30:
                            console.print(f"[bold cyan][{current_time}][/bold cyan] [bold yellow]{url} [{exp_date}][/bold yellow]")

                        #SSL expired
                        if datetime.now() > exp_date:
                            console.print(f"[bold cyan][{current_time}][/bold cyan][bold red]{url} {exp_date}[/bold red]")

                        # Get status
                        response = requests.get(f"http://{url}")
                        statusCode  = response.status_code

            except Exception as e:
                console.print(f"[bold cyan][{current_time}][/bold cyan] {url} [bold red][SSL not found][/bold red]")
                exp_date = f"SSL not found"
                statusCode = "No response"

            # counter = counter + 1
        if alert == 'yes':
            exec(open('notify/AuditCompleted.py').read())

if __name__ == '__main__':
    monitor_ssl()