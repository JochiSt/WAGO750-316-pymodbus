"""
    KL2134
    4 channel Digital output 24V DC
"""
from .io_module import io_module
from .WAGO_750 import WAGO_750

class Beckhoff_KL2134(io_module):
    
    def __init__(self, controller : WAGO_750):
        self.NoutBits = 4
        super(Beckhoff_KL2134, self).__init__(controller, NoutBits=self.NoutBits)
        
    def setBinaryOutputs(self, value = []):
        assert len(value) == 4
        self.controller.client.write_coils( 0x0000 + self.outBitOffset, value )
        
    def getBinaryOutputs(self):
        outputs = []
        for i in range(self.NoutBits):
            outputs.append( self.controller.client.read_coils( 0x0200 + self.outBitOffset + i).bits[0] )
        return outputs
        
