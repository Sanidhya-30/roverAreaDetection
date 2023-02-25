from .Rover import * 
from src.roverClean import cleanArea


def mainStart(serial=None, connection=None):
    if serial != None:
        print(serial)
        rover = Rover(roverSerial=serial,connection=connection)
        cleanArea(rover=rover)
        #checkDistance(rover=rover)




if __name__ == '__main__':
    pass
else:
    mainStart()