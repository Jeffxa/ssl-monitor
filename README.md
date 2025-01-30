
```markdown
# Manual de Usuario: Url Monitor y Auditoría de SSL/TLS

Este manual proporciona una guía detallada para utilizar la aplicación de monitoreo y auditoría de URLs. La aplicación está diseñada para verificar el estado de las URLs (códigos de estado HTTP) y auditar la validez de los certificados SSL/TLS. El archivo principal para ejecutar la aplicación es `app.py`.

---

## Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

1. **Python 3.x**: La aplicación está escrita en Python. Asegúrate de tener Python instalado en tu sistema.
2. **Dependencias de Python**: Instala las bibliotecas necesarias ejecutando el siguiente comando:

   ```bash
   pip install -r requirements.txt
   ```

3. **Archivo `urls.txt`**: Crea un archivo llamado `urls.txt` en el mismo directorio que `app.py`. Este archivo debe contener una lista de URLs que deseas monitorear o auditar, una por línea.

   Ejemplo de contenido de `urls.txt`:
   ```
   example.com
   google.com
   github.com
   ```

---

## Ejecución de la Aplicación

Para ejecutar la aplicación, utiliza el siguiente comando en la terminal:

```bash
python app.py
```

### Opciones de la Línea de Comandos

La aplicación admite varias opciones para personalizar su funcionamiento:

- **`--mode` o `-m`**: Especifica el modo de ejecución. Los valores posibles son:
  - `monitor` (predeterminado): Monitorea el estado de las URLs en intervalos regulares.
  - `audit`: Realiza una auditoría de los certificados SSL/TLS de las URLs.

  Ejemplo:
  ```bash
  python app.py --mode audit
  ```

- **`--interval` o `-i`**: Define el intervalo de tiempo (en segundos) entre cada verificación en modo `monitor`. El valor predeterminado es `60` segundos.

  Ejemplo:
  ```bash
  python app.py --interval 30
  ```

- **`--alert` o `-a`**: Activa las notificaciones de escritorio cuando se completa una auditoría. Los valores posibles son:
  - `no` (predeterminado): No muestra notificaciones.
  - `yes`: Muestra notificaciones.

  Ejemplo:
  ```bash
  python app.py --alert yes
  ```

- **`--report` o `-r`**: Genera un informe en formato Excel después de una auditoría. Los valores posibles son:
  - `no` (predeterminado): No genera un informe.
  - `yes`: Genera un informe.

  Ejemplo:
  ```bash
  python app.py --report yes
  ```

---

## Funcionalidades

### 1. **Modo Monitor (`--mode monitor`)**

En este modo, la aplicación verifica periódicamente el estado de las URLs listadas en `urls.txt`. Muestra el código de estado HTTP de cada URL en la consola, con colores que indican el tipo de respuesta:

- **Códigos 2xx (Éxito)**: Verde.
- **Códigos 4xx o 5xx (Errores)**: Amarillo.
- **Otros códigos**: Púrpura.
- **Errores de conexión**: Rojo.

Ejemplo de salida:
```
[14:30:45] [200] example.com
[14:30:45] [404] notfound.com
```

Para detener el monitoreo, presiona `Ctrl + C`.

---

### 2. **Modo Auditoría (`--mode audit`)**

En este modo, la aplicación realiza una auditoría de los certificados SSL/TLS de las URLs. Verifica:
- La fecha de expiración del certificado.
- El código de estado HTTP.

Además, si se habilita la opción `--report yes`, se genera un archivo Excel con los siguientes datos:
- Fecha de la auditoría.
- URL.
- Código de estado HTTP.
- Fecha de expiración del certificado SSL/TLS.

El archivo de informe se guarda con el nombre `YYYY-MM-DD_HHMM_reporte.xlsx`.

Ejemplo de salida:
```
[Auditing]: example.com
[2023-10-05] [200] example.com [2024-01-01]
```

---

### 3. **Notificaciones de Escritorio (`--alert yes`)**

Si se habilita la opción `--alert yes`, la aplicación mostrará una notificación en el escritorio cuando se complete una auditoría.

---

### 4. **Generación de Informes (`--report yes`)**

Si se habilita la opción `--report yes`, la aplicación generará un archivo Excel con los resultados de la auditoría. El archivo se guardará en el mismo directorio que `app.py`.

---

## Estructura del Proyecto

El proyecto debe tener la siguiente estructura de archivos:

```
/proyecto
│
├── app.py                # Archivo principal de la aplicación
├── urls.txt              # Lista de URLs para monitorear/auditar
├── notify/               # Directorio con scripts de notificación
│   ├── AuditCompleted.py
│   └── keyBoardInterrupted.py
└── README.md             # Manual de usuario (este archivo)
```

---

## Ejemplos de Uso

1. **Monitoreo básico**:
   ```bash
   python app.py --mode monitor --interval 30
   ```

2. **Auditoría con informe y notificación**:
   ```bash
   python app.py --mode audit --report yes --alert yes
   ```

---

## Notas Adicionales

- Asegúrate de que el archivo `urls.txt` esté correctamente formateado y contenga URLs válidas.
- Las notificaciones de escritorio requieren que el sistema operativo admita notificaciones nativas.
- Para detener la aplicación en modo `monitor`, presiona `Ctrl + C`.

---

## Soporte

Si encuentras algún problema o tienes preguntas, no dudes en contactar al equipo de soporte.

¡Gracias por usar nuestra aplicación! 😊
```

Este manual proporciona una guía completa para usar la aplicación, incluyendo cómo configurarla, ejecutarla y entender sus funcionalidades. ¡Espero que sea útil! 😊