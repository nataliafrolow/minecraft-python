from mcpi.minecraft import Minecraft


def buduj(blok):
    global krok
    global
    gracz = mc.player.getTilePos()
    x=player.x
    y=player.y
    z=player.z
    if blok == "1":
        print("buduj skale")
    elif blok == "0":
        print("buduj przestrzen")
    else:
        print("nie buduj")



mc = Minecraft.create()
zloto = mc.setBlock()
tlen = mc.setBlock()

plik = open("dane.txt","r")
linie = list(plik)

for linia in range(0,len(linie)):
    #print(linie[linia])
    for znak in linie[linia]:
        buduj(znak)
plik.close()
