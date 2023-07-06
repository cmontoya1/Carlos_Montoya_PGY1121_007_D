import numpy as np
pre_entrada_platinum=12000
pre_entrada_gold=80000
pre_entrada_silver=50000


def mostrar_menu():
    print("""  Bienvenido a la productora "Creativos.cl"     
                    Menú
    1.Comprar entradas
    2.Mostrar ubicaciones disponibles
    3.Ver listado de asistentes
    4.Mostrar ganancias totales
    5.Salir""")

def validar_opc():
    while True:
        try:
            opc=int(input("Ingrese opción: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR! LA OPCIÓN DEBE ESTAR ENTRE 1 Y 5")
        except:
            print("ERROR!DEBE INGRESAR UN NÚMERO ENTERO")

def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese rut: "))
            if len(str(rut)) >=7 and len(str(rut))<=8:
                return rut
            else:
                print("ERROR!EL RUT NO DEBE GUION, PUNTOS, DÍGITO VERIFICADO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")

def validar_fila():
    while True:
        try:
            fila=int(input("Ingrese fila(1-10): "))
            if fila >=1 and fila <=10:
                return fila
            else:
                print("ERROR! DEBE ESTAR ENTRE 1 Y 10")
        except:
            print("ERROR!DEBE INGRESAR UN NÚMERO ENTERO")

def validar_columna():
    while True:
        try:
            columna=int(input("Ingrese columna(1-10): "))
            if columna >=1 and columna <=10:
                return columna
            else:
                print("ERROR! DEBE ESTAR ENTRE 1 Y 10")
        except:
            print("ERROR!DEBE INGRESAR UN NÚMERO ENTERO")

def validar_cantidad_entradas():
   while True:
       try:
           cantidad_entrada=int(input("Cuántas entradas desea comprar: "))
           if cantidad_entrada >=1 and cantidad_entrada <=3:
               return cantidad_entrada
           else:
               print("ERROR! LA CANTIDAD DE ENTRADAS DEBE ESTAR ENTRE 1 Y 3")
               
       except:
           print("ERROR!DEBE INGRESAR UN NÚMERO ENTERO")

def validar_tipo_entradas():
    print(f"""Tipos de entrada
          1.PLATINUM ${pre_entrada_platinum}
          2.GOLD     ${pre_entrada_gold}
          3.SILVER   ${pre_entrada_silver}""")
    while True:
        try:
            tipo_entrada=int(input("Ingrese tipo de entrada: "))
            if tipo_entrada in(1,2,3):
                return tipo_entrada
            else:
                print("ERROR!DEBE INGRESAR UN TIPO DE ENTRADA ENTRE 1 Y 3")
        except:
            print("ERROR!DEBE INGRESAR UN NÚMERO ENTERO")          
              
                
            
        

concierto=np.zeros((10,10),int)
lista_cantidad_entradas=[]
lista_tipo_entradas=[]
lista_ruts=[]
lista_filas=[]
lista_columnas=[]
lista_cedulas=[]
        

def mostrar_concierto():
    print("           1  2  3  4  5  6  7  8  9  10")
    for x in range(10):
        print(f"Filas:{x+1}",end="    ")
        for y in range(10):
            print(concierto[x][y],end="  ")
        print() 

def validar_cedula():
    while True:
        try:
            cedula=int(input("Posee cédula de identidad?(1.SI/2.NO): "))
            if cedula==1:
                nombre=validar_nombre()
                apellido=validar_apellido()
                fecha=validar_fecha()
                return 
            else:
                print("Se necesita cédula de identidad para ingresar")
        except:
            print("ERROR!DEBE INGRESAR UN NÚMERO ENTERO")

def validar_nombre():
    while True:
        nombre=input("Ingrese nombre: ")
        if len(nombre.strip()) >=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR!el nombre debe tener 3 o más letras ")

def validar_apellido():
    while True:
        apellido=input("Ingrese apellido: ")
        if len(apellido.strip()) >=3 and apellido.isalpha():
            return apellido
        else:
            print("ERROR!el apellido debe tener 3 o más letras ")



def validar_fecha():
    return

def listado_asistentes():
        posicion=lista_ruts.index
        print(posicion)



def comprar():
    if 0 not in concierto:
        print("NO HAY ENTRADAS DISPONIBLES!")
        return
    cedula=validar_cedula()
    rut=validar_rut()
    cantidad_entrada=validar_cantidad_entradas()
    tipo_entrada=validar_tipo_entradas()
    while True:
        mostrar_concierto()
        fila=validar_fila()
        columna=validar_columna()
        if concierto[fila-1][columna-1]==0:
            concierto[fila-1][columna-1]=1
            lista_ruts.append(rut)
            lista_cedulas.append(cedula)
            lista_cantidad_entradas.append(cantidad_entrada)
            lista_tipo_entradas.append(tipo_entrada)
            lista_filas.append(fila-1)
            lista_columnas.append(columna-1)
            print("Compra realizada con éxito")
            return
        else:
            print("Asiento no disponible") 

def listado_asistentes():
    print("Listado de asistentes")
    print(lista_ruts)
    return                        



acumulador=0
def ganancias():
    for x in range(10):
        for y in range(10):
            if concierto[x][y]==1:
                acumulador

def salir():
    print("Salir")
    cedula=validar_cedula()
    if cedula in lista_cedulas:
        posicion=lista_cedulas.index(posicion)
        print("Gracias por su compra!", lista_cedulas(posicion))

                    
                
       
            
            


        
    

        
        

    
        

                
            
