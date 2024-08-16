#include <SoftwareSerial.h>

SoftwareSerial miSerial(2, 3); // Rx, Tx

void setup() {
  // Abre la configuración serial para la PC
  Serial.begin(9600); // Abre puerto a 9600 bps
  while (!Serial) {
    // Espera por conexión
    ;
  }
  Serial.println("Serial PC Conectado");

  // Abre la comunicación serial para el SIM808
  miSerial.begin(9600);
  while (!miSerial) {
    // Espera por la conexión serial
    ;
  }

  Serial.println("Serial SIM808 Conectado");
  delay(2000);

  // Enviar comandos AT para inicializar GPS
  miSerial.println("AT+CGNSPWR=1"); // Encender GPS
  delay(1000);
  miSerial.println("AT+CGNSINF");   // Enviar comando CGNSINF para obtener datos GPS
}

void loop() {
  // Leer datos de respuesta del SIM808
  if (miSerial.available()) {
    String data = miSerial.readStringUntil('\n');
    Serial.println(data); // Muestra los datos recibidos

    // Analizar el mensaje CGNSINF
    if (data.startsWith("+CGNSINF:")) {
      parseCGNSINFData(data);
    }
  }

  // Espera y vuelve a enviar el comando CGNSINF
  delay(5000); // Espera 5 segundos antes de enviar el siguiente comando
  miSerial.println("AT+CGNSINF");
}

void parseCGNSINFData(String data) {
  // El mensaje CGNSINF tiene el formato:
  // +CGNSINF: <GNSS run status>,<Fix status>,<UTC date & Time>,<Latitude>,<Longitude>,<MSL Altitude>,<Speed Over Ground>,<Course Over Ground>,<Fix Mode>,<Reserved1>,<HDOP>,<PDOP>,<VDOP>,<Reserved2>,<GPS Satellites in View>,<GNSS Satellites Used>,<GLONASS Satellites Used>,<Reserved3>,<C/N0 max>,<HPA>,<VPA>

  // Dividir la cadena por comas
  int index1 = data.indexOf(','); // Primer coma
  int index2 = data.indexOf(',', index1 + 1); // Segunda coma
  int index3 = data.indexOf(',', index2 + 1); // Tercera coma
  int index4 = data.indexOf(',', index3 + 1); // Cuarta coma
  int index5 = data.indexOf(',', index4 + 1); // Quinta coma

  if (index3 != -1 && index4 != -1) {
    // Extraer latitud y longitud
    String lat = data.substring(index3 + 1, index4);
    String lon = data.substring(index4 + 1);

    // Convertir latitud y longitud a formato decimal
    float latitude = lat.toFloat();
    float longitude = lon.toFloat();

    // Enviar los datos en formato JSON
    Serial.print("{\"latitude\": ");
    Serial.print(latitude, 6); // Mostrar con precisión de 6 decimales
    Serial.print(", \"longitude\": ");
    Serial.print(longitude, 6); // Mostrar con precisión de 6 decimales
    Serial.println("}");
  } else {
    Serial.println("Error parsing CGNSINF data.");
  }
}


