from mcpi.minecraft import Minecraft
typ = 23
mc = Minecraft.create()
poz = mc.player.getTilePos()
mc.postToChat(poz)
mc.setBlock(poz.x,poz.y,poz.z,typ)
