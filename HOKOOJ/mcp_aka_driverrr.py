import smbus
class MCP:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range
    def denit(self):
        self.bus.close()
    def set_num(self, number):
        if not isinstance(number, int):
            print("только целые урод")
        
        if not (0 <= number <= 4095):
            print("выходишь за рамочки брат")
        
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage(self, voltage):
        if not (0 <= voltage <= self.dynamic_range):
            print("говно говнищееееее")
        number = int(voltage / self.dynamic_range * 4095)
        self.set_num(number)
if __name__ == "__main__":
    dac = None
    try:
        dac = MCP(dynamic_range = 5.11)
        while True:
            voltage = float(input("кентишка мой солнце дай напряга "))
            dac.set_voltage(voltage)
    except KeyboardInterrupt:
        print("дура ты")
    finally:
        if dac is not None:
            dac.denit()