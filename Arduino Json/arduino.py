import serial
import json
import firebase_admin
from firebase_admin import credentials, db

# Configura el puerto serial
ser = serial.Serial('COM5', 9600)  # Asegúrate de cambiar 'COM5' al puerto adecuado para tu sistema
ser.flush()

# Configura Firebase
cred = credentials.Certificate('basurin-506ae-firebase-adminsdk-9024k-a19dda2860.json')  # Ruta al archivo JSON de credenciales
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://basurin-506ae-default-rtdb.firebaseio.com/'  # Reemplaza con la URL de tu base de datos
})

ref = db.reference('gps_data')  # Reemplaza 'gps_data' con el nodo deseado en tu base de datos

while True:
    if ser.in_waiting > 0:
        try:
            data = ser.readline().decode('utf-8', errors='replace').strip()
            if data.startswith('{'):
                json_data = json.loads(data)
                # Actualiza los datos en el mismo nodo
                ref.update(json_data)
                print(f"Datos actualizados en Firebase: {json_data}")
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            print(f"Error: {e}")

