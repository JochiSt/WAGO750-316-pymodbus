"""
    KL2134
    4 channel Digital output 24V DC
"""
from .io_module import io_module
from .WAGO_750 import WAGO_750

class Beckhoff_KL2134(io_module):
    
    def __init__(self, controller : WAGO_750):
        super(Beckhoff_KL2134, self).__init__(controller, NoutBits=4)
        

        
