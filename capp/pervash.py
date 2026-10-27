import RPi.GPIO as GPIO
import time
class R2R_ADC:
    def __init__(self, dyn_range, comp_time = 0.01, verbose = False):
        self.dyn_range = dyn_range
        self.verbose = verbose
        self.comp_time = comp_time
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        self._cleaned = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def __del__(self):
        self.cleanup()
    def cleanup(self):
        if getattr(self, "_cleaned", True):
            return
        self.cleaned = True

        try:
            self.number_to_dac(0)
        except Exception:
            pass
    def number_to_dac(self,number):
        n = len(self.bits_gpio)
        max_number = (1 << n) - 1
        number = max(0, min(int(number), max_number))

        bits = [(number >> (n - 1 - i)) & 1 for i in range(n)]
        GPIO.output(self.bits_gpio, bits)
    def sequental_counting_adc(self):
        n = len(self.bits_gpio)
        max_number = (1 << n) - 1
        for number in range(max_number + 1):
            self.number_to_dac(number)
            time.sleep(self.comp_time)

            if GPIO.input(self.comp_gpio):
                if self.verbose:
                    print(f"ADC code = {number}")
                return number

        if self.verbose:        
            print(f"ADC code = {max_number}")
        return max_number

    def get_sc_voltage(self):
        code = self.sequental_counting_adc()
        max_number = (1 << len(self.bits_gpio)) - 1
        return code * self.dyn_range / max_number


if __name__ == "__main__":
    adc = None
    try:
        adc = R2R_ADC(dyn_range = 3.3)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f} В")
    
    except KeyboardInterrupt:
        pass
    finally:
        if adc is not None:
            adc.__del__()