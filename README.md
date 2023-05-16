# Maze-runner

# FourRooms Reinforcement Learning Example

This is an example of Reinforcement Learning implementation using the FourRooms environment. The environment is a grid world with 4 rooms. The agent can move in any of the four directions (up, down, left, right) but some of the directions may be blocked.

## Requirements

* Python 3.7 or later
* matplotlib
* numpy

## Usage

To run the code, run the following command:
`python Scenerio[i].py [-s | --stochastic]` where i ∈ {1,2,3}


The `-s` or `--stochastic` flag is optional and adds stochasticity to the action space.

## Description

The main script `main.py` implements the training of the RL agent and the visualization of the results. The script uses the `FourRooms` class to instantiate the environment and the `RLAgent` class to instantiate the agent.

The training consists of `num_episodes` episodes where the agent takes actions in the environment to maximize the cumulative reward. In each episode, the agent chooses an action based on its current state using the epsilon-greedy policy. The agent then updates its Q-table and moves to the next state.

At the end of each episode, the script prints the total reward and the path taken by the agent. The results are also plotted using matplotlib.

## Files

### FourRooms.py

This file contains the `FourRooms` class that implements the environment.

### RLAgent.py

This file contains the `RLAgent` class that implements the agent.

### utils.py

This file contains utility functions used by the main script.

### Scenerio1.py

This file contains a main script that runs the training and visualization using the `simple` configuration of the `FourRooms` class.

### Scenerio2.py

This file contains a main script that runs the training and visualization using the `multi` configuration of the `FourRooms` class.

### Scenerio3.py

This file contains a main script that runs the training and visualization using the `rgb` configuration of the `FourRooms` class.

