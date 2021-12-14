print("BIENVENIDO")
print("Ingrese su usuario y contraseña para validar")
print("Recuerde su usuario es su Email y su contraseña debe tener minimo 8 digitos")
def data_user():
    use = input("Ingese su usuario: ")
    return(use)
def data_password():
    con = input("ingrese su contraseña: ")
    return(con)


usuario=data_user()
contraseña=data_password()

def cont_password():
    cont=len(contraseña)
    return(cont)

contcon=cont_password()
def user():
    if usuario == "yang.gualteros@uptc.edu.co":
        print("Su usuario correcto")
    else :
        print("Su usuario no es correcto")

def pas():
    if contraseña=="yang1234":
        print("Contraseña correcta")
    elif contcon<8:
        print("Su contraseña tiene menos de 8 digitos Contraseña incorrecta")
    else :
        print ("contraseña incorrecta")

user()
pas()