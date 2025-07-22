from PIL import Image
Image.MAX_IMAGE_PIXELS = None

import os
# Your input image path (the full-resolution map)
source_image = r'Z:\webServer\RedMpolycreator\tiles\0\0_0.jpg'
tile_size = 256
max_zoom = 9  # 0 to 9 (10 levels)
output_dir = r'Z:\webServer\RedMpolycreator\tiles\splittolvl10zoom'

# Open source image
im = Image.open(source_image)
width, height = im.size

for z in range(0, max_zoom + 1):
    tiles = 2 ** z
    zoom_dim = tiles * tile_size

    # Resize with padding to a square if necessary
    zoom_img = im.resize((zoom_dim, zoom_dim), Image.LANCZOS)

    z_dir = os.path.join(output_dir, str(z))
    if not os.path.exists(z_dir):
        os.makedirs(z_dir)

    for x in range(tiles):
        for y in range(tiles):
            left = x * tile_size
            upper = y * tile_size
            right = left + tile_size
            lower = upper + tile_size

            tile = zoom_img.crop((left, upper, right, lower))
            tile_path = os.path.join(z_dir, f"{x}_{y}.jpg")
            tile.save(tile_path, "JPEG", quality=90)
    print(f"Zoom level {z} done ({tiles}x{tiles} tiles)")

print("All done!")
