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
  Serial.print(getTemp() + "," + getHumd() +  "," + getLight());
  Serial.print("\n");
}

String getTemp() {

  float t = dht.readTemperature();
  return String(t);
  
}

String getHumd() {

  float h = dht.readHumidity();
  return String(h);
  
}

String getLight() {
  int LDR = analogRead(LDRPIN); // read the value from the sensor
  double Vout = (LDR * 0.0048828125);
  double RLDR = (R1 * (5 - Vout)) / Vout;
  double Lux = (500 / RLDR);
  return String(Lux * 100);
}
