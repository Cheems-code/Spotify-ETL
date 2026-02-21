import sqlite3
import pandas as pd
import os

def cargar_datos_sqlite(df, nombre_bd="spotify_etl.db"):
    print("\n>> Paso 4: Cargando datos en la Base de Datos...")
    
    # 1. Ruta donde se guardará la base de datos (raíz del proyecto)
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    raiz_proyecto = os.path.dirname(directorio_actual)
    ruta_bd = os.path.join(raiz_proyecto, nombre_bd)
    
    try:
        # 2. Creamos la conexión (si el archivo .db no existe, Python lo creará automáticamente)
        conexion = sqlite3.connect(ruta_bd)
        
        # 3. Pandas: envía todo el DataFrame a SQL en una sola línea
        df.to_sql('historial_escuchas', con=conexion, if_exists='append', index=False)
        
        print(f"¡Carga exitosa! Datos guardados en la tabla 'historial_escuchas' dentro de {nombre_bd}")
        
    except Exception as e:
        print(f"Error al cargar los datos en la base de datos: {e}")
        
    finally:
        # 4. Cerramos la conexión
        conexion.close()