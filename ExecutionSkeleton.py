from FourRooms import FourRooms
import matplotlib
import utils
import tkinter as tk
matplotlib.use('TkAgg')

import os

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

    # I know i'm accessing a private member
    # I'm not modifying it, i'm just getting the current space
    env = fourRoomsObj._FourRooms__environment.copy() # type: ignore[attr]

    from time import sleep

    i = 0 
    for act in actSeq:
        os.system('clear')

        i+= 1

        currX, currY = fourRoomsObj._FourRooms__current_pos # type: ignore[attr]
        env[currY][currX] = 4

        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(act)

        currX, currY = fourRoomsObj._FourRooms__current_pos # type: ignore[attr]
        env[currY][currX] = 5

        utils.print_colored_maze(env)

        print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[act], newPos, gTypes[gridType]))

        if isTerminal:
            break

        sleep(.4)

    # Don't forget to call newEpoch when you start a new simulation run

    # Show Path
    #fourRoomsObj.showPath(-1)


if __name__ == "__main__":
    main()