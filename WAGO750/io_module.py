
from .WAGO_750 import WAGO_750

class io_module(object):
    """
        Base class for a WAGO / Beckhoff io module
    """
    
    def __init__(self, controller : WAGO_750, NinBits = None, NoutBits = None, NinWords = None, NoutWords = None):
        self.controller = controller
                
        if self.controller._DEBUG:
            print("Creating a new IO module")
        self.inBitOffset, self.outBitOffset, self.inWordOffset, self.outWordOffset = controller.add_module(self, NinBits = NinBits, NoutBits = NoutBits, NinWords = NinWords, NoutWords = NoutWords)
        
    def readBinaryInputs(self):
        print("not implemented")
        
    def setBinaryOutputs(self, outputs = []):
        print("not implemented")
        
    def setAnalogOutput(self, output):
        print("not implemented")
        
    def getAnalogOutout(self):
        print("not implemented")
        return None
        
    def readAnalogInputs(self):
        print("not implemented")
        return None
    