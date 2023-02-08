from .util import keyboard_shutdown
import time

def cleanArea(rover, roverDataCollection,droneDataCollection,exit_event):
    try:
        #Check if cleaning should start
        print('check drone status')
        rover.workingStatus = True
        rover.setupAndArm()
        rover.changeVehicleMode('GUIDED')
        print('Cleaning Started')
        #currently without ultrasonic sensor

        j = 0
        while j < 2:
            i = 0
            while i < 5:
                i = i + 1
                time.sleep(1)
                rover.moveForward(0.5)
            i = 0
            while i < 5:
                i = i + 1
                time.sleep(1)
                rover.moveBackward(0.5)
            rover.changeYaw(0.8)
            rover.moveForward(0.2)
            rover.changeYaw(-0.8)
            j = j + 1

        rover.workingStatus = False

    except KeyboardInterrupt:
        keyboard_shutdown()
   