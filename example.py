import pyvisa
import time

def setBurst(src, phase):
    instrument.write(f'TRIG{src}:SOURCE BUS')
    instrument.write(f'SOURCE{src}:BURST:MODE TRIG')
    instrument.write(f'SOURCE{src}:BURST:NCYCles INFinity')
    instrument.write(f'SOURCE{src}:BURST:INTernal:PERiod MIN')
    instrument.write(f'SOURCE{src}:BURST:PHASE {phase}')
    instrument.write(f'SOURCE{src}:BURST:STATE ON')
    instrument.write(f'OUTPUT{src}:STAT ON')

if __name__ == "__main__":

    resourceManager = pyvisa.ResourceManager()
    print(resourceManager)
    print(f'Instruments VISA address: {resourceManager.list_resources()}')

    VISA_ADDRESS = input('Input instruments VISA address: ')

    instrument = resourceManager.open_resource(VISA_ADDRESS)
    print(instrument.query('*IDN?'))

    instrument.write("SOURCE1:VOLT:UNIT VRMS")
    instrument.write("SOURCE2:VOLT:UNIT VRMS")

    instrument.write("SOURCE1:APPLY:SIN 850kHz, 3.5356VRMS")
    setBurst(1, 0)
    instrument.write("SOURCE2:APPLY:SIN 850kHz, 3.5356VRMS")
    setBurst(2, 180)
    instrument.write('*TRG')

    time.sleep(3)
    instrument.write("OUTPUT1:STAT OFF")
    instrument.write("OUTPUT2:STAT OFF")
    instrument.write('SOURCE1:BURST:STATE OFF')
    instrument.write('SOURCE2:BURST:STATE OFF')
    resourceManager.close()
    instrument.close()