
class WAGO_750(object):
    
    _FIRMWARE_INFO_REGISTERS = {
        "INFO_REVISION"     : (0x2010,  1),
        "INFO_SERIES"       : (0x2011,  1),
        "INFO_ITEM"         : (0x2012,  1),
        "INFO_MAJOR"        : (0x2013,  1),
        "INFO_MINOR"        : (0x2014,  1),
        "INFO_DESCRIPTION"  : (0x2020, 32),
        "INFO_TIME"         : (0x2021, 16),
        "INFO_DATE"         : (0x2022, 16)
    }
    
    
    def __init__(self):
        self.client = None
        self.device_id=0
        self._FIRMWARE_INFO_RESULT = {}
        
    def read_firmware_info(self):
        for key in WAGO_750._FIRMWARE_INFO_REGISTERS.keys():          
            result = self.client.read_input_registers( 
                WAGO_750._FIRMWARE_INFO_REGISTERS[key][0], count=WAGO_750._FIRMWARE_INFO_REGISTERS[key][1], slave=self.device_id)
            
            self._FIRMWARE_INFO_RESULT[key] = result.registers
            
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
                