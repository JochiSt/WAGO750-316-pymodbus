"""
    WAGO 750 316 RS232 Modbus Buscoupler
"""

from pymodbus.client import ModbusSerialClient as ModbusClient

from .WAGO_750 import WAGO_750

class WAGO_750_316(WAGO_750):

    def __init__(self, port="/dev/ttyUSB0", baudrate=9600, device_id=1, DEBUG=False):
        super(WAGO_750_316, self).__init__(DEBUG=DEBUG)
        self.client = ModbusClient(
                port=port, 
                baudrate=baudrate, 
                bytesize=8, 
                timeout=2,
                parity='N',
                stopbits=1,
                handle_local_echo=True,
                retries=0
                )
        self.device_id=device_id
        
        if self.client.connect():
            print("connection to device succeeded")
        else:
            print("ERROR in connection")
            
        self.read_firmware_info()
        self.read_constant_registers()
        self.read_configuration_registers()
            