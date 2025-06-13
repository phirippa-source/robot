import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

pwm.set_pwm(0,0,110)
time.sleep(1)

while True:
  for duty in range(110, 551):     # duty : 100~560  110~550
    pwm.set_pwm(0,0,duty)
    time.sleep(0.02)
  for duty in range(550, 109, -1):
    pwm.set_pwm(0,0,duty)
    time.sleep(0.02)
