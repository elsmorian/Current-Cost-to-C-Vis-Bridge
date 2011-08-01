import xml.parsers.expat
import serial
import datetime


MYCOMPORT = "/dev/tty.usbserial"
errorfile = open('error.log', 'a')


#get current month and day,

try:
    ser = serial.Serial(port=MYCOMPORT, timeout=5)
except serial.SerialException, msg:
    errorfile.write("Failed to connect to CurrentCost meter: " + str(msg))
    print("Failed to connect to CurrentCost meter: " + str(msg))
    exit(1)

while True:
    now = datetime.datetime.now()
    thisyear = now.year
    thismonth = now.month now.day
    
    outfile = open('S-m1-'+str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'.json', 'a')
    line = ser.readline()
    
    try:
        
        outfile.write(line)
        
    except serial.SerialException, err:
        errorfile.write("Failed to receive data from CurrentCost meter: " + str(err))
        print("Failed to receive data from CurrentCost meter: " + str(err))
        ser.close()
        exit(1)
    
    outfile.close()

ser.close()
exit(0)