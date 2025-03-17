#
import logging
import logging.handlers as Handlers

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

from pymodbus.client import ModbusSerialClient as ModbusClient

from time import sleep

for baudrate in [
            #1200, 
            #2400, 
            #4800,
            9600, 
            #19200, 
            #38400, 
            #57600, 
            #115200
            ]:

    print("#"*80)
    print("Testing baudrate:", baudrate)
    # Konfiguration des Clients
    client = ModbusClient(
                    port='/dev/ttyUSB0', 
                    baudrate=baudrate, 
                    bytesize=8, 
                    timeout=2,
                    parity='N',
                    stopbits=1,
                    handle_local_echo=True,
                    retries=0
                    )

    try:
        # Verbindung herstellen
        if client.connect():
            print("Verbindung erfolgreich hergestellt.")

            # Beispiel: Lesen von Registern (z.B. 2 Register ab Adresse 0)
            #result = client.read_holding_registers(0x2000, count=1, device_id=1)

            #print(client.read_device_information())

            result = client.read_input_registers(0x2002, count=1, slave=1)

            if not result.isError():
                for value in result.registers:
                   print(f"Gelesene Werte: 0x%X - %d"%(value, value))
            else:
                print("Fehler beim Lesen der Register:", result)
                print(result.decode())

            for state in [True, False, True, False]:
                for coil in range(8):
                    print("setting coil", coil, "to", state)
                    client.write_coil(coil, state, slave=1)
                    sleep(0.5)
                sleep(1)

            # Verbindung schließen
            client.close()
        else:
            print("Verbindung konnte nicht hergestellt werden.")
    except Exception as e:
        print(e)

    client.close()
