import numpy as np
import RPi.GPIO as GPIO
import time

motor_pins = [31, 33, 35, 37]
GPIO.setmode(GPIO.BOARD);
for i in motor_pins:
	GPIO.setup(i, GPIO.OUT)

n = 180;	
one_rev = 2048
turns = int(n * 2048 / 360)
pin = 0

for i in motor_pins:
	GPIO.output(i, GPIO.LOW)

for i in range(turns):
	pin = i % 4
	GPIO.output(motor_pins[(i+3) % 4], GPIO.LOW)
	GPIO.output(motor_pins[(i+1) % 4], GPIO.HIGH)
	time.sleep(0.01)

for i in motor_pins:
	GPIO.output(i, GPIO.LOW)
GPIO.cleanup();

