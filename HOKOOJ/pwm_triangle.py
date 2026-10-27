import niger3
import time
import pisinus



freq = 2.0
amp = 3.28
samp_freq = 200
if __name__ == "__main__":

    dac = None
    try:
        dac = niger3.PWM_DAC(12, 1000, 3.290)
        t0 = time.time()
        while True:
            t = time.time() - t0

            raw = pisinus.triang(freq, t)
            voltage = amp * raw
            dac.set_voltage(voltage)
            pisinus.wait(samp_freq)
    except KeyboardInterrupt:
        print("дебил")

    finally:
        if dac is not None:
            dac.deinit()