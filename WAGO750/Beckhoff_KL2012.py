"""
    KL2012
    2 channel Digital output 24V DC
"""
from .io_module import io_module
from .WAGO_750 import WAGO_750

class Beckhoff_KL2012(io_module):
    
    def __init__(self, controller : WAGO_750):
        super(Beckhoff_KL2012, self).__init__(controller, NoutBits=2)
        
    def setBinaryOutputs(self, value = []):
        assert len(value) == 2
        print("setting digital outputs")
        self.controller.client.write_coils( 0x0000 + self.outBitOffset, value )
        
    def getBinaryOutputs(self):
        return self.controller.client.read_input_registers( 0x0200 + self.outBitOffset).registers[0]
