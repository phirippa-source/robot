import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)  # 50Hz

for port in [0, 1, 2, 3]:
  pwm.set_pwm(port,0,330)
