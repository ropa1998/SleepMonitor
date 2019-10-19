#include <DHT.h>
#define DHTPIN 2
#define LDRPIN A5
#define DHTTYPE DHT11
#define R1 220
#define dly 3000
#define MAX_ADC_READING 1023
#define ADC_REF_VOLTAGE 5
#define REF_RESISTANCE 220
#define LUX_CALC_SCALAR 12518931
#define LUX_CALC_EXPONENT -1.405

DHT dht(DHTPIN, DHTTYPE);



void setup() {
  Serial.begin(9600);
  dht.begin();

}

void loop() {
  delay(dly);
  Serial.print(getTemp() + "," + getHumd() +  "," + getLightREF());
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

String getLightREF() {
  double rawData = analogRead(LDRPIN);
  // MAX_ADC_READING is 1023 and ADC_REF_VOLTAGE is 5
  double resistorVoltage = (float)rawData / MAX_ADC_READING * ADC_REF_VOLTAGE;
  double ldrVoltage = ADC_REF_VOLTAGE - resistorVoltage;
  double ldrResistance = ldrVoltage / resistorVoltage * REF_RESISTANCE; // REF_RESISTANCE is 5 kohm
  double ldrLux = LUX_CALC_SCALAR * pow(ldrResistance, LUX_CALC_EXPONENT);
  // LUX_CALC_SCALAR and LUX_CALC_EXPONENT are determined by the Excel
  //spreadsheet
  // They are set to 12518931 and -1.405 respectively in my example
  return String(ldrLux/2);
}
