"""
    Beckhoff KL1104
    4 channel digital input
"""

from .io_module import io_module
from .WAGO_750 import WAGO_750

class Beckhoff_KL1104(io_module):
    
    def __init__(self, controller : WAGO_750):
        super(Beckhoff_KL1104, self).__init__(controller)