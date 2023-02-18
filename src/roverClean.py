from .util import keyboard_shutdown
import time

def coverForwardArea(rover, spd):
    rover.moveForward(speed=spd)

def coverBackwardArea(rover, spd):
    rover.moveBackward(speed=spd)

def changeDirection(rover, angle):
    rover.changeYaw(angle=angle,speed=0.02)

def cleanArea(rover):
    try:

        #Check if cleaning should start

        print('check drone status')
        rover.workingStatus = True
        rover.setupAndArm()
        rover.changeVehicleMode('GUIDED')
        print('Cleaning Started')

        # frontDist = rover.ul_front_edge.getDistance()
        # backDist = rover.ul_back_edge.getDistance()
        #currently without ultrasonic sensor
        coverForwardArea(rover=rover,spd=2)
        coverBackwardArea(rover=rover, spd=2)
        time.sleep(3)
        changeDirection(angle=0.2,rover=rover)
        coverForwardArea(rover=rover,spd=0.2)
        changeDirection(angle=-0.2,rover=rover)

        rover.workingStatus = False

    except KeyboardInterrupt:
        keyboard_shutdown()

def checkDistance(rover):
    print('started')
    while True:
        front = rover.ul_front_edge.checkDriveOk()
        back = rover.ul_back_edge.checkDriveOk()
        frontDist = rover.ul_front_edge.getDistance()
        backDist = rover.ul_back_edge.getDistance()
        
        if front:
            print("Drive")
            print("Front Distance:", frontDist)
        else:
            print("Dont Drive Forward, Edge Reached")
        
        print("------------------------------------")
        if back:
            print("Drive")
            print("Back Distance:", backDist)
        else:
            print("Dont Drive Backward, Edge Reached")
        
        print("************************************************************************************")
        time.sleep(1)

def changeLane(rover):
    print('Lane change')
    changeDirection(angle=0.2,rover=rover)
    coverForwardArea(rover=rover,spd=0.2)
    changeDirection(angle=-0.2,rover=rover)
        
def cleanPanels(rover):
    try:

        #Check if cleaning should start
        while True:
            front = rover.ul_front_edge.checkDriveOk()
            back = rover.ul_back_edge.checkDriveOk()
            
            if front:
                print('Forward')
                coverForwardArea(rover=rover,spd=2)
            elif (not front) and back:
                rover.ul_front_edge.areaCompleted = True
                coverBackwardArea(rover=rover, spd=2)
            elif (rover.ul_front_edge.areaCompleted) and (not back):
                rover.ul_back_edge.areaCompleted = True
                changeLane(rover=rover)

    except KeyboardInterrupt:
        keyboard_shutdown()