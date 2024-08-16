import time
import firebase_admin
from firebase_admin import credentials, db

# Configura Firebase
cred = credentials.Certificate('basurin-506ae-firebase-adminsdk-9024k-a19dda2860.json')  # Ruta al archivo JSON de credenciales
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://basurin-506ae-default-rtdb.firebaseio.com/'  # Reemplaza con la URL de tu base de datos
})

ref = db.reference('gps_data')  # Reemplaza 'gps_data' con el nodo deseado en tu base de datos

# Lista de coordenadas a ingresar manualmente
coordinates = [
    {'latitude': 23.266129, 'longitude': -106.375588},
    {'latitude': 23.265798, 'longitude': -106.375828},
    {'latitude': 23.265342, 'longitude': -106.376171},
    {'latitude': 23.264955, 'longitude': -106.376779},
    {'latitude': 23.264240, 'longitude': -106.377715},
    {'latitude': 23.263638, 'longitude': -106.378153},
    {'latitude': 23.262022, 'longitude': -106.379039},
    {'latitude': 23.260034, 'longitude': -106.380110},
    {'latitude': 23.258948, 'longitude': -106.380639}
]


# Actualiza cada conjunto de coordenadas en Firebase una por una
for i, coord in enumerate(coordinates):
    try:
        ref.update(coord)
        print(f"Datos actualizados en Firebase: {coord}")
        time.sleep(3)
    except Exception as e:
        print(f"Error al actualizar en Firebase: {e}")
