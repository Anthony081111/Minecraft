"""Hi person."""
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

print("Hello")
mc.postToChat("HI PEOPLE")
position = mc.player.getTilePos()

mc.postToChat(position)

x = position.x
y = position.y
z = position.z
a = z

while x < 300:
    x += 100
    z = a
    while z < 300:
        z += 100
        mc.player.setTilePos(x, y, z)
        time.sleep(0.5)
