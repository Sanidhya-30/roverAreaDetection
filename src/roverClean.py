from .util import keyboard_shutdown
import time
import math

length = 45
breadth = 30

#True = edge detected 

def coverForwardArea(rover, spd):
    rover.moveF(speed=spd)

def coverBackwardArea(rover, spd):
    rover.moveB(speed=spd)

def MoveForward(rover, spd, d):
    rover.moveF_L(speed=spd,d=d)

def MoveBackward(rover, spd, d):
    rover.moveB_L(speed=spd,d=d)

def changeDirection(rover, angle):
    rover.changeYaw(angle=angle,speed=0.02)

def sweep(rover):
    
    try:
        while(rover.ul_front_edge.checkDriveOk() == True):
                        
            if (rover.ul_back_edge.checkDriveOk() == True):
                changeLane()
                print("Changing Lane")

            else:
                coverBackwardArea(rover,spd=2)
                print("Moving Back")

        else:
            coverForwardArea(rover,spd=2)
            print("Moving Fwd")

    except KeyboardInterrupt:
        keyboard_shutdown()  

def changeLane(rover):
    
    H = math.sqrt(((length/2)**2)+(breadth**2))
    theta = math.atan((breadth)/(length/2))

    try:
        while(rover.ul_back_edge.checkDriveOk() == True):
            
            MoveForward(rover,spd=2, d=int((length/2)))
            changeDirection(rover, theta)
    
            if (rover.ul_front_edge.checkDriveOk() == True):
            # Lane End
                print("Lane End")
                changeDirection(rover, -theta)
                MoveBackward(rover,spd=2, d=int((length/2)))
                #check drone status
                #call dock function()
                break

            else:
                MoveForward(rover,spd=2, d=int((H)))
                changeDirection(rover, (-theta))
                MoveBackward(rover,spd=2, d=int((3*length)/2))

    except KeyboardInterrupt:
        keyboard_shutdown()  

def cleanArea(rover):
  #  try:
        while (rover.ul_back_edge.checkDriveOk() == False):

            print('check drone status')
            rover.workingStatus = True
            rover.setupAndArm()
            rover.changeVehicleMode('GUIDED')
            MoveForward(rover,spd=2, d=int((length)))
            print("Undocking")
            #wait till drone takeoff
            coverBackwardArea(rover,spd=2)

            if (rover.back_edge.checkDriveOk() == True):
                changeDirection(rover, 90)
                print("Orienting to corner")
                
                if (rover.back_edge.checkDriveOk() == True):
                    print("Starting sweep")
                    sweep()
            
                else:
                    coverBackwardArea(rover,spd=2)
                    print("Going to Top-Right corner")  
            
            else:
                coverBackwardArea(rover,spd=2)
                print("Going to Top edge")
                

   # except KeyboardInterrupt:
    #    keyboard_shutdown()