import serial

LaunchPad = serial.Serial('COM4', 9600)

while True:
    Entrada=raw_input("H para encender, L para apagar ")
    if Entrada== "H" or Entrada=="L":
        LaunchPad.write(Entrada)
    else:
        break
LaunchPad.close()
