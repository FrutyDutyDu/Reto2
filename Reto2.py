import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SP1i=2 #Sensores de cada piso izquierda
SP2i=3
SP3i=4
SP4i=17
SP1d=27 #Sensores de cada piso derecha
SP2d=22
SP3d=10
SP4d=9

Ps1= #Botones pedir ascensor subir
Ps2=
Ps3=

Pb2=  #Botones pedir ascensor bajar
Pb3=
Pb4=

UPi=14 #Movimientos del motor izquierdo
DWNi = 15
VELi = 18
UPd=23 #Movimientos del motor derecho
DWNd = 24
VELd = 25

PUP= 20#Botones pedir ascensor
PDWN=21

GPIO.setup(SP1i, GPIO.IN) #Config. sensores de cada piso como entradas
GPIO.setup(SP2i, GPIO.IN)
GPIO.setup(SP3i, GPIO.IN)
GPIO.setup(SP4i, GPIO.IN)
GPIO.setup(SP1d, GPIO.IN) #Config.sensores de cada piso como entradas
GPIO.setup(SP2d, GPIO.IN)
GPIO.setup(SP3d, GPIO.IN)
GPIO.setup(SP4d, GPIO.IN)
GPIO.setup(Ps1, GPIO.IN) #Configurar botones pedir asc. como entradas
GPIO.setup(Ps2, GPIO.IN)
GPIO.setup(Ps3, GPIO.IN)
GPIO.setup(Pb2, GPIO.IN)
GPIO.setup(Pb3, GPIO.IN)
GPIO.setup(Pb4, GPIO.IN)


GPIO.setup(PUP, GPIO.IN) #Config. botones pedir ascensor
GPIO.setup(PDWN, GPIO.IN)

GPIO.setup(UPi, GPIO.OUT) #Configurar movimiento del motor izquierdo como salidas
GPIO.setup(DWNi, GPIO.OUT)
GPIO.setup(VELi, GPIO.OUT)
GPIO.setup(UPd, GPIO.OUT) #Configurar movimiento del motor derecho como salidas
GPIO.setup(DWNd, GPIO.OUT)
GPIO.setup(VELd, GPIO.OUT)

sensor = {SP1i, SP2i, SP3i, SP4i}

def ubicacion():
    if GPIO.input(SP1i):
        return 1
    elif GPIO.input(SP2i):
        return 2
    elif GPIO.input(SP3i):
        return 3
    elif GPIO.input(SP4i):
        return 4
    return 0

def botones():
    if GPIO.input(Ps1):
        return 1
    elif GPIO.input(Ps2):
        return 2
    elif GPIO.input(Ps3):
        return 3
    elif GPIO.input(Ps4):
        return 4
    if GPIO.input(Pb1):
        return 1
    elif GPIO.input(Pb2):
        return 2
    elif GPIO.input(Pb3):
        return 3
    elif GPIO.input(Pb4):
        return 4
    return 0

while True:
    #destino=int(input("Piso destino")) debería leer los botone del ascensor
    destino= GPIO.input (botones)
    origen=ubicacion()
    if origen==0:
        print("Pide el ascensor")
    elif destino>origen:
        print("Bajar") 
        while destino!=origen:
          GPIO.output(DWNi,1)
          origen=ubicacion()
        print("Llego al destino")
        GPIO.output(DWNi,0)
    elif destino<origen:
        print("Subir") 
        while destino!=origen:
          GPIO.output(UPi,1)
          origen=ubicacion()
        print("Llego al destino")
        GPIO.output(UPi,0)
    else:
        print("Ya esta en el destino")
        GPIO.output(izquierda,0)
        GPIO.output(DWNi,0)