import gym
import gym_raas
import numpy as np
import time
from os import system
import urllib.request

env = gym.make("raaspendulum-v0")
env.reset()
obs = []

print("\nBeginning ping test to google...")
print(system("ping -c 1 www.google.com"))

print("\nBeginning download with google html response wtih urlopen")
try:
    response = urllib.request.urlopen("http://www.google.com/")
    html = response.read()
    print(html)
except:
    print("Download has failed using `urlopen`. Moving on.")


print("\nBeginning file download with urlretrieve")
try:
    url = "http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg"
    cat = urllib.request.urlretrieve(url)
    print(cat[1])
except:
    print("Download has failed using `urlretrieve`. Moving on.")

print("Job done.")
