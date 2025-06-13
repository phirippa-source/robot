import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)  # 50Hz

try:
  for _ in range(3):
    pwm.set_pwm(0,0,300)
    pwm.set_pwm(1,0,120)    # min : about 100
    time.sleep(2)

    pwm.set_pwm(0,0,400)
    pwm.set_pwm(1,0,540)    # max : about 560
    time.sleep(2)
except KeyboardInterrupt:
  pwm.set_pwm(0,0,120)
  pwm.set_pwm(2,0,120)
