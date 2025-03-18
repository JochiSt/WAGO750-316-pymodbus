
class WAGO_750(object):
    
    def __init__(self):
        self.client = None
        self.device_id=0
        print("")
        
    def read_firmware(self):
        result = self.client.read_input_registers(0x2010, count=1, slave=self.device_id)
        print(result)