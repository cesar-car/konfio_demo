# Proyecto de Procesamiento de Datos

Este proyecto está diseñado para realizar la ingestión, limpieza y generación de informes a partir de datos.

## Estructura del Proyecto

- **`clean_data/`**: Carpeta que contiene los datos procesados.
- **`raw_data/`**: Carpeta que contiene los datos sin procesar.
- **`report_data/`**: Carpeta para los informes generados.
- **`Clean.py`**: Script para limpiar los datos.
- **`Ingest.py`**: Script para la ingestión de datos.
- **`main.py`**: Punto de entrada principal del proyecto.
- **`Report.py`**: Script para generar informes.
- **`config.yml`**: Archivo de configuración del proyecto.
- **`requirements.txt`**: Lista de dependencias del proyecto.

## Requisitos Previos

1. Instala [Python 3.8 o superior](https://www.python.org/downloads/).
2. Instala las dependencias del proyecto ejecutando:

```bash
pip install -r requirements.txt
```

## Configuración

Configura el archivo `config.yml` según tus necesidades. Este archivo contiene parámetros importantes para la ejecución del proyecto.

## Ejecución

1. **Ingesta de Datos**:
   Ejecuta el script `Ingest.py` para cargar los datos sin procesar:
   ```bash
   python Ingest.py
   ```

2. **Limpieza de Datos**:
   Ejecuta el script `Clean.py` para procesar los datos:
   ```bash
   python Clean.py
   ```

3. **Generación de Informes**:
   Ejecuta el script `Report.py` para generar informes a partir de los datos procesados:
   ```bash
   python Report.py
   ```

4. **Ejecución Completa**:
   Para ejecutar todo el flujo de trabajo, usa el archivo `main.py`:
   ```bash
   python main.py
   ```

## Notas

- Asegúrate de que los datos necesarios estén en la carpeta `raw_data/` antes de comenzar.
- Los datos procesados y los informes se guardarán automáticamente en las carpetas correspondientes (`clean_data/` y `report_data/`).

## Contribuciones

Si deseas contribuir al proyecto, por favor envía un pull request o reporta problemas en el repositorio.
