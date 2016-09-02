"""Luis Alvarez
Esvin Paredes
Samuel Choc"""

def ingreso():
    m = raw_input('Ingrese el texto')
    conversion(m)

def conversion(m):

    for i in m:
        ascii = ord(i)
        bin = []
        while (ascii > 0):
            if (ascii & 1) == 1:
                    bin.append("1")
            else:
                    bin.append("0")
            ascii = ascii >> 1
        bin.reverse()
        binary = "".join(bin)
        zerofix = (8 - len(binary)) * '0'
        return zerofix + binary
    binary.append(zerofix + binary)
    print " ".join(binary)
    
ingreso()
