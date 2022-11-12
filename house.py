"""This will help us build a house."""
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()


def build_floor(block_id, x, y, z, x_offset, z_offset):
    mc.setBlocks(x, y, z, x + x_offset, y, z + z_offset, block_id)


def build_wall(block_id2, x, y, z, x_offset, y_offset, z_offset):
    mc.setBlocks(x, y, z, x + x_offset, y + y_offset, z + z_offset, block_id2)


position = mc.player.getTilePos()
mc.postToChat(position)
# coordinates: -5013, -8, 6109
x = -5013
y = -8
z = 6109
mc.player.setTilePos(x, y, z)
a = x + 10
b = z - 10
c = x - 10
d = z + 10
print(a, b)
build_floor(4, a, y, b, -20, 30)
build_wall(45, a, y, b, -20, 3, 0)
build_wall(45, a, y, b, -20, 3, 0)
build_wall(45, a, y, b, -20, 3, 0)
build_wall(45, a, y, b, -20, 3, 0)
# build_wall(0, a, y, b, -20, 3, 0)                 # Use this to clear a mistake
