import gymnasium
import highway_env
import numpy as np
import torch
import random


# Set the seed and create the environment
np.random.seed(0)
random.seed(0)
torch.manual_seed(0)

MAX_STEPS = int(2e4)  # This should be enough to obtain nice results, however feel free to change it
env_name = "highway-fast-v0"  # We use the 'fast' env just for faster training, if you want you can use "highway-v0"

env = gymnasium.make(env_name,
                     config={'action': {'type': 'DiscreteMetaAction'}, 'duration': 40, "vehicles_count": 50})

# Initialize your model
agent = None
raise NotImplementedError

state, _ = env.reset()
state = state.reshape(-1)
done, truncated = False, False

episode = 1
episode_steps = 0
episode_return = 0

# Training loop
for t in range(MAX_STEPS):
    episode_steps += 1
    # Select the action to be performed by the agent
    action = None
    raise NotImplementedError

    # Hint: take a look at the docs to see the difference between 'done' and 'truncated'
    next_state, reward, done, truncated, _ = env.step(action)
    next_state = next_state.reshape(-1)

    # Store transition in memory and train your model
    raise NotImplementedError

    state = next_state
    episode_return += reward

    if done or truncated:
        print(f"Total T: {t} Episode Num: {episode} Episode T: {episode_steps} Return: {episode_return:.3f}")

        # Save training information and model parameters
        raise NotImplementedError

        state, _ = env.reset()
        state = state.reshape(-1)
        episode += 1
        episode_steps = 0
        episode_return = 0

env.close()
