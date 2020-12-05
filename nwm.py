from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create
zloto = block.GOLD_BLOCK
przestrzen = block.AIR

global krok
global pietro

gracz = mc.player.getTilePos()
x = gracz.x
y = gracz.y
z = gracz.z


def buduj(blok):
    print("buduj skale")
    if(blok == "1"):
        print("buduj skale")
    elif(blok == "0"):
        print("buduj przestrzen")
    else:
        print("nic nie buduj")
