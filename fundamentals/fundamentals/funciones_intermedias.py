"""
1)Actualizar valores en diccionarios y listas
"""
x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Cambiar el valor 10 en x a 15
x[1][0] = 15

# Cambiar el "apellido" del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name'] = 'Bryant'

# En el directorio_deportes, cambiar "Messi" por "Andrés"
directorio_deportes['fútbol'][0] = 'Andrés'

# Cambiar el valor 20 en z a 30
z[0]['y'] = 30


print("x:", x)
print("estudiantes:", estudiantes)
print("directorio_deportes:", directorio_deportes)
print("z:", z)

"""
2)Iterar a través de una lista de diccionarios
Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:

"""

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    for diccionario in some_list:
        elementos = []
        for clave, valor in diccionario.items():
            elementos.append(f"{clave} - {valor}")
        print(", ".join(elementos))




iterateDictionary(estudiantes)

"""
3)Obtener valores de una lista de diccionarios
Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

"""

def iterateDictionary2(key_name, some_list):
    for diccionario in some_list:
        if key_name in diccionario:
            print(diccionario[key_name])


iterateDictionary2('first_name', estudiantes)
print("--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--")
iterateDictionary2('last_name', estudiantes)


"""
4)Iterar a través de un diccionarios con valores de lista
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
"""
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for clave, lista in some_dict.items():
        print(f"{len(lista)} {clave.upper()}")
        for valor in lista:
            print(valor)
printInfo(dojo)
