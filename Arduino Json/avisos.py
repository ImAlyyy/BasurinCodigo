import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inicializa la aplicación Firebase
cred = credentials.Certificate('basurin-506ae-firebase-adminsdk-9024k-a19dda2860.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://basurin-506ae-default-rtdb.firebaseio.com/'
})

# Texto a almacenar en el nodo "avisos"
avisos_text = "Hoy no habra servicio de recoleccion"

# Referencia al nodo "avisos"
ref_avisos = db.reference('avisos')

# Almacena el texto en el nodo "avisos"
ref_avisos.set(avisos_text)

print("Aviso almacenado en Firebase exitosamente bajo 'avisos'.")
