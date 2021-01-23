from mcpi.minecraft import Minecraft
from random import randint
import time
mc = Minecraft.create()
poz = mc.player.getTilePos()
for miejsce in range(5):
    mc.postToChat(miejsce)
    
    zmienna_losowa_X = randint(0,300)
    zmienna_losowa_Y = randint(0,300)
    zmienna_losowa_Z = randint(0,300)

    mc.postToChat(zmienna_losowa_X)
    mc.postToChat(zmienna_losowa_Y)
    mc.postToChat(zmienna_losowa_Z)

    mc.player.setPos(zmienna_losowa_X,zmienna_losowa_Y,zmienna_losowa_Z)

    time.sleep(3)