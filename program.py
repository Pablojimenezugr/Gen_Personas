import sys
import random 
from datetime import datetime, timedelta

class Persona:
    def __init__(self, n, a, f, nm):
        self._nombre = n
        self._ape = a
        self._nac = f
        self._nota_media = nm

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._ape

    @property
    def fecha_nac(self):
        return self._nac

    @property
    def nota_media(self):
        return self._nota_media
    
    def __str__(self):
        return self._nombre + " " + self._ape + " " + self._nac + " " +str(self._nota_media)

# -------------------------------------------------------------------------

def cargarNombres_Apellidos(nombres, apes):
    fich = open("nombres.txt")
    fich2 = open("apellidos.txt")
    
    for linea in fich:
        nombres.append( linea.strip('\n') )

    fich.close()

    for linea in fich2:
        apes.append( linea.strip('\n') )
        
    fich2.close()

# -------------------------------------------------------------------------
def generar_fecha(anio_i, anio_f):
    '''
    No todos los meses tienen 31 días, pero para lo que es el programa nos
    da igual ese detalle.
    '''
    d = random.randint(1, 31)
    m = random.randint(1, 12)
    a = random.randint(anio_i, anio_f)   
  
    return str(a) + "-" + str(m) + "-" + str(d)

def insertSQL(personas):
    s = ""
    for p in personas:
        s = "INSERT INTO `personas`(`Nombre`, `Apellidos`, `Nacimiento`, `Nota_media`) VALUES ('"
        s += p.nombre + "','" + p.apellido + "','" + p.fecha_nac + "'," + str(p.nota_media) + ");"
        print(s)

nombres = []
apes = []
cargarNombres_Apellidos(nombres, apes)
personas= []


for i in range( int(sys.argv[1]) ):
    personas.append( Persona(random.choice(nombres),
                             random.choice(apes) + " " + random.choice(apes),
                             generar_fecha(1999, 2005),
                             round(random.uniform(0.5, 10.0), 3)) 
                    )

insertSQL(personas)