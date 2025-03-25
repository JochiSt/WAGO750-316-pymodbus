"""
    WAGO 750-600
    End Module
"""

from .io_module import io_module
from .WAGO_750 import WAGO_750

def WAGO_750_600(io_module):
    def __init__(self, controller : WAGO_750):
        super(WAGO_750_600, self).__init__(controller)