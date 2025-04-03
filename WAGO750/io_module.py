
from .WAGO_750 import WAGO_750

class io_module(object):
    """
        Base class for a WAGO / Beckhoff io module
    """
    
    def __init__(self, controller : WAGO_750, NinBits = None, NoutBits = None, NinWords = None, NoutWords = None):
        self.controller = controller
                
        self.NinBits = NinBits
        self.NoutBits = NoutBits
        
        self.NinWords = NinWords
        self.NoutWords = NoutWords
    
        if self.controller._DEBUG:
            print("Creating a new IO module")
        self.inBitOffset, self.outBitOffset, self.inWordOffset, self.outWordOffset = controller.add_module(self, NinBits = NinBits, NoutBits = NoutBits, NinWords = NinWords, NoutWords = NoutWords)
        
    def setBinaryOutputs(self, value = []):
        assert len(value) == self.NoutBits
        self.controller.client.write_coils( 0x0000 + self.outBitOffset, value )
        
    def getBinaryOutputs(self):
        outputs = []
        for i in range(self.NoutBits):
            outputs.append( self.controller.client.read_coils( 0x0200 + self.outBitOffset + i).bits[0] )
        return outputs        
        
    def getBinaryInputs(self):
        inputs = []
        for i in range(self.NinBits):
            inputs.append( self.controller.client.read_coils( 0x0000 + self.inBitOffset + i).bits[0] )
        return inputs     
                
    def setAnalogOutput(self, output):
        print("not implemented")
        
    def getAnalogOutout(self):
        print("not implemented")
        return None
        
    def readAnalogInputs(self):
        print("not implemented")
        return None
    