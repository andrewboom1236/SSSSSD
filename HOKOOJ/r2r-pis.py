import pisinus as ps
import zov2 as zov
import time as t

amp = 3.2
sig_freq = 10
samp_freq = 1000

if __name__ == "__main__":
    dac = None
    try:
        dac = zov.R2R_DAC(gpio_bits, amplitude)
        start = t.time()

        while True:
            curr = t.time() - start
            norm = ps.pipisinus(sig_freq, curr)
            voltage = norm * amp
            dac.set_voltage(voltage)
            ps.wait(samp_freq)

    except KeyboardInterrupt:
        print("ну liii ты")
    finally:
        if dac is not None:
            dac.deinit()