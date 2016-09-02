def ascii_to_bin(char):
	ascii = ord(char)
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
 
 
# Ejemplo:

def ingreso():
    String = raw_input('Ingrese el Texto --->    ')

    binary = []
    for char in String:
            binary.append(ascii_to_bin(char))
     
    print binary
    print " ".join(binary) 

ingreso()
