# Proyecto ETL con Spotify y Supabase

Este proyecto es un pipeline de Extracción, Transformación y Carga (ETL) diseñado para procesar tu historial de canciones escuchadas en Spotify y almacenarlo en una base de datos de Supabase.

## Descripción

El pipeline ETL realiza los siguientes pasos:
1.  **Extrae**: Se conecta a la API de Spotify para obtener las últimas 50 canciones que has escuchado.
2.  **Transforma**: Limpia y estructura los datos, seleccionando el nombre de la canción, el artista y la fecha de reproducción. Realiza validaciones de calidad de datos para asegurar que no haya duplicados ni valores nulos.
3.  **Carga**: Inserta los datos transformados en una tabla en una base de datos PostgreSQL alojada en Supabase, evitando duplicados si una canción ya fue registrada a la misma hora.

## Tecnologías Utilizadas

-   **Python**: Lenguaje principal del proyecto.
-   **Pandas**: Para la manipulación y transformación de datos.
-   **Spotipy**: Una biblioteca de Python para la API Web de Spotify.
-   **SQLAlchemy**: Para interactuar con la base de datos PostgreSQL.
-   **Psycopg2**: Adaptadpr de PostgreSQL para Python.
-   **Supabase**: Plataforma de backend como servicio que provee una base de datos PostgreSQL.
-   **Docker**: Para la contenerización de la aplicación.

## Estructura del Proyecto

```
.
├── Dockerfile
├── main.py
├── readme.md
├── requirements.txt
├── config/
│   └── .env.example
├── data/
│   ├── processed/
│   └── raw/
└── src/
    ├── extract.py
    ├── load.py
    └── transform.py
```

-   `main.py`: El script principal que orquesta todo el proceso ETL.
-   `src/extract.py`: Módulo para extraer las 50 canciones más recientes de Spotify.
-   `src/transform.py`: Módulo para transformar los datos crudos en un DataFrame de Pandas y validar su calidad.
-   `src/load.py`: Módulo para cargar los datos transformados a la base de datos en Supabase.
-   `config/.env.example`: Archivo de ejemplo para las variables de entorno necesarias.
-   `Dockerfile`: Define la configuración para construir una imagen de Docker del proyecto.
-   `requirements.txt`: Lista de las dependencias de Python necesarias para el proyecto.

## Configuración

1.  **Clona este repositorio:**
    ```bash
    git clone <url-del-repositorio>
    cd MY_FIRST_ETL
    ```

2.  **Configura las variables de entorno:**
    Crea un archivo `.env` dentro de la carpeta `config`. Puedes duplicar el archivo `.env.example` y renombrarlo.

    ```
    config/.env
    ```

    Necesitarás las siguientes credenciales:

    -   **Spotify API:**
        -   Ve al [Dashboard de Desarrolladores de Spotify](https://developer.spotify.com/dashboard/).
        -   Crea una nueva aplicación.
        -   Copia tu `Client ID` y `Client Secret`.
        -   En la configuración de tu app de Spotify, añade `http://localhost:8888/callback` a los "Redirect URIs".
        -   Añade estas variables a tu archivo `.env`:
            ```env
            SPOTIPY_CLIENT_ID='TU_CLIENT_ID'
            SPOTIPY_CLIENT_SECRET='TU_CLIENT_SECRET'
            SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
            ```

    -   **Supabase:**
        -   Crea un nuevo proyecto en [Supabase](https://supabase.com/).
        -   Ve a `Project Settings` > `Database`.
        -   Copia la `Connection string` (URI) y añádela a tu archivo `.env`:
            ```env
            SUPABASE_URL='TU_CONNECTION_STRING'
            ```

3.  **Crea la tabla en Supabase:**
    Ejecuta el siguiente script SQL en el editor de SQL de Supabase para crear la tabla donde se guardarán los datos:
    ```sql
    CREATE TABLE public.historiall_escuchas (
        cancion VARCHAR(255),
        artista VARCHAR(255),
        played_at TIMESTAMP PRIMARY KEY
    );
    ```

## Instalación

1.  **Crea un entorno virtual e instálalo:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar el pipeline ETL completo, ejecuta el siguiente comando. La primera vez, se te pedirá que inicies sesión en tu cuenta de Spotify en el navegador para autorizar la aplicación.

```bash
python main.py
```

### Ejecución con Docker

También puedes construir y ejecutar el proyecto usando Docker. Asegúrate de que tu archivo `config/.env` esté completo.

1.  **Construye la imagen de Docker:**
    ```bash
    docker build -t mi-primer-etl .
    ```

2.  **Ejecuta el contenedor:**
    ```bash
    docker run --env-file ./config/.env mi-primer-etl
    ```
