"""     Mi primer código       """

print('Hola Mundo')

def hola(a,b):
    return a + b

print(hola(4, 10))

lista = [1, 2, 4, 7, 5, 6]
maximo = lista[0]
for i in range(1,len(lista)):
    if lista[i]>maximo:
        maximo=lista[i]
print("El maximo es: "+str(maximo))
