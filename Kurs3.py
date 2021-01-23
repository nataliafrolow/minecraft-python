from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
poz = mc.player.getTilePos()
typ = 41
x=poz.x
y=poz.y
z=poz.z
mc.setBlocks(x,y,z,x+2,y,z,block.WOOD.id)
