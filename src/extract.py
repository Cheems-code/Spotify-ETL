import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path="./config/.env")

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# Scope: Le decimos a Spotify qué permisos necesitamos (solo leer el historial)
def extraer_datos_spotify():
    print("Iniciando extracción desde Spotify...")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-read-recently-played"
    ))

    # Extracción: Pedimos las últimas 50 canciones que se escucharon en la cuenta
    resultados = sp.current_user_recently_played(limit=50)

    return resultados

# Solo para probar que funciona si funciona solo el archivo de extracción
if __name__ == "__main__":
    datos = extraer_datos_spotify()
    print(f"Se extrajeron {len(datos['items'])} registros.")