import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 23
sw_pin = 24

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(sw_pin, GPIO.IN)

try:
  while True:
    if GPIO.input(sw_pin):
      GPIO.output(led_pin, GPIO.HIGH)
    else:
      GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.01)

except KeyboardInterrupt:
  GPIO.cleanup()
