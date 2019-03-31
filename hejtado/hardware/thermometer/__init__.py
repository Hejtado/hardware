import minimalmodbus
import serial

from hejtado.hardware.hardware import connection_section


class Thermometer:
    """Connect to the thermometer via modbus protocol and return current temperature"""

    def __init__(self, tm_id):
        self.tm_id = tm_id
        self.__connect__()

    def __connect__(self):
        """Connect to the thermometer using Modbus protocol"""
        self.instrument = minimalmodbus.Instrument(connection_section['usb'], self.tm_id)
        self.instrument.serial.baudrate = int(connection_section['baudrate'])
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.serial.bytesize = int(connection_section['bytesize'])
        self.instrument.serial.stopbites = int(connection_section['stopbits'])
        self.instrument.serial.timeout = int(connection_section['timeout'])

    def __get_test_temperature(self):
        """Return random value of the temperature for the test purpose"""

        import random

        random_temp = "%.1f" % random.uniform(22.6, 23.5)
        print("Random temp {}".format(random_temp))
        return random_temp

    def get_temperature(self):
        """Get the temparature"""

        return float(self.instrument.read_register(1, 1, functioncode=4))
        # Test code
        #return self.__get_test_temperature()
