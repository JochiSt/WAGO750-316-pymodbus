
from .WAGO_750 import WAGO_750

class io_module(object):
    """
        Base class for a WAGO / Beckhoff io module
    """
    
    def __init__(self, controller : WAGO_750):
        controller.add_module(self)
        print("Creating a new IO module")
    