'''

persona = {
    "nombre" : "Anita",
    "edad" : 29,
    "ciudad" : "Lima"
}
print("==============impresiones=================")
print(persona["nombre"])

persona["profesion"] = "Ingenieria industrial"

for clave,valor in persona.items():
    print(clave," : ", valor)

'''

'''
#ejemplos de conjuntos

numeros = {1,2,3,4,5,6}


#agregar un elemento

numeros.add(15)

#eliminar elemento

numeros.discard(4)

print(numeros)

'''

numeros_1 = {1,2,3,4,5,6}

numeros_2 = {4,5,6,7,8,9,10}

union = numeros_1 | numeros_2

intersección = numeros_1 & numeros_2

print(intersección)
