import pyvisa
from Util import Util

class Base():
    def __init__(self, visaAddress) -> None:
        self.initAddress(visaAddress)
        self.getInstrument()
        self.initConst()

    def initAddress(self, visaAddress):
        self.VISA_ADDRESS = visaAddress

    def initConst(self):
        # Parameters
        self.P = {
            'V_TYPE': 'SIN',
            'V_MAX': 3.536,
            'V_MIN': 0.01,
            'V_UNIT': 'VRMS',
            'F_MAX': 1000000,
            'F_MIN': 50,
            'F_UNIT': 'HZ',
            'LOAD': 50,
            'ANGLE': 'DEGREE',
        }

    def getInstrument(self):
        self.resourceManager = pyvisa.ResourceManager()
        self.instrument = self.resourceManager.open_resource(self.VISA_ADDRESS)

    def checkValueInRange(self, p, value):
        return self.P[f'{p}_MIN'] <= value <= self.P[f'{p}_MAX']

    def autoranging(self, parameter, value):
        p = parameter.upper()
        if not self.checkValueInRange(p, value):
            if value > self.P[f'{p}_MAX']:
                return self.P[f'{p}_MAX']
            else:
                return self.P[f'{p}_MIN']
        else:
            return value

    def queryIDN(self):
        print(f"[IDN] {self.instrument.query('*IDN?')}")

    def queryERROR(self):
        check = True
        while (check):
            tmp = self.instrument.query('SYSTem:ERRor?')
            # tmp can be these cases
            # -222,"Data out of range; amplitude; value clipped to maximum"
            # +0,"No error"
            t = eval(tmp.split(',')[0])
            if t:
                print(f"[ERROR] {tmp}")
            else:
                check = False
        self.instrument.write('*CLS')

    def _query(self, cmd):
        return self.instrument.query(cmd)

    def _write(self, cmd):
        self.instrument.write(cmd)

    def parseStrToNumber(self, s):
        return Util.parseStrToNumber(s)

    def close(self):
        self.resourceManager.close()
        self.instrument.close()