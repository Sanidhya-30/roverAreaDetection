from .Rover import *    

def clean(rover):
    print('Cleaning...')


def mainStart(serial=None, connection=None):
    if serial != None:
        print(serial)
        rover = Rover(roverSerial=serial,connection=connection)
        clean(rover=rover)



if __name__ == '__main__':
    pass
else:
    mainStart()