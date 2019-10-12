#include <DHT.h>
#define DHTPIN 2
#define LDRPIN A5
#define DHTTYPE DHT11
#define R1 220
#define dly 3000

DHT dht(DHTPIN, DHTTYPE);



void setup() {
  Serial.begin(9600);
  dht.begin();

}

void loop() {
 delay(dly);
 Serial.print(getTemp());
 Serial.print(getLight());
 Serial.print("\n");
}

String getTemp(){
   //Temperatura y humedad
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  return "Humidity: " + String(h) +"\n" + "Temperature in C: " + String(t) + "\n"; 
  //Termina temperatura y humedad
}

String getLight(){
  int LDR = analogRead(LDRPIN); // read the value from the sensor
  double Vout = (LDR * 0.0048828125);
  double RLDR = (R1 * (5 - Vout)) / Vout;
  double Lux = (500 / RLDR);
  return "Light: " + String(Lux*100);
}
