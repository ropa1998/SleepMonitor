

# Sleep Monitor {#mainpage}
This is a simple project that uses Arduino and a Linux-based Single-Board computer to monitor ambient variables that influence your sleep quality. With this information the system can send alarms with insight about your sleeping ambient in order to improve it.

## Table of Contents

- [Getting Started](#getting-started)
- [Prequisites](#prequsites)
- [Usage](#usage)
    - [Main page](#home-page)
    - [Reports](#reports)
    - [Configure](#configure)

## Getting Started
This is a list of things you will need in order to use this code
 * An Arduino Board (Uno or Nano will do just fine)
    * A DHT11 sensor (Temperature and Humidity)
    * An LDR
    * A 220 Ohms resistor. You can change this but you would need to modify some Arduino source code.
    * Implementing this circuit
    
        ![Circuit](https://raw.githubusercontent.com/ropa1998/SleepMonitor/master/Images/Start%20Simulating.png) 
 *  A Linux-Based Single-Board Computer (We recommend a Raspberry Pi and Raspbian)
## Prequsites
First of all, you need to install the software in the Arduino. You can do this in any way you prefer (IDE or console).

The code that must be installed is `unifiend_sensors_sm.ino`. Remember to have the circuit configuration as shown before. Otherwise you will need to change the code.
 
After that you will need to connect via USB your Arduino to your SBC.
* First you must install SQLite3 in your computer. To do so run the following commands, that will install SQLite3 on your SBC.
    * `sudo apt-get install sqlite3`
    * `sudo apt-get install sqlitebrowser`
* Then you will need to run the requirements.txt file. To do that remember to set a virtual enviorment for this app. Then, inside the venv just run `pip install --user --requirement requirements.txt`. This will leave all the required libraries for the project to work readily installed in your virtual environment.
* After that you must create yourself a [gmail account](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp) and [set it](https://myaccount.google.com/lesssecureapps) up to work for app SMTP.
    * Then you must configure your account in the `email_sender.py` module. For the `USERNAME` constant write the email of your newly created account. Now open the Python Console and configure [keyring](https://pypi.org/project/keyring/) to use it in the app.  
* After that you must run two different Python scripts in your SBC, in different consoles. Leave the second one running:
    * `create_database.py`
    * `serial_reader.py`
 
 That's it for the prequisites part! 
 
 ## Usage
 Now to the interesting part: how do you use this?
 
 First, we must pay attention to the IP direction and the port on which the app is running. This will route us to the project from any local network connected device.
 
 You must learn, by the tool of your choice (we recommend net-tools), your IP direction in your local network.
 
 After that you must run two commands (from the project venv): 
 
 `export FLASK_APP=hello.py`
 
 `flask run --host=0.0.0.0`
 
 This will allow you to use the project in your local network: you will need to access, from any local network connected device, the IP <SBC-IP>:5000, which will show you the project working.
 
 ### Home Page
 
 ![Sample home page](https://raw.githubusercontent.com/ropa1998/SleepMonitor/master/Images/sample_home_page.png)
 
 The first thing you can do is see the actual state of the environment. The colour of the value representing each value tells you how ideal is that value for sleeping
 * Green is ideal
 * Yellow is not so bad
 * Red is not a recommendable value
 
 ![Sample home page with graphs](https://raw.githubusercontent.com/ropa1998/SleepMonitor/master/Images/graphs_main_page.png)
 
 You can also see three tables that show you a history of all three variables. They get generated when you ask for the last N registers.     
 
 ### Reports
 
 You can also create your own reports based on dates from a time period you select.
 
 ![Sample report configuration page](https://raw.githubusercontent.com/ropa1998/SleepMonitor/master/Images/sample_report_config_page.png)

 After that, on another page, you will receive a report which you can later download if you wish so.
 
 ![Sample report](https://raw.githubusercontent.com/ropa1998/SleepMonitor/master/Images/sample_report_page.png)
 
 ### Configure
 
 In order to receive emails with your report after every sleep session you must register the sleeping ranges for every day and the email you want to have the email with the report sent.
 
 ![Sample config page](https://raw.githubusercontent.com/ropa1998/SleepMonitor/master/Images/sample_config_page.png)

Five minutes after your sleep session is over you will receive an email with the report

![Sample email page](https://raw.githubusercontent.com/ropa1998/SleepMonitor/master/Images/sample_email_image.jpeg)


## Contributors

This project exists thanks to all the people who contribute. 
* [Franz Soto Leal](https://github.com/FranzSL)
* [Rodrigo Pazos](https://github.com/ropa1998) 


## License

[MIT](LICENSE)
