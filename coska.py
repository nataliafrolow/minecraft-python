from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pozycja = mc.player.getTilePos()  # {x, y, z}
x = pozycja.x+1
y = pozycja.y
z = pozycja.z
typ = 46
mc.setBlocks(x, y, z, x+121212, y+56765, z+13412, typ)
