"""
1)Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
"""
def cuenta_regresiva(numero):
    lista = []
    for item in range(numero, -1, -1):
        lista.append(item)
    return lista
"""
2)Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
"""
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]
"""
3)Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
"""
def primero_mas_longitud(lista):
    suma = lista[0] + len(lista)
    return suma
"""
4)Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
"""
def valores_mayores_que_segundo(lista):
    if len(lista) < 2:
        return False

    segundo_valor = lista[1]
    valores_mayores = [valor for valor in lista if valor > segundo_valor]
    cantidad_valores_mayores = len(valores_mayores)

    print("Cantidad de valores mayores que el segundo:", cantidad_valores_mayores)
    return valores_mayores
"""
5)Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
"""
def longitud_y_valor(tamaño, valor):
    lista = [valor] * tamaño
    return lista
print(longitud_y_valor(5,7))
