import RPi.GPIO as GPIO

gas_boiler = 18 
pump_fireplace_cellar = 23
pump_fireplace_first_floor = 24
pump_fireplace_second_floor = 25
pump_first_floor = 7
pump_second_floor = 12
red_led = 16
orange_led = 20
blue_led = 21

GPIO.setmode(GPIO.BCM) 
#GPIO.setup(gas_boiler, GPIO.OUT)
#GPIO.setup(pump_fireplace_cellar, GPIO.OUT)
#GPIO.setup(pump_fireplace_first_floor, GPIO.OUT)
#GPIO.setup(pump_fireplace_second_floor, GPIO.OUT)
#GPIO.setup(pump_first_floor, GPIO.OUT) 
#GPIO.setup(pump_second_floor, GPIO.OUT) 
GPIO.setup(red_led, GPIO.OUT) 
GPIO.setup(orange_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)


#GPIO.output(gas_boiler, GPIO.LOW)
#GPIO.output(pump_fireplace_cellar, GPIO.LOW)
#GPIO.output(pump_fireplace_first_floor, GPIO.LOW)
#GPIO.output(pump_fireplace_second_floor, GPIO.LOW)
#GPIO.output(pump_first_floor, GPIO.LOW)
#GPIO.output(pump_second_floor, GPIO.LOW)
GPIO.output(red_led, GPIO.HIGH)
GPIO.output(orange_led, GPIO.HIGH)
GPIO.output(blue_led, GPIO.HIGH)
