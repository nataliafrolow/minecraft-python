from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time
import math

poz = mc.player.getTilePos()

x1 = poz.x+1
y1 = poz.y
z1 = poz.z

typ = 34

mc.setBlock(x1,y1,z1,typ)

while True:
    poz = mc.player.getTilePos()
    x2 = poz.x
    z2 = poz.z
    x = x1 - x2
    z = z1 - z2
    c = math.sqrt(x * x + z * z)
    if (c < 3):
        mc.postToChat("jestes blisko bloku: " + str(math.floor(c)) + " jednostek")
    else:
        mc.postToChat("jestes daleko bloku: " + str(math.floor(c)) + " jednostek")
        
    time.sleep(1)
