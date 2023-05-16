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
	env = FourRooms('simple', args.stochastic)

	# Agent
	agent = RLAgent(num_states=13*13,
					num_actions=4,
					alpha=0.1,
					gamma=0.99,
					epsilon=0.1)

	# Training
	num_episodes = 1000
	rewards = np.zeros(num_episodes)
	for i in range(num_episodes):
		env.newEpoch()

		"""
		I know i'm accessing a private member
		I'm not modifying it, i'm just getting a shallow copy of current space
		I need this to print out to the terminal at the end of each episode
		to get an idea of how my agent is training
		I would've added a getter in FourRooms that returns this copy but that was
		not allowed in the brief
		"""
		cpy = env._FourRooms__environment.copy() # type: ignore[attr]


		x, y = env.getPosition()
		# Use the coordinates of the position to define a state
		state = 13*x+y
		done = False
		total_reward = 0
		
		currX, currY = env.getPosition()
		# Update my copy of the space
		cpy[currY][currX] = 5

		origin = env.getPosition()

		# Save the state transitions for the episode
		actPosGrid = []

		while not done:
			action = agent.choose_action(state)

			currX, currY = env.getPosition()

			val = cpy[currY][currX]
			# Only over-write white spaces in the environment copy
			if val == 0:
				cpy[currY][currX] = 4
	
			gridType, newPos, packagesRemaining, isTerminal = env.takeAction(action)
			
			# Update the state
			next_state = 13*newPos[0] + newPos[1]
			if gridType > 0:
				reward = 100 # Reward getting to the end
			else:
				reward = -1 # Punish each step taken to encourage taking shortest path

			done = isTerminal

			# Update the tables
			agent.learn(state, action, reward, next_state, done)
			state = next_state
			total_reward += reward

			actPosGrid.append((action, newPos, gridType))

		rewards[i] = total_reward
		os.system('clear')
		utils.print_colored_maze(cpy)
		print(f"Episode: {i}")
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