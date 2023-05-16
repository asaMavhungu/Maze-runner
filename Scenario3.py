from FourRooms import FourRooms
import matplotlib.pyplot as plt
import numpy as np
from RLAgent import RLAgent
import utils
from time import sleep
import os
import argparse


def main(args):

	aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
	gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

	# Environment
	env = FourRooms('rgb', args.stochastic)

	# Agent
	agent = RLAgent(num_states=13*13*8,
					num_actions=4,
					alpha=0.1,
					gamma=0.99,
					epsilon=0.05)

	# Training
	num_episodes = 1000
	rewards = np.zeros(num_episodes)
	for i in range(num_episodes):
		env.newEpoch()
		cpy = env._FourRooms__environment.copy() # type: ignore[attr]
		x, y = env.getPosition()
		state = (13*x+y)
		done = False
		total_reward = 0
		
		currX, currY = env.getPosition()
		cpy[currY][currX] = 5

		packages = []
		binary2 = [0,0,0]
		next_package = 1

		origin = env.getPosition()

		actPosGrid = []

		while not done:
			action = agent.choose_action(state)

			currX, currY = env.getPosition()

			val = cpy[currY][currX]
			if val == 0:
				cpy[currY][currX] = 4
	
			gridType, newPos, packagesRemaining, isTerminal = env.takeAction(action)

			
			reward = 0
			next_state = (13*newPos[0] + newPos[1])
			if gridType > 0 and gridType not in packages:
				if gridType == next_package:
					packages.append(gridType)
					next_package += 1
					reward = 100*(4-len(packages))
					binary2[gridType-1] = 1
				else:
					# If current package is not the next one in sequence, send the agent back to origin
					reward = -100
					break

			
			offset = binary2[0]* 2**2 + binary2[1]* 2**1 + binary2[2]* 2**0
			
			next_state = offset*(13*13) + (13*newPos[0] + newPos[1])

			done = isTerminal

			agent.learn(state, action, reward, next_state, done)
			state = next_state
			total_reward += reward


			actPosGrid.append((action, newPos, gridType))

		rewards[i] = total_reward
		os.system('clear')
		utils.print_colored_maze(cpy)
		print(f"Episode: {i}")
		print(f"Packs: {packages}")
		print(f"Total reward:{total_reward}")

		print('Agent starts at: {0}'.format(origin))

		for ten in actPosGrid:
			print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[ten[0]], ten[1], gTypes[ten[2]]))
		sleep(.05)

	# Plot Results
	plt.plot(rewards)
	plt.xlabel('Episode')
	plt.ylabel('Reward')
	plt.show()

	# Show Path
	env.showPath(-1)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--stochastic', action='store_true', help='Add stochasticity to action space')
	args = parser.parse_args()
	main(args)
	print(args.stochastic)