int buttonpin = 5; // define D0 Sensor Interface
double val = 0;// define numeric variables val

void setup ()
{
  Serial.begin(9600);
  pinMode (buttonpin, INPUT) ;// output interface D0 is defined sensor
}

void loop ()
{
  val = analogRead(buttonpin);// digital interface will be assigned a value of pin 5 to read val
  double dB = 20*log10(val);
  Serial.println(dB, DEC);

}
