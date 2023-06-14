import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM) 
GPIO.setup(14, GPIO.IN) 
state_first_floor = GPIO.input(14)
        
GPIO.setup(15, GPIO.IN) 
state_second_floor = GPIO.input(15)

print("state_first_floor")
print(state_first_floor)
print("state_second_floor")
print(state_second_floor)
