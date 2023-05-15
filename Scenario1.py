from FourRooms import FourRooms
import matplotlib.pyplot as plt
import numpy as np
from RLAgent import RLAgent

def main():
	# Environment
	env = FourRooms('simple')

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
		x, y = env.getPosition()
		state = 13*x+y
		done = False
		total_reward = 0
		while not done:
			action = agent.choose_action(state)
			gridType, newPos, packagesRemaining, isTerminal = env.takeAction(action)
			
			next_state = 13*newPos[0] + newPos[1]
			reward = 100 if gridType > 0 else 0
			done = isTerminal

			#next_state, reward, done, _ = env.step(action)

			agent.learn(state, action, reward, next_state, done)
			state = next_state
			total_reward += reward
		rewards[i] = total_reward

	# Plot Results
	#plt.plot(rewards)
	#plt.xlabel('Episode')
	#plt.ylabel('Reward')
	#plt.show()

	# Show Path
	#env.showPath(-1)

main()