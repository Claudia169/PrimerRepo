

print ("***** Bienvenido al menú *****")
menu = "A"


print ("Operaciones: ")
print("S.Suma") 
print ("R.Resta")
print("M.Multiplicación")
print("A.Salir")

while menu == opcion :
    opcion = input ("Qué operación desea realizar: ")
    if opcion == 'S':
        num1 = ("Ingrese un numero: ")
        num2 = ("Ingrese otro numero: ")
        resultado = num1 + num2
        print (f"La suma es {resultado}")
    elif opcion== 'R': 
        num1 = ("Ingrese un numero: ")
        num2 = ("Ingrese otro numero: ")
        resultado = num1 - num2
        print (f"La resta es {resultado}")
    elif opcion== 'M': 
        num1 = ("Ingrese un numero: ")
        num2 = ("Ingrese otro numero: ")
        resultado = num1 * num2
        print (f"La multiplicación es {resultado}")
    else: 
        opcion = "A"
    

