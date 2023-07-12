"""
cmp(dict1, dict2): compara dos diccionarios. El proceso de comparación comienza con la longitud de cada diccionario, seguido de los nombres de las claves, seguidos de los valores. La función devuelve 0 si los dos diccionarios son iguales, -1 si dict1 > dict2, 1 si dict1 < dict2. 
len() : proporciona la longitud total del diccionario. 
str(): produce una representación de cadena de un diccionario. 
type() : devuelve el tipo de la variable pasada. Si la variable pasada es un diccionario, devolverá un tipo de dict. 
Python incluye los siguientes métodos de diccionario:

(funcionará dict.method(yourDictionary) o yourDictionary.method())

.clear(): elimina todos los elementos del diccionario 
.copy() : devuelve un diccionario de copia superficial 
.fromkeys(sequence, [value] ): crea un nuevo diccionario con claves de secuencia y valores establecidos al valor. 
.get(key, default=None): para clave, devuelve un valor o default si la clave no está en el diccionario. 
.has_key(key) : devuelve verdadero si una clave determinada está disponible en el diccionario; de lo contrario, devuelve false. 
.items(): devuelve una lista de pares de tuplas (clave, valor) del diccionario. 
.keys(): devuelve una lista de claves de diccionario. 
.setdefault(key, default=None) : similar a get(), pero establecerá dict[key]=default si la clave no está ya en el diccionario. 
.update(dict2): agrega pares clave-valor del diccionario dict2 a un diccionario existente. 
.values(): devuelve una lista de valores del diccionario. 
"""

#imprime todos los números enteros del 0 al 150.

for i in range(151):
    print(i)

#imprime todos los múltiplos de 5 entre 5 y 1,000.

for i in range(5, 1001, 5):
    print(i)

#imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#agrega los enteros impares del 0 al 500,000, e imprime la suma final.

suma = 0
for i in range(1, 500001, 2):
    suma += i

print("La suma de los enteros impares del 0 al 500,000 es:", suma)

#imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.

for i in range(2018, 0, -4):
    print(i)

#establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 


lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)

#   