""" This is in logging data from a Weighing Scale Machine """

import sys
import glob
import serial



def serial_ports():
    buffer1 = []
    result = []
    myfile = open("Latest.csv","a+")
    print("Pointer for File:\t",myfile.tell())
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    for port in ports:
        try:
            s = serial.Serial(port=port,\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS)
            result.append(port)
            print("-----------------------------")
            for x in range(9):
                ans=ascii(s.read())
                print("Data:\t",ans[2:3])
                myfile.write(ans[2:3])
            myfile.write("\n")
            print(buffer1)
            print("Pointer from FOR:\t",myfile.tell())
            print("-----------------------------")
            s.close()
            myfile.close()
        except (OSError, serial.SerialException):
            pass            #Is this even worth to write a pass here?
    return result


print(serial_ports())  #This will run the Actual Data





#for m in range(0,9):
#    ans=ascii(s.read())
#    buffer1.append(ans[2:3])
#myfile.write("\nThis is writing")
#myfile.write(str(buffer1))
