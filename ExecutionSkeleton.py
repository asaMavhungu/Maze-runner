from FourRooms import FourRooms
import matplotlib
import tkinter as tk
matplotlib.use('TkAgg')

import os
import shutil



def clearImages():

    folder_path = "./images"

    # Remove all files and subdirectories in the folder
    shutil.rmtree(folder_path)

    # Recreate the folder
    os.mkdir(folder_path)

def checkImages():
    if not os.path.exists('images'):
        os.makedirs('images')
    else:
        clearImages()

def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')

    # This will try to draw a zero
    actSeq = [FourRooms.LEFT, FourRooms.LEFT, FourRooms.LEFT,
              FourRooms.UP, FourRooms.UP, FourRooms.UP,
              FourRooms.RIGHT, FourRooms.RIGHT, FourRooms.RIGHT,
              FourRooms.DOWN, FourRooms.DOWN, FourRooms.DOWN]

    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()))

    i = 0 
    for act in actSeq:

        i+= 1
        fourRoomsObj.showPath(-1, f"images/asa{i}.png")

        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(act)

        print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[act], newPos, gTypes[gridType]))

        if isTerminal:
            break

    # Don't forget to call newEpoch when you start a new simulation run

    # Show Path
    fourRoomsObj.showPath(-1)


if __name__ == "__main__":
    clearImages()
    main()
