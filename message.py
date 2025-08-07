import random
#@aniceday__1
import pyautogui as pg
import time
pet=['parrot','dog','cat','rabbit']
time.sleep(8)
for i in range(5000):
    a=random.choice(pet)
    pg.write("You are a "+ a)
    pg.press('enter')