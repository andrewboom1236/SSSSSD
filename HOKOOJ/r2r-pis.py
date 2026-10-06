import pisinus as ps
import zov2 as zov
import time as t

amp = 3.0
sig_freq = 10
samp_freq = 1000
gpio_bits = [16, 20, 21, 25, 26, 17, 27, 22]

if __name__ == "__main__":
    dac = zov.R2R_DAC(gpio_bits, 3.183, False)
    try:
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
        dac.deinit()