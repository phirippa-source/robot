# adafruit_pca9685 모듈 설치
# bullseye인 경우, $ pip install adafruit_pca9685

import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)  # 50Hz

for _ in range(3):
  pwm.set_pwm(0,0,300)
  time.sleep(1)
  pwm.set_pwm(0,0,400)
  time.sleept(1)
