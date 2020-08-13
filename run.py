import gym
import gym_raas
import numpy as np
import time
from os import system
import urllib.request

env = gym.make("raaspendulum-v0")
env.reset()
obs = []

print("\nBeginning ping test to google.com ...")
print(system("ping -c 1 www.google.com"))

print("\nBeginning google.com html download with urlopen ...")
try:
    response = urllib.request.urlopen("http://www.google.com/")
    html = response.read()
    print(html)
except:
    print("Download has failed using `urlopen`.")

print("\nBeginning file download with urlretrieve ...")
try:
    url = "http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg"
    cat = urllib.request.urlretrieve(url)
    print(cat[1])
except:
    print("Download has failed using `urlretrieve`.")

print("Job done.")
