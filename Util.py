class Util():
    def __init__(self) -> None:
        pass

    def parseStrToNumber(s):
        result = ''
        s = s.replace(' ', '')
        for c in s:
            # Numbers (48~57), negative sign (45), decimal point (46)
            if 48 <= ord(c) <= 57 or ord(c) == 45 or ord(c) == 46:
                result += c
            # Kilo
            elif c in 'Kk':
                result = f'{eval(result) * 1000}'
            # Mega
            elif c in 'Mm':
                result = f'{eval(result) * 1000000}'
        if result == '':
            result = '0'
        return eval(result)
