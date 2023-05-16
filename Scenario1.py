from FourRooms import FourRooms
import matplotlib.pyplot as plt
import numpy as np
from RLAgent import RLAgent
import utils
from time import sleep
import os
import argparse

def main(args):
	
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
		cpy = env._FourRooms__environment.copy() # type: ignore[attr]
		x, y = env.getPosition()
		state = 13*x+y
		done = False
		total_reward = 0
		
		currX, currY = env._FourRooms__current_pos # type: ignore[attr]
		cpy[currY][currX] = 5

		while not done:
			action = agent.choose_action(state)

			currX, currY = env._FourRooms__current_pos # type: ignore[attr]

			val = cpy[currY][currX]
			if val == 0:
				cpy[currY][currX] = 4
	
			gridType, newPos, packagesRemaining, isTerminal = env.takeAction(action)

			next_state = 13*newPos[0] + newPos[1]
			if gridType > 0:
				reward = 10*gridType
			else:
				reward = 0

			done = isTerminal

			agent.learn(state, action, reward, next_state, done)
			state = next_state
			total_reward += reward
		rewards[i] = total_reward
		os.system('clear')
		utils.print_colored_maze(cpy)
		print(f"Episode: {i}")
		print(f"Total reward:{total_reward}")
		sleep(.05)

	# Show Path
	env.showPath(-1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--stochastic', action='store_true', help='Add stochasticity to action space')
    args = parser.parse_args()
    main(args)
    print(args.stochastic)