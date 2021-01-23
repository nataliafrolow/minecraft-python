from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pozycja = mc.player.getTilePos()  # {x, y, z}
x = pozycja.x+1
y = pozycja.y
z = pozycja.z
typ = 19
for i in range(0, 100):
    mc.setBlock(x+i, y, z, typ)
