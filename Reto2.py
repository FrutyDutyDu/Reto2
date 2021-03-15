import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

SP1i=2 #Sensores de cada piso izquierda
SP2i=3
SP3i=4
SP4i=17
SP1d=27 #Sensores de cada piso derecha
SP2d=22
SP3d=10
SP4d=9

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
GPIO.setup(PUP, GPIO.IN) #Config. botones pedir ascensor
GPIO.setup(PDWN, GPIO.IN)

GPIO.setup(UPi, GPIO.OUT) #Configurar movimiento del motor izquierdo como salidas
GPIO.setup(DWNi, GPIO.OUT)
GPIO.setup(VELi, GPIO.OUT)
GPIO.setup(UPd, GPIO.OUT) #Configurar movimiento del motor derecho como salidas
GPIO.setup(DWNd, GPIO.OUT)
GPIO.setup(VELd, GPIO.OUT)

sensor = {SP1i, SP2i, SP3i, SP4i}