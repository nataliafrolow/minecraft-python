import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


time.sleep(3)

pozycja = mc.player.getTilePos()

x = pozycja.x + 2
y = pozycja.y
z = pozycja.z

typ = 11

mc.setBlocks(x, y, z, x-4, y-150, z-4, typ)

mc.postToChat("SKACZ!?!")

typ = 0

time.sleep(3)

mc.setBlocks(x-1, y, z-1, x-3, y-150, z-3, typ)
