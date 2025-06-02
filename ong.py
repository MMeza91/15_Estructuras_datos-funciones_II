
def factorial(numero:int) -> int:
    """
    Se entrega un valor entero y devuelve el factorial de dicho número
    """
    factor = 1
    for i in range(numero):
        factor *= (i+1)
    
    return factor

def productoria(valores:list[int]) -> int:
    """
    Se entrega una lista de valores enteros y devuelve el resultado de la multiplicación de dichos números
    """
    producto = 1
    for i in valores:
        producto *= i
    
    return producto

def calcular(variables:str):
    """
    Se entregan valores con instrucciones y retorna impresión en pantalla con los resultados
    """
    variables_divididas = []
    variables_divididas = variables.split(',')

    print(variables_divididas)

    a_1 = []
    for i in variables_divididas:
        a_1.append(i.split(' = '))

    print(a_1)







calcular('fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6')
