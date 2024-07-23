'''
What commands to send to stepper motor driver is defined in .ino file.
Send 'p' to sending pulse.

'''
import serial

def connect_stepper(port_name):
    
    ser = serial.Serial(
        port = port_name, #Type in the com port
        baudrate = 9600
    )

    return ser   

def send_pulse(ser, steps):

    for i in range(steps):
        ser.write('p'.encode()) 