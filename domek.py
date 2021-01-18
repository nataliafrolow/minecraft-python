from mcpi.minecraft import Minecraft
mc = Minecraft.create()

poz = mc.player.getTilePos()

x = poz.x
y = poz.y
z = poz.z

typ = 5, 1
mc.setBlocks(x+4, y-1, z+3, x-4, y-1, z-3, typ)
typ = 251, 7
mc.setBlocks(x+4, y, z+3, x-4, y, z-3, typ)
typ = 0
mc.setBlocks(x+3, y, z+2, x-3, y, z-2, typ)
mc.setBlock(x+4, y, z, typ)
typ = 20
mc.setBlocks(x+4, y+1, z+3, x-4, y+1, z-3, typ)
typ = 0
mc.setBlocks(x+3, y+1, z+2, x-3, y+1, z-2, typ)
mc.setBlock(x+4, y+1, z, typ)
typ = 252, 8
mc.setBlocks(x+4, y+2, z+3, x-4, y+2, z-3, typ)
typ = 0
mc.setBlocks(x+3, y+2, z+2, x-3, y+2, z-2, typ)
mc.setBlock(x+4, y+2, z, typ)
typ = 251, 7
mc.setBlocks(x+4, y+3, z+3, x-4, y+3, z-3, typ)
typ = 0
mc.setBlocks(x+3, y+3, z+2, x-3, y+3, z-2, typ)
typ = 5, 1
mc.setBlocks(x+5, y+4, z+4, x-5, y+4, z-4, typ)
mc.setBlocks(x+4, y+5, z+3, x-4, y+5, z-3, typ)
mc.setBlocks(x+3, y+6, z+2, x-3, y+6, z-2, typ)
typ = 50
mc.setBlock(x, y, z, typ)
typ = 109
mc.setBlocks(x+3, y, z+2, x+3, y, z-2, typ)
typ = 0
mc.setBlock(x+3, y, z, typ)
typ = 58
mc.setBlock(x-3, y, z, typ)
typ = 61
mc.setBlock(x-3, y, z+1, typ)
typ = 116
mc.setBlock(x-3, y, z+2, typ)
typ = 54
mc.setBlock(x-3, y, z-1, typ)
typ = 130
mc.setBlock(x-3, y, z-2, typ)
