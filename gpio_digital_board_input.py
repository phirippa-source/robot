import time

GPIO.setmode(GPIO.BOARD)

pin = 24
GPIO.setup(pin, GPIO.IN)

try:
  while True:
    if GPIO.input(pin):
      print("SW On")
    else:
      print("SW Off")
    time.sleep(0.2)

except KeyboardInterrupt:
  GPIO.cleanup()
