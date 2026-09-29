import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits  = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print("Напряжение чет многовато брат")
            print("установим наверн 0.0")
            return 0
        return int(self.voltage / dynamic_range * 255)
    def set_number(self,num):
        a = [int(el) for el in bin(self.num)[2:].zfill(8)]
        
        GPIO.output(led, a)
    def set_voltage(self, voltage):
        self.set_number(self.voltage_to_number(voltage))

led = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(led, GPIO.OUT)
dynamic_range = 3.3


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        while True:
            try:
                voltage = float(input("напряжения сне в пиво капни"))
                dac.set_voltage(voltage)

            except ValueError:
                print("ну ты ебень внатуре")
    finally:
        dac.deinit()