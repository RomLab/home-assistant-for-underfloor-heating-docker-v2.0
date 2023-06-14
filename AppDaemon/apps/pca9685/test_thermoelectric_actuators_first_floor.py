import pca9685
import time
#import i2c_lcd_driver
#PCA9685_ADDRESS_SECOND_FLOOR = 0x40
#PCA9685_ADDRESS_FIRST_FLOOR = 0x41
#pca9685.software_reset()
ADRESS = 0x40
pwm = pca9685.PCA9685(ADRESS)

channel = None

#pwm_pulse = 0
pwm_pulse = 4095

channel = 0          
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)
channel = 1
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)
channel = 2
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)  
channel = 3
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)     
channel = 4
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)
channel = 5
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)      
channel = 6
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)      
channel = 7
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)
channel = 8
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)
channel = 9
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)
channel = 10
pwm.set_pwm(channel, 0, pwm_pulse)
time.sleep(2)     
channel = 11
pwm.set_pwm(channel, 0, pwm_pulse)
