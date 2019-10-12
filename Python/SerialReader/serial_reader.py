import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
s = [0, 1]
while True:
    read_serial = ser.readline().rstrip()
    print(str(read_serial))