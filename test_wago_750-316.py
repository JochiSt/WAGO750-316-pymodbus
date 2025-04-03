"""
    testing the WAGO 750 316 I/O controller
"""

from WAGO750 import WAGO_750_316
from WAGO750 import WAGO_750_430, Beckhoff_KL1104
from WAGO750 import WAGO_750_504, WAGO_750_1515

from WAGO750 import WAGO_750_600

from WAGO750 import Beckhoff_KL4032
from WAGO750 import Beckhoff_KL2134, Beckhoff_KL2012

import time


################################################################################
modbus_io = WAGO_750_316(DEBUG=True)
# teststack from side of BUSmaster

KL2134_0 = Beckhoff_KL2134(modbus_io)
KL2134_1 = Beckhoff_KL2134(modbus_io)

KL4032_0 = Beckhoff_KL4032(modbus_io)

KL2012_0 = Beckhoff_KL2012(modbus_io)
KL2012_1 = Beckhoff_KL2012(modbus_io)

# WAGO 750-600      endterminal
_ = WAGO_750_600(modbus_io)

################################################################################
# reset outputs
value = [0,0,0,0]
KL2134_0.setBinaryOutputs( value )
KL2134_1.setBinaryOutputs( value )

KL2012_0.setBinaryOutputs( value[:2])
KL2012_1.setBinaryOutputs( value[:-2])

time.sleep(0.5)

for i in range(4):
    value = [0,0,0,0]
    value[i] = 1
    KL2134_0.setBinaryOutputs( value )
    KL2134_1.setBinaryOutputs( value )
    
    KL2012_0.setBinaryOutputs( value[:2])
    KL2012_1.setBinaryOutputs( value[-2:])
    
    time.sleep(0.5)
    
KL4032_0.setAnalogOutput(0,0x7fff)
KL4032_0.setAnalogOutput(1,0)

print(KL4032_0.getAnalogOutput(0), KL4032_0.getAnalogOutput(1))

print(KL2134_0.getBinaryOutputs(), KL2134_1.getBinaryOutputs())

