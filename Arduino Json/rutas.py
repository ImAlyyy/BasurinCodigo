import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inicializa la aplicación Firebase
cred = credentials.Certificate('basurin-506ae-firebase-adminsdk-9024k-a19dda2860.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://basurin-506ae-default-rtdb.firebaseio.com/'
})

# Coordenadas a almacenar
coordinates = [
    {'latitude': 23.266650, 'longitude': -106.375249},
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

# Datos a enviar bajo el nodo "rutas"
data = {
    'ruta1': coordinates
}

# Referencia al nodo "rutas"
ref = db.reference('rutas')

# Almacena los datos en el nodo "rutas"
ref.set(data)

print("Coordenadas almacenadas en Firebase exitosamente bajo 'ruta1'.")
