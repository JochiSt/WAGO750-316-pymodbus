"""
    WAGO 750-1515
    8 channel digital output
"""

from .io_module import io_module
from .WAGO_750 import WAGO_750

class WAGO_750_1515(io_module):
    
    def __init__(self, controller : WAGO_750):
        super(WAGO_750_1515, self).__init__(controller)