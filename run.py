import gym
import gym_raas
import numpy as np
import time

env = gym.make('raaspendulum-v0')
env.reset()
obs = []

from os import system
system("ping -c 1 www.google.com")

import urllib.request

print('\nBeginning download with google html response wtih urlopen...')
response = urllib.request.urlopen('http://www.google.com/')
html = response.read()
print(html)

print('\nBeginning file download with urlretrieve...')
url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
cat = urllib.request.urlretrieve(url)
print(cat[1])
