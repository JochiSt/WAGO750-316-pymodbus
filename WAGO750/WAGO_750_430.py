"""
    WAGO 750-430
    8DI 24V 3.0ms
"""

from .io_module import io_module

class WAGO_750_430(io_module):
    
    def __init__(self, controller):
        super(WAGO_750_430, self).__init__(controller)