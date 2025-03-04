# ETL Workshop 001: Desafío de Ingeniería de Datos

Este proyecto implementa un proceso ETL para migrar datos de candidatos desde un CSV a PostgreSQL, realizar transformaciones y generar visualizaciones sobre contrataciones.

## Tecnologías

- Python
- Jupyter Notebook
- PostgreSQL
- Pandas, Matplotlib, Seaborn

## Instalación

1. Clona el repositorio: `git clone https://github.com/jpgomezv/ETL_Workshop_001.git`
2. Crea un entorno virtual: `python -m venv venv`
3. Activa el entorno: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (macOS/Linux)
4. Instala dependencias: `pip install -r requirements.txt`
5. Configura PostgreSQL y actualiza `.env` con tus credenciales.

## Uso

Ejecuta los notebooks en orden: `01_extract_load.ipynb`, `02_explore_data.ipynb`, `03_transform_data.ipynb`.
