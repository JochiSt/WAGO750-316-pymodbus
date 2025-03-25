"""
    WAGO 750-430
    8DI 24V 3.0ms
"""

from .io_module import io_module
from .WAGO_750 import WAGO_750

class WAGO_750_430(io_module):
    
    def __init__(self, controller : WAGO_750):
        super(WAGO_750_430, self).__init__(controller)