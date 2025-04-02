"""
    KL3062
    2 channel 0 ... + 10V input (12 bit)

"""
from .io_module import io_module
from .WAGO_750 import WAGO_750

class Beckhoff_KL3062(io_module):
    
    def __init__(self, controller : WAGO_750):
        super(Beckhoff_KL3062, self).__init__(controller)
        