import os
from PIL import Image

# SETTINGS
TILE_SIZE = 256
IMAGE_WIDTH = 24576
IMAGE_HEIGHT = 19456
TILE_FOLDER = "tiles"  # set to your tiles root folder
TILE_EXT = ".jpg"      # use ".png" for PNG if you prefer

# Blank tile (white or transparent)
def create_blank_tile(path, ext=".jpg"):
    if ext == ".jpg":
        img = Image.new("RGB", (TILE_SIZE, TILE_SIZE), (255, 255, 255))  # white JPG
    else:
        img = Image.new("RGBA", (TILE_SIZE, TILE_SIZE), (0, 0, 0, 0))    # transparent PNG
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)

for z in range(0, 8):  # zoom levels 0 to 7
    tiles_x = int((IMAGE_WIDTH // TILE_SIZE) // (2 ** (7 - z))) + 1
    tiles_y = int((IMAGE_HEIGHT // TILE_SIZE) // (2 ** (7 - z))) + 1
    for x in range(tiles_x):
        for y in range(tiles_y):
            tile_path = os.path.join(TILE_FOLDER, str(z), f"{x}_{y}{TILE_EXT}")
            if not os.path.exists(tile_path):
                create_blank_tile(tile_path, TILE_EXT)
print("All missing blank tiles generated!")
