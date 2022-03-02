import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)


GPIO.setup(leds, GPIO.OUT)

j = 0

while j < 3:
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)
    j = j + 1

GPIO.output(leds, 0)

GPIO.cleanup()