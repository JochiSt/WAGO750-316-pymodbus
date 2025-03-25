"""
    4 channel digital output module
"""

from .io_module import io_module
from .WAGO_750 import WAGO_750


class WAGO_750_504(io_module):
    
    def __init__(self, controller : WAGO_750):
        super(WAGO_750_504, self).__init__(controller)