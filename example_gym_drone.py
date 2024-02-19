import gym
# import gym_pybullet_drones

env = gym.make("ctrl-aviary-v0")  # Replace "drone-v0" with the actual environment ID
env.reset()

for _ in range(1000):
    env.render()
    action = env.action_space.sample()  # Take a random action
    observation, reward, done, info = env.step(action)
    if done:
        break

env.close()
