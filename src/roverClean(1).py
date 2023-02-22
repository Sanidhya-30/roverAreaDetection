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
    print()


def changeLane(rover):
    H = math.sqrt((length**2)+(breadth**2))
    coverForwardArea(rover,d=int((length/2)),spd=2)
    changeDirection(rover, theta)
    coverForwardArea(rover,d=int((H)),spd=2)
    changeDirection(rover, (-theta))
    coverBackwardArea(rover,d=int((3*length)/2),spd=2)

# def changeLane(rover,):