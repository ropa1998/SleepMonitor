#define LDRPIN A5
#define R1 220

void setup() {
  Serial.begin(9600);
}
void loop() {
  int LDR = analogRead(LDRPIN); // read the value from the sensor
  double Vout = (LDR * 0.0048828125);
  double RLDR = (R1 * (5 - Vout)) / Vout;
  double Lux = (500 / RLDR);
  Serial.println(Lux * 100); //prints the values coming from the sensor on the screen
  delay(100);
}
