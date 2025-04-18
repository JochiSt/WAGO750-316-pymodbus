
class WAGO_750(object):
    
    _FIRMWARE_INFO_REGISTERS = {
        # Name                address, length
        "INFO_REVISION"     : (0x2010,  1),
        "INFO_SERIES"       : (0x2011,  1),
        "INFO_ITEM"         : (0x2012,  1),
        "INFO_MAJOR"        : (0x2013,  1),
        "INFO_MINOR"        : (0x2014,  1),
        "INFO_DESCRIPTION"  : (0x2020, 32),
        "INFO_TIME"         : (0x2021, 16),
        "INFO_DATE"         : (0x2022, 16),
    }
    
    _CONSTANT_REGISTERS = {
        # Name                address, length
        "GP_ZERO"           : (0x2000, 1), 
        "GP_ONES"           : (0x2001, 1), 
        "GP_1234"           : (0x2002, 1), 
        "GP_AAAA"           : (0x2003, 1), 
        "GP_5555"           : (0x2004, 1), 
        "GP_MAX_POS"        : (0x2005, 1), 
        "GP_MAX_NEG"        : (0x2006, 1), 
        "GP_MAX_HALF_POS"   : (0x2007, 1), 
        "GP_MAX_HALF_NEG"   : (0x2008, 1), 
    }
    
    _CONSTANT_REG_VALUES = {
        # Name                value
        "GP_ZERO"           : 0x0000, 
        "GP_ONES"           : 0xFFFF, 
        "GP_1234"           : 0x1234, 
        "GP_AAAA"           : 0xAAAA, 
        "GP_5555"           : 0x5555, 
        "GP_MAX_POS"        : 0x7FFF, 
        "GP_MAX_NEG"        : 0x8000, 
        "GP_MAX_HALF_POS"   : 0x3FFF, 
        "GP_MAX_HALF_NEG"   : 0x4000, 
    }
    
    _CONFIGURATION_REGISTERS = {
        "CnfLen.AnalogOut"  : (0x1022, 1),
        "CnfLen.AnalogInp"  : (0x1023, 1),
        "CnfLen.DigitalOut" : (0x1024, 1),
        "CnfLen.DigitalInp" : (0x1025, 1),
    }
    
    
    def __init__(self, DEBUG = False):
        self.client = None
        self.device_id = 0
        self._FIRMWARE_INFO_RESULT = {}
        self._CONSTANT_REGISTERS_RESULT = {}
        self._CONFIGURATION_REGISTERS_RESULT = {}
        
        self._DEBUG = DEBUG
        
        self.modules = []
        self.inBitOffset = 0
        self.outBitOffset = 0
        self.inWordOffset = 0
        self.outWordOffset = 0
        
    def read_firmware_info(self):
        for key in WAGO_750._FIRMWARE_INFO_REGISTERS.keys():          
            result = self.client.read_input_registers( 
                WAGO_750._FIRMWARE_INFO_REGISTERS[key][0], count=WAGO_750._FIRMWARE_INFO_REGISTERS[key][1], slave=self.device_id)
            self._FIRMWARE_INFO_RESULT[key] = result.registers
            
        if self._DEBUG:
            for key in self._FIRMWARE_INFO_RESULT.keys():
                print(key, end=" ")
                if key not in ["INFO_DESCRIPTION", "INFO_TIME", "INFO_DATE"]:
                    for value in self._FIRMWARE_INFO_RESULT[key]:
                        print("%X"%(value), end=" ")
                else:
                    # build hex string
                    result_bytes = ""
                    for i in self._FIRMWARE_INFO_RESULT[key]:
                        if ((i & 0xFF00) >> 8) < 255 and i & 0xFF < 255:
                            result_bytes += "%X "%(i & 0xff)
                            if (i & 0xFF00) >> 8 != 0:
                                result_bytes += "%X "%((i & 0xFF00) >> 8)
                            
                    result_bytes = bytes.fromhex( result_bytes )
                    print( result_bytes.decode(errors='ignore'), end="" )
                print()
    
    def read_constant_registers(self):
        for key in WAGO_750._CONSTANT_REGISTERS.keys():          
            result = self.client.read_input_registers( 
                WAGO_750._CONSTANT_REGISTERS[key][0], count=WAGO_750._CONSTANT_REGISTERS[key][1], slave=self.device_id)
            self._CONSTANT_REGISTERS_RESULT[key] = result.registers[0]
            
            assert self._CONSTANT_REGISTERS_RESULT[key] == WAGO_750._CONSTANT_REG_VALUES[key]
        
        if self._DEBUG:
            for key in self._CONSTANT_REGISTERS_RESULT.keys():
                print(key, "%X"%(self._CONSTANT_REGISTERS_RESULT[key]))
            
    def read_configuration_registers(self):
        for key in WAGO_750._CONFIGURATION_REGISTERS.keys():          
            result = self.client.read_input_registers( 
                WAGO_750._CONFIGURATION_REGISTERS[key][0], count=WAGO_750._CONFIGURATION_REGISTERS[key][1], slave=self.device_id)
            self._CONFIGURATION_REGISTERS_RESULT[key] = result.registers[0]
              
        if self._DEBUG:    
            for key in self._CONFIGURATION_REGISTERS_RESULT.keys():
                print(key, "%d"%(self._CONFIGURATION_REGISTERS_RESULT[key]))
            
    def add_module(self, module, NinBits = None, NoutBits = None, NinWords = None, NoutWords = None):                
        offsets = self.getOffsets()
                
        if NinBits:
            self.inBitOffset += NinBits       
        if NoutBits:
            self.outBitOffset += NoutBits
        if NinWords:
            self.inWordOffset += NinWords    
        if NoutWords:
            self.outWordOffset += NoutWords
            
        self.modules.append(module)            
            
        if self._DEBUG:            
            print("\tcurrent offsets", offsets)
            
        return offsets
        
    def getOffsets(self):
        return self.inBitOffset, self.outBitOffset, self.inWordOffset, self.outWordOffset
    