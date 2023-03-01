from .util import keyboard_shutdown
import time
import math

length = 45
breadth = 30

#True = edge detected

def moveF(rover, spd):
    rover.moveForward(speed=spd)

def moveB(rover, spd):
    rover.moveBackward(speed=spd)

def moveF_L(rover, spd, d):
    rover.moveForward_L(speed=spd,d=d)

def moveB_L(rover, spd, d):
    rover.moveBackward_L(speed=spd,d=d)

def changeDirection(rover, angle):
    rover.changeYaw(angle=angle,speed=0.02)


def changeLane(rover):
    
    print("Changing Lane")
    time.sleep(1)
    H = math.sqrt(((length/2)**2)+(breadth**2))
    theta = math.atan((breadth)/(length/2))

    try:
        while(True):
            
            moveF_L(rover,spd=2, d=int((length/2)))
            print("moving forward2")
            time.sleep(1)
            changeDirection(rover, theta)
            print("changing direction")
            time.sleep(1)
    
            # Lane End
            if (rover.ul_front_edge.checkDriveOk() == True):
                print("Lane End")
                changeDirection(rover, -theta)
                print("changing direction !Lane end")
                moveB_L(rover,spd=2, d=int((length/2)))
                print("moving back4")
                print("docking called")
                dock(rover=rover)
            
            else:
                moveF_L(rover,spd=2, d=int((H)))
                print("moving forward2")
                changeDirection(rover, (-theta))
                moveB_L(rover,spd=2, d=int((3*length)/2))
                print("moving back3")
                break

    except KeyboardInterrupt:
        keyboard_shutdown()


def sweep(rover):
    print("Sweeeping")
    time.sleep(1)
    try:
        while(rover.ul_front_edge.checkDriveOk() == False):
            
            moveF(rover=rover,spd=2)
            print("moving forward1")
            time.sleep(1)

        while (rover.ul_back_edge.checkDriveOk() == False):
            moveB(rover=rover,spd=2)
            print("moving back3")
            time.sleep(1)
            
        changeLane(rover=rover)
        sweep(rover=rover)

    except KeyboardInterrupt:
        keyboard_shutdown()  
  

def cleanArea(rover):
    
    print('check drone status')
    rover.workingStatus = True
    rover.setupAndArm()
    rover.changeVehicleMode('GUIDED')
    time.sleep(2)
    
    try:
        moveF_L(rover,spd=2, d=int((length)))
        print("Undocking")
        #wait(5)
        #wait till drone takeoff
        while(True):
            moveB(rover,spd=2)
            print("moving back1")
            time.sleep(1)

            if (rover.ul_back_edge.checkDriveOk() == True):
                changeDirection(rover, 90)
                print("Orienting to corner")
                time.sleep(1)

            moveB(rover,spd=2)
            print("moving back1")
            if (rover.ul_back_edge.checkDriveOk() == True):
                print("Corner Detected")
                print("Sweep function called")
                sweep(rover=rover)
                break
    
    except KeyboardInterrupt:
        keyboard_shutdown()

def dock(rover):
    print("Docking")