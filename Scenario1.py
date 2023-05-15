import matplotlib
import tkinter as tk
matplotlib.use('TkAgg')

import os
import shutil

import utils

from time import sleep



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

# I know i'm accessing a private member
# I'm not modifying it, i'm just getting the current space
env = rooms._FourRooms__environment.copy() # type: ignore[attr]

for i in range(15):

	os.system('clear')

	currX, currY = rooms._FourRooms__current_pos # type: ignore[attr]
	env[currY][currX] = 4

	
	act: int = agent1.get_next_move()

	gridType, newPos, packagesRemaining, isTerminal = agent1.move(act)

	currX, currY = rooms._FourRooms__current_pos # type: ignore[attr]
	env[currY][currX] = 5

	utils.print_colored_maze(env)

	print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[act], newPos, gTypes[gridType]))
	sleep(.4)
	if isTerminal:
		break
		

