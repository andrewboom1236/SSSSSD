import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
up = 9
down = 10
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds,0)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
num = 0
def f(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]
sleep_time = 0.2
while True:
    if GPIO.input(up):
        num += 1
        print(num, f(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        num -= 1
        print(num, f(num))
        time.sleep(sleep_time)
    if num < 0 or num > 50:
        break
    GPIO.output(leds, f(num))