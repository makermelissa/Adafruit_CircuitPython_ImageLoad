import board
import displayio
import adafruit_imageload

image, palette = adafruit_imageload.load(
    "images/4bit.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette
)
tile_grid = displayio.TileGrid(image, pixel_shader=palette)

group = displayio.Group()
group.append(tile_grid)
board.DISPLAY.show(group)

while True:
    pass
