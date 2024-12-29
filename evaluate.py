import gymnasium
import highway_env
import numpy as np
import torch
import random


# Set the seed and create the environment
np.random.seed(0)
random.seed(0)
torch.manual_seed(0)

env_name = "highway-v0"

env = gymnasium.make(env_name,
                     config={'action': {'type': 'DiscreteMetaAction'}, "lanes_count": 3, "ego_spacing": 1.5},
                     render_mode='human')

# Initialize your model and load parameters
agent = None
raise NotImplementedError

# Evaluation loop
state, _ = env.reset()
state = state.reshape(-1)
done, truncated = False, False

episode = 1
episode_steps = 0
episode_return = 0

while episode <= 10:
    episode_steps += 1
    # Select the action to be performed by the agent
    action = None
    raise NotImplementedError

    # Hint: take a look at the docs to see the difference between 'done' and 'truncated'
    state, reward, done, truncated, _ = env.step(action)
    state = state.reshape(-1)
    env.render()

    episode_return += reward

    if done or truncated:
        print(f"Episode Num: {episode} Episode T: {episode_steps} Return: {episode_return:.3f}, Crash: {done}")

        state, _ = env.reset()
        state = state.reshape(-1)
        episode += 1
        episode_steps = 0
        episode_return = 0

env.close()
