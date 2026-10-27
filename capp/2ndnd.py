from pervash import R2R_ADC
from fuckingfuck import plot_voltage_vs_time

import time

adc = R2R_ADC(dyn_range=3.3, comp_time=0.0001)

voltage_values = []
time_values = []
duration = 3.0

try:
    start = time.time()
    while (time.time() - start) < duration:
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(time.time() - start)

    plot_voltage_vs_time(time_values, voltage_values, adc.dyn_range)

finally:
    adc.__del__()