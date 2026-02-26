import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from dotenv import load_dotenv

def cargar_datos_supabase(df):
    print("\n>> Cargando datos en la Base de Datos...")
    
    # Ruta donde se guardará la base de datos (raíz del proyecto)
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    raiz_proyecto = os.path.dirname(directorio_actual)
    ruta_env = os.path.join(raiz_proyecto, "config", ".env")

    # Cargar variables de entorno desde el archivo .env
    load_dotenv(dotenv_path=ruta_env)
    db_url = os.getenv("SUPABASE_URL")

    if not db_url:
        print ("No se encontro SUPABASE_URL en el archivo .env")
    
    # Cargar el DataFrame a la base de datos utilizando SQLAlchemy
    try:
        engine = create_engine(db_url)

        df.to_sql('historiall_escuchas',con=engine, if_exists='append', index=False)

        print("Carga exitosa en la Base de Datos.")

    except Exception as e:
        print(f"Error al cargar datos en la Base de Datos: {e}")