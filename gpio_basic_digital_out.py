import RPi.GPIO as GPIO
import time

pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

try:
  while True:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
