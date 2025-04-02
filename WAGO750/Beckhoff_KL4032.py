"""
    KL4032 
    2 channel -10V ... + 10V output (12 bit)
    
    -10V = 0x8001
    +10V = 0x7FFF
"""
from .io_module import io_module
from .WAGO_750 import WAGO_750

class Beckhoff_KL4032(io_module):
    
    def __init__(self, controller : WAGO_750):
        super(Beckhoff_KL4032, self).__init__(controller, N_in_regs=None, N_out_regs=2)
        
    def setAnalogOutput(self, channel, value):
        assert channel in [0,1]
        self.controller.client.write_register( 0x0000 + self.output_offset + channel, value )
            
    def getAnalogOutput(self, channel):
        assert channel in [0,1]
        return self.controller.client.read_input_registers( 0x0200 + self.output_offset + channel).registers[0]
