#  How to resolve Coding Challenge - Bitcoin Price
# Objective:
Develop an automated and scalable process to obtain the 5-day moving
average of Bitcoin's price during the first quarter of 2022.
# Brief:
The finance team needs to analyze Bitcoin's behavior to determine if it's feasible to invest in this cryptocurrency. Your task is to automate this process and be prepared for real-time adjustments when necessary.
# Tasks:
1. Explore the Crypto API CoinGecko API Documentation
2. Create a DEMO account in the API to avoid any costs.
3. Retrieve a list of all cryptocurrencies with id, name, and symbol (using the CoinGecko API).
4. Retrieve the Bitcoin coin id.
5. Get Bitcoin's price in USD and by date for the first quarter of 2022 (using the CoinGecko API).
6. Save the data in the database of your choice.
7. Use the data previously stored in the database to calculate the 5-day moving average using a window/partition function in Python (you may use either pandas or PySpark).

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
