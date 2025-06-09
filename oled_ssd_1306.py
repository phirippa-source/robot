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

while True:
  # Draw a black filled box to clear the image
  draw.rectangle((0,0,width, height), outline=0, fill=0)
  
  draw.text((5,0), 'Temp. of Raspberry Pi CPU', fill=255)
  temp = os.popen('vcgencmd measure_temp').readline()
  temp = temp.replace('temp=','').replace("'", "°")
  draw.text((5, 10), temp, fill=255)
  disp.image(image)
  disp.display()
