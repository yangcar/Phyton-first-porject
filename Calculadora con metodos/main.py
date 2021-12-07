def welcome_message():
    print("BIENVENIDOS")
def menu_options():
    menu = " Marque 1 para sumar \n Marque 2 para restar \n Marque 3 para multiplicar \n Marque 4 para dividir"
    print(menu)
def num_operation():
    global numero, numero2
    numero = float(input("Ingrese el primer numero: "))
    numero2 = float(input("ingrese el segundo numero: "))
def sum(n_numero, n_numero2):
    suma = n_numero + n_numero2
    print("el resutaldo es")
    print(suma)
def subtraction(n2_numero, n3_numero):
    resta = n2_numero - n3_numero
    print("El resultado es")
    print(resta)
def multiplication(n4_numero, n5_numero):
    multi = n4_numero * n5_numero
    print("El resultado es")
    print(resta)
def division(n6_numero, n7_numero):
    div = n6_numero / n7_numero
    print("El resultado es")
    print(div)
welcome_message()
menu_options()
num_operation()
opc = input("Marque la opcion de su operacion: ")
if int(opc) == 1:
    sum(numero, numero2)
elif int(opc) == 2:
    subtraction(numero, numero2)
elif int(opc) == 3:
    multiplication(numero, numero2)
elif int(opc) == 4:
    division(numero, numero2)
elif int(opc) > 4:
    print("El numero ingresado no es una opcion de operacion")
