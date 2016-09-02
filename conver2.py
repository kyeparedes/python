import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

#m = raw_input('Ingrese el Texto --->  ')
#m = str(m)

def convertir(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    
    print str(decimal) + binario

def conver(n):
    c = []
    while n > 0:
        r = n%2
        #c.append(str(r))
        c.append(r)
        n = n/2
    #hamming(c)
    #print ''.join(c)
    
    while len(c) < 7:
        #c.append(str(0))
        c.append(0)
    #print ''.join(c)
    hamming(c)
    
def hamming(c): 
         

b = bytearray("b1b")
print b[0]
print b[1]
n = b[0]
conver(n)

    
    
