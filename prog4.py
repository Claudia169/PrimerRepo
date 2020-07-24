

print ("***** Bienvenido al menú *****")
opcion = "0"


while opcion == "0":

    print ("Operaciones: ")
    print("S.Suma") 
    print ("R.Resta")
    print("M.Multiplicación")
    print("A.Salir")

    opcion = input ("Qué operación desea realizar: ")
    
if opcion =='S':
    num1 = input("Ingrese un numero: ")
    num2 = input("Ingrese otro numero: ")
    resultado = num1 + num2
    print (f"La suma es {resultado}")
elif opcion=='R': 
    num1 = input("Ingrese un numero: ")
    num2 = input("Ingrese otro numero: ")
    resultado2 = num1 - num2
    print (f"La resta es {resultado2}")
elif opcion == 'M': 
    num1 = input("Ingrese un numero: ")
    num2 = input("Ingrese otro numero: ")
    resultado3 = num1 * num2
    print (f"La multiplicación es {resultado3}")
else: 
    opcion = "0"
    

