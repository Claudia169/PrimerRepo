#INDICA UN TEXTO Y UN NUMERO Y DE ACUERDO A ESTA IMPRIMIRA EL TEXTO CUANTAS VECES HAYA SIDO EL NUMERO INDICADO

def repetir(texto, numero):
    texto += '\n'
    print(texto*numero)

#escribir el codigo para usar la funcion
t = input("ingresa un texto: ")
n = int(input("ingresa un numero: "))

repetir(t,n)