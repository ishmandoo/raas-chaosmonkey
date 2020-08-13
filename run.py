import gym
import gym_raas
import numpy as np
import time


env = gym.make('raaspendulum-v0')
env.reset()
obs = []
import urllib.request

print('Beginning file download with urllib2...')

url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
cat = urllib.request.urlretrieve(url)
print(cat[1])