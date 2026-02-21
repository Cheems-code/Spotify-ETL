from src.extract import extraer_datos_spotify
from src.transform import transformar_datos_spotify
from datetime import datetime
import os

def ejecutar_pipeline_etl():
    print(" Iniciando el Pipeline ETL de Spotify...\n")

    try:
        #f1: extraer
        print(">> Paso 1: Extrayendo datos...")
        datos_crudos = extraer_datos_spotify()
        
        #f2: transformar
        print(">> Paso 2: Transformando y limpiando datos...")
        df_limpio = transformar_datos_spotify(datos_crudos)
        
        #fi: Guardar localmente
        print(">> Paso 3: Guardando en archivo CSV local...")
        
        #generamos la ruta asegurándonos de que la carpeta exista
        carpeta_destino = "data/processed"
        os.makedirs(carpeta_destino, exist_ok=True) 
        
        # Le ponemos la fecha de hoy al archivo para llevar un historial
        fecha_hoy = datetime.now().strftime("%Y%m%d")
        ruta_archivo = f"{carpeta_destino}/historial_spotify_{fecha_hoy}.csv"
        
        # Guardamos el DataFrame de Pandas como un archivo .csv sin el índice numérico
        df_limpio.to_csv(ruta_archivo, index=False)
        
        print(f"\n ¡Pipeline ejecutado con éxito!")
        print(f" Tus datos limpios están guardados en: {ruta_archivo}\n")
        
        # Mostramos una pequeña muestra (las primeras 5 filas)
        print("Muestra de tus datos listos para analizar:")
        print("-" * 50)
        print(df_limpio.head())
        print("-" * 50)

    except Exception as e:
        # Si algo falla en cualquier parte del proceso, lo atrapamos aquí
        print(f"\n Ocurrió un error en el pipeline: {e}")

# Esto asegura que el código solo corra si ejecutamos este archivo directamente
if __name__ == "__main__":
    ejecutar_pipeline_etl()