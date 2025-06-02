import sys

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}


def filtrar(numero,orden='mayor',**lista):

#def filtrar(lista:dict[str,int],numero:int,orden:str='mayor'):
    resultado=[]
    if orden == 'mayor':
        for item , precio in lista.items():
            if precio > numero:
                resultado.append(item)

    else:
        for item , precio in lista.items():
            if precio < numero:
                resultado.append(item)
    
    print(f'\nlos productos {orden}es al umbral son: {', '.join(resultado)}\n')

# Se evalua entrada de datos desde terminal, si no se entregan datos, da un error

# Si solo se da un valor, se entrega directamente a la función filtrar
if len(sys.argv)==2:
    umbral=int(sys.argv[1])

    filtrar(precios,umbral)


# Si se entrega un segundo parámetro, se evalua que sean las palabras "menor" o "mayor" para entregarsela a la función,
# de lo contrario entrega un error
elif len(sys.argv)==3:
    umbral=int(sys.argv[1])

    if sys.argv[2].lower()=='menor':
        accion=sys.argv[2].lower()

        filtrar(precios,umbral,accion)

    elif sys.argv[2].lower()=='mayor':
        accion=sys.argv[2].lower()

        filtrar(precios,umbral,accion)

    else:
         print("\nLo sentimos, no es una operación válida\n")


else:
    print("\nLo sentimos, se debe ingresar el valor a analizar y la acción que sigue\n")