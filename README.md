# Sleep Monitor
This is a simple project that uses Arduino and a Linux-based Single-Board computer to monitor ambient variables that influence your sleep quality. With this information the system can send alarms with insight about your sleeping ambient in order to improve it.
## Getting Started
This is a list of things you will need in order to use this code
 * An Arduino Board (Uno or Nano will do just fine)
    * A DHT11 sensor (Temperature and Humidity)
    * An LDR
    * A 220 Ohms resistor. You can change this but you would need to modify some Arduino source code.
    * Implementing this circuit
        ![Circuit](/home/rodrigo/projects/sleepmonitor/SleepMonitor/Images/Start Simulating.png) 
 *  A Linux-Based Single-Board Computer (We recommend a Raspberry Pi and Raspbian)
## Prequsites
First of all, you need to install the software in the Arduino. You can do this in any way you prefer (IDE or console).

The code that must be installed is `unifiend_sensors_sm.ino`. Remember to have the circuit configuration as shown before. Otherwise you will need to change the code.
 
After that you will need to connect via USB your Arduino to your SBC.
* First you must install SQLite3 in your computer. To do so run the following commands, that will install SQLite3 on your SBC.
    * `sudo apt-get install sqlite3`
    * `sudo apt-get install sqlitebrowser`
* Then you will need to run the requierement 
    
On that SBC you must start two Python scripts: `app.py` and `serial_reader.py`   
 
  