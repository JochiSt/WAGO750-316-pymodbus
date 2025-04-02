
from .WAGO_750 import WAGO_750

class io_module(object):
    """
        Base class for a WAGO / Beckhoff io module
    """
    
    def __init__(self, controller : WAGO_750, N_in_regs = None, N_out_regs = None):
        self.controller = controller
        if self.controller._DEBUG:
            print("Creating a new IO module")
        self.input_offset, self.output_offset = controller.add_module(self, N_in_regs = N_in_regs, N_out_regs = N_out_regs)
        
    def readBinaryInputs(self):
        print("not implemented")
        
    def setBinaryOutputs(self, outputs = []):
        print("not implemented")
        
    def setAnalogOutputs(self, outputs = []):
        print("not implemented")
        
    def readAnalogInputs(self):
        print("not implemented")
    