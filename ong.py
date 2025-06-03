
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

def calcular(**kwargs):
    """
    Se entregan valores con instrucciones y retorna impresión en pantalla con los resultados
    """
    print("\nCalculemos la productoria y el factorial de los valores ingresados\n")
    for x,y in kwargs.items():


        if "fact" in x.lower():
            resultado = factorial(y)
            print(f"El factorial de {y} es {resultado}")
        elif "prod" in x.lower():
            resultado = productoria(y)
            print(f"La productoria de {y} es {resultado}")
    print()

    





calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
