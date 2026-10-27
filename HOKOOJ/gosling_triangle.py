import mcp_aka_driverrr as gosling
import pisinus
import time

amp = 0.5
freq = 10
samp = 1000

if __name__ == "__main__":
    dac = None
    try:
        dac = gosling.MCP(5.11, 0x61, verbose = False)
        t0 = time.time()

        while True:
            t = time.time() - t0
            voltage = amp * pisinus.triang(freq, t)
            dac.set_voltage(voltage)
            pisinus.wait(samp)

    except KeyboardInterrupt:
        print("lt,nk")

    finally:
        if dac is not None:
            dac.denit()
