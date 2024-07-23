'''
import rotary and gantry module
can either send command to gantry for x,y,z-axis movement or to rotary for rotation movement

'''
import serial
import numpy as np
import time
import gantry
import rotary

def xyzr(mode, steps, positions, gantry_ser, rotary_ser):
    if (mode == "rotate"):
        rotary.send_pulse(rotary_ser,steps)
        print("rotate to ",steps," steps")
        
    elif (mode == "linear"):
        
        gantry.move(gantry_ser,positions,0)
        print("move to ",positions[0])


def main():
    gantry_port = 'COM7'
    rotary_port = 'COM6'

    # establish the communication port for rotary and gantry
    rotary_ser = rotary.connect_stepper(rotary_port)
    gantry_ser = gantry.connect_gantry(gantry_port)

    # add the positions or steps for example
    xyzr("linear", 0, np.array([15,0,0]), gantry_ser, rotary_ser)
    xyzr("rotate", 1000, 0, gantry_ser, rotary_ser)
    xyzr("linear", 0, np.array([10,0,0]), gantry_ser, rotary_ser)
    xyzr("rotate", 1000, 0, gantry_ser, rotary_ser)

    print("Finished !!")
    rotary_ser.close()
    gantry_ser.close()

if __name__ == "__main__":
    main()
