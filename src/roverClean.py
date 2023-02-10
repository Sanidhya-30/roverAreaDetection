from .util import keyboard_shutdown
import time

def coverForwardArea(rover, spd):
    j=0
    while j<5:
        rover.moveForward(speed=spd)
        j = j+1
        time.sleep(1)

def coverBackwardArea(rover):
    j=0
    while j<5:
        rover.moveBackward(speed=2)
        j = j+1
        time.sleep(1)

def changeDirection(rover, angle):
    j=0
    while j<5:
        rover.changeYaw(angle=angle,speed=0.02)
        j = j+1
        time.sleep(1)

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
        coverBackwardArea(rover=rover)
        time.sleep(3)
        changeDirection(angle=0.2,rover=rover)
        coverForwardArea(rover=rover,spd=0.2)
        changeDirection(angle=-0.2,rover=rover)

        rover.workingStatus = False

    except KeyboardInterrupt:
        keyboard_shutdown()

def checkDistance(rover):
    while True:
        frontDist = rover.ul_front_edge.getDistance()
        backDist = rover.ul_back_edge.getDistance()
        print("Front Distance:", frontDist)
        print("Back Distance:", backDist)