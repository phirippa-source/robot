import Adafruit_SSD1306
from PIL import Image, ImageFont, ImageDraw

# Raspberry Pi pin configuration:
RST = 24

# 128 x 64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# 128 x 32 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize libarary
disp.begin()
# Get display width and height
width = disp.width
height = disp.height

# clear dispaly
disp.clear()
disp.display()

# Create image buffer
# Make susre to create image with '1' for 1-bit color
image = Image.new('1', (width, height))

# Create drawing object
draw = ImageDraw.Draw(image)

draw.text((0,0), 'Hello World!', fill=255)

disp.image(image)
disp.display()
