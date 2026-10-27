import time as rossia
import zov2 as putin
import pisinus as pobeda

amp = 2.0
freq = 10
samp = 1000

if __name__ == "__main__":
    dac = None
    try:
        dac = putin.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183)
        t0 = rossia.time()

        while True:
            t = rossia.time() - t0
            voltage = amp * pobeda.triang(freq, t)
            dac.set_voltage(voltage)
            pobeda.wait(samp)
    except KeyboardInterrupt:
        print("хуйло")
    finally:
        if dac is not None:
            dac.deinit()
