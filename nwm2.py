import math
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

licznik = 5

time.sleep(3)

poz = mc.player.getTilePos()

x = poz.x
y = poz.y
z = poz.z

typ = 2

mc.setBlocks(poz.x+6, poz.y-1, poz.z+6, poz.x-6, poz.y-1, poz.z-6, typ)
typ = 214
mc.setBlocks(poz.x+3, poz.y-1, poz.z+3, poz.x-3, poz.y-1, poz.z-3, typ)

mc.postToChat("Uwaga na czerwona strefe!")

time.sleep(5)

while licznik >= 1:
    mc.postToChat("WYBUCH ZA: " + str(licznik))
    licznik -= 1
    time.sleep(1)
    poz2 = mc.player.getTilePos()
    x = poz2.x
    y = poz2.y-1
    z = poz2.z
    typ = 214
    if (poz2.y == typ):
        poz3 = mc.player.getTilePos()
        x = poz3.x
        y = poz3.y-1
        z = poz3.z
        typ = 11
        mc.setBlock(poz3.x, poz3.y+1, poz3.z, typ)
    else:
        mc.postToChat("Udalo ci sie przezyc!")
