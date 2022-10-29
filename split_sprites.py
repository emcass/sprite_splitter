#################################
# Written by Alex Wayne 07/27/22
#################################

from PIL import Image
import os

# CHANGE WITH YOUR FILENAME
filename = "tilemap.png"

# change 4 if your extension length is different
extension = filename[-4:]

# SET THE DIMENSIONS OF YOUR DESIRED SPRITES
tile_width = 16
tile_height = 16

original = Image.open(filename)
width, height = original.size

num_sprites = 1

for y in range(int(height / tile_height)):
    for x in range(int(width / tile_width)):
        x = int(x)

        # Save the cropped image to the sprites folder
        # Named the original filename without the extension + the index
        if not os.path.exists("sprites/"):
            os.makedirs("sprites")
        right = (x + 1) * tile_width
        bottom = (y + 1) * tile_height
        left = right - tile_width
        top = bottom - tile_height
        sprite = original.copy().crop((left, top, right, bottom))
        sprite.save(f"sprites/{filename[0:-len(extension)]}{num_sprites}{extension}", f"{extension[1:].upper()}")
        num_sprites += 1
