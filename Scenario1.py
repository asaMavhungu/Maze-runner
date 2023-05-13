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
        
checkImages()


from RLAgent import RLAgent
from FourRooms import FourRooms

agent1: RLAgent = RLAgent()

rooms: FourRooms = FourRooms('simple')

agent1.set_room(rooms)

aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

print('Agent starts at: {0}'.format(rooms.getPosition()))

for i in range(15):
	rooms.showPath(-1, f"images/asa{i}.png")

	act: int = agent1.get_next_move()

	gridType, newPos, packagesRemaining, isTerminal = agent1.move(act)

	print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[act], newPos, gTypes[gridType]))

	if isTerminal:
		break
        

