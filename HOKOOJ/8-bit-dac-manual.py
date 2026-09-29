import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(led, GPIO.OUT)
dynamic_range = 3.3
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение чет многовато брат")
        print("установим наверн 0.0В")
        return 0
    return int(voltage / dynamic_range * 255)

def number_todac(num):
    a = [int(el) for el in bin(num)[2:].zfill(8)]
    GPIO.output(led, a)

try:
    while True:
        try:
            voltage = float(input("напряжение брат: "))
            number = voltage_to_number(voltage)
            number_todac(number)
        except ValueError:
            print("ты тупой сука")
finally:
    number_todac(0)
    GPIO.cleanup()