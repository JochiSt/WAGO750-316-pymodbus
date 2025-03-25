"""
    4 channel digital output module
"""

from .io_module import io_module

class WAGO_750_504(io_module):
    
    def __init__(self, controller):
        super(WAGO_750_504, self).__init__(controller)