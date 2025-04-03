"""
    Beckhoff KL1102
    2 channel digital input
"""

from .io_module import io_module
from .WAGO_750 import WAGO_750

class Beckhoff_KL1002(io_module):
    
    def __init__(self, controller : WAGO_750):
        super(Beckhoff_KL1002, self).__init__(controller, NinBits=2)
    
    
    def readBinaryInputs(self):
        return self.controller.client.read_coils(0x0000 + self.inBitOffset + 0).bits[0], self.controller.client.read_coils(0x0000 + self.inBitOffset + 1).bits[0]