import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 1. Tus credenciales (En un proyecto real, esto iría oculto en un archivo .env)
CLIENT_ID = "df1783bcb7ac46b3a850e3f7363dc7c3"
CLIENT_SECRET = "391f652e93b24375ad311aecebfc7e1a"
REDIRECT_URI = "http://127.0.0.1:8000/callback"

# 2. Scope: Le decimos a Spotify qué permisos necesitamos (solo leer el historial)
SCOPE = "user-read-recently-played"

print("Iniciando conexión con Spotify...")

# 3. Autenticación (OAuth)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# 4. Extracción: Pedimos las últimas 50 canciones que has escuchado
resultados = sp.current_user_recently_played(limit=50)

# 5. Prueba de éxito: Imprimimos la primera canción para confirmar que funcionó
if resultados['items']:
    primera_cancion = resultados['items'][0]['track']['name']
    artista = resultados['items'][0]['track']['artists'][0]['name']
    print(f"¡Éxito! La última canción que escuchaste fue: '{primera_cancion}' de {artista}")
else:
    print("No se encontraron canciones recientes. ¡Ve a escuchar algo en Spotify y vuelve a intentar!")