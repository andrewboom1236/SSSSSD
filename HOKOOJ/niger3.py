import RPi.GPIO as GPIO
class RWM_DAC:
    def __init__(self, gpio_bits, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_bits  = gpio_bits
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Напряжение чет многовато брат")
            print("установим наверн 0.0")
            return 0
        return int(voltage / self.dynamic_range * 255)
    def set_number(self, num):
        a = [int(el) for el in bin(num)[2:].zfill(8)]
        
        GPIO.output(self.gpio_bits, a)
    def set_voltage(self, voltage):
        self.set_number(self.voltage_to_number(voltage))
if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("кентишка мой солнце дай напряга "))
                dac.set_voltage(voltage)
            except ValueError:
                print("тупой ты сука уебок")
    finally:
        dac.deinit()