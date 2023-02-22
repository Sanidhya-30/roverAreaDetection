from .util import keyboard_shutdown
import time
import math

length = 45
breadth = 30


def coverForwardArea(rover, d, spd):
    rover.moveForward(x=d,speed=spd)

def coverBackwardArea(rover, d, spd):
    rover.moveBackward(x=d,speed=spd)

def changeDirection(rover, angle):
    rover.changeYaw(angle=angle,speed=0.02)

def sweep(rover):
    
    try:
        while(rover.front_edge.checkDriveOk() == True):
            
            if (rover.back_edge.checkDriveOk() == True):
                changeLane()         

            else:
                coverBackwardArea(rover,spd=2)

        else:
            coverForwardArea(rover,spd=2)

    except KeyboardInterrupt:
        keyboard_shutdown()  

def changeLane(rover):
    
    H = math.sqrt(((length/2)**2)+(breadth**2))
    theta = math.atan((breadth)/(length/2))

    try:
        while(rover.back_edge.checkDriveOk() == True):
            
            coverForwardArea(rover,d=int((length/2)),spd=2)
            changeDirection(rover, theta)
            
            if (rover.front_edge.checkDriveOk() == True):
            # Lane End
                changeDirection(rover, -theta)
                coverBackwardArea(rover,d=int((length/2)),spd=2)
                #check drone status
                #call dock function()
                break

            else:
                coverForwardArea(rover,d=int((H)),spd=2)
                changeDirection(rover, (-theta))
                coverBackwardArea(rover,d=int((3*length)/2),spd=2)

    except KeyboardInterrupt:
        keyboard_shutdown()  

def cleanArea(rover):
    try:
        while (rover.back_edge.checkDriveOk() == False):
            
            print('check drone status')
            rover.workingStatus = True
            rover.setupAndArm()
            rover.changeVehicleMode('GUIDED')
            coverForwardArea(rover,d=int((length)),spd=2)
            #wait till drone takeoff
            coverBackwardArea(rover,spd=2)

            if (rover.back_edge.checkDriveOk() == True):
                changeDirection(rover, 90)
                break
            else:
                coverBackwardArea(rover,spd=2)

            print('starting Cleaning')
            sweep()

    except KeyboardInterrupt:
        keyboard_shutdown()

# def changeLane(rover,):