import gymnasium
import highway_env


# Remember to save what you will need for the plots

env_name = "highway-v0"
env = gymnasium.make(env_name,
                     config={"manual_control": True, "lanes_count": 3, "ego_spacing": 1.5},
                     render_mode='human')

env.reset()
done, truncated = False, False

episode = 1
episode_steps = 0
episode_return = 0

while episode <= 10:
    episode_steps += 1

    # Hint: take a look at the docs to see the difference between 'done' and 'truncated'
    _, reward, done, truncated, _ = env.step(env.action_space.sample())  # With manual control these actions are ignored
    env.render()

    episode_return += reward

    if done or truncated:
        print(f"Episode Num: {episode} Episode T: {episode_steps} Return: {episode_return:.3f}, Crash: {done}")

        env.reset()
        episode += 1
        episode_steps = 0
        episode_return = 0

env.close()
