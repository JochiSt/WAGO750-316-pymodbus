"""
    testing the WAGO 750 316 I/O controller
"""

from WAGO750 import WAGO_750_316
from WAGO750 import WAGO_750_430, Beckhoff_KL1104
from WAGO750 import WAGO_750_504, WAGO_750_1515

modbus_io = WAGO_750_316()

# teststack from side of BUSmaster

#WAGO 750-430       8 ch di
WAGO_750_430(modbus_io)
#WAGO 750-430       8 ch di

#Beckhoff KL1104    4 ch di

# WAGO 750-504      4 ch do
WAGO_750_504(modbus_io)
# WAGO 750-1515     8 ch do
# WAGO 750-600      endterminal
