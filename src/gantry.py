# establish connection via com port to grbl platform
import serial
import numpy as np
import time

def connect_gantry(port_name):
    ser = serial.Serial (port_name,115200)
    return ser

# confirm if the target  move to specificed location
def wait_move(ser,target,tolerance,axis):
    targetX, targetY, targetZ = target[0], target[1], target[2]
    count_tmp = 0;
    while True:
        
        grbl_response = get_cur_pos(ser)
        grbl_response = output_decode(grbl_response)
        #print(grbl_response)
        if grbl_response.find('Idle') > 0:
            count_tmp+=1
        #print (findx(grbl_response))
            #time.sleep(0.01)
            diff = abs(findx(grbl_response,axis) - targetX)
        #print(diff)
            if (diff<1e-3):
                return 1
            if (count_tmp > 20):
                return 0

# extract x-coordinate from return message
def findx(output,axis):
    out = output
    out = out.split("|")[1]
    out = out.strip('MPos:')
    out = out.split(',')
    out = np.array(out, dtype=np.double).astype(float)
    return out[axis]

# send '?' to grbl controller to ask for current position
def get_cur_pos(ser):
    ser.reset_input_buffer()
    command_tmp = '?'
    command_send = str.encode(command_tmp + '\n')
    ser.write(command_send)
    return(ser.readline())

def output_decode(output):
    return output.strip().decode('utf-8')

def move(ser,position, axis):
    positionX = position[0]
    positionY = position[1]
    positionZ = position[2]
    
    if (axis == 0):
        command_tmp = "G0 X" + str(positionX)
    elif (axis == 1):
        command_tmp = "G0 Y" + str(positionY)
    elif (axis == 2):
        command_tmp = "G0 Z" + str(positionY)
    #print(command_tmp)
    command_send = str.encode(command_tmp + '\n')
    ser.write(command_send)
    #data = ser.readline()
    if(wait_move(ser,position,1e-3,axis) == 0):
        time.sleep(1)
        
    return 