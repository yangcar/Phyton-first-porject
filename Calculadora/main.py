menu = " Marque 1 para sumar \n Marque 2 para restar \n Marque 3 para multiplicar \n Marque 4 para dividir"
print(menu)
numero=float(input("Ingrese el primer numero: "))
numero2=float(input("ingrese el segundo numero: "))

opc = input("Marque la opcion de su operacion: ")
if int(opc)==1:
       suma = numero + numero2
       print("La respuesta es:")
       print(suma)
elif int(opc)==2:
       resta = numero - numero2
       print("La respuesta es:")
       print(resta)
elif int(opc)==3:
       multi = numero * numero2
       print("La respuesta es:")
       print(multi)
elif int(opc)==4:
       div = numero / numero2
       print("La respuesta es:")
       print(div)
elif int(opc) > 4:
       print("El numero ingresado no es una opcion de operacion")
