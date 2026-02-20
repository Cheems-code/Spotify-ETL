import pandas as pd

# Función de validación de calidad de datos (Data Quality)
def check_if_valid_data(df: pd.DataFrame) -> bool:
    # 1. ¿Está vacía la tabla?
    if df.empty:
        print("No se encontraron canciones. Finalizando ejecución.")
        return False

    # 2. Revisar si hay duplicados exactos (Primary Key Check)
    # En Spotify, la fecha/hora exacta en que escuchaste una canción (played_at) debe ser única
    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        raise Exception("Se rompió la regla de Primary Key: Hay duplicados en la fecha de reproducción.")

    # 3. Revisar si hay valores nulos en columnas importantes
    if df.isnull().values.any():
        raise Exception("Valores nulos encontrados en los datos.")

    return True


def transformar_datos_spotify(datos_crudos):
    print("Iniciando transformación de datos...")
    
    canciones = []
    artistas = []
    fechas_reproduccion = []
    
    # Navegamos por el JSON "sacando cosas de las cajas"
    for item in datos_crudos['items']:
        canciones.append(item['track']['name'])
        artistas.append(item['track']['artists'][0]['name'])
        fechas_reproduccion.append(item['played_at'])
        
    # Creamos un diccionario preparándolo para Pandas
    diccionario_canciones = {
        "cancion": canciones,
        "artista": artistas,
        "played_at": fechas_reproduccion
    }
    
    # Convertimos a un DataFrame (Tabla) de Pandas
    df_canciones = pd.DataFrame(diccionario_canciones)
    
    # Limpiamos el formato de la fecha/hora para que la base de datos lo entienda bien
    df_canciones['played_at'] = pd.to_datetime(df_canciones['played_at'])
    
    # Validamos que los datos sean de calidad antes de devolverlos
    if check_if_valid_data(df_canciones):
        print("Datos transformados y validados correctamente.")
    
    return df_canciones