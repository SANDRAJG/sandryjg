DETERMINAR SI ES JOVEN O VIEJO UNA PERSONA.

while True:
    firstname = input("Cu�l es su primer nombre? ")
    lastname = input("Cu�l es su apellido? ")
    location = input("Cu�l es su direcci�n? ")
    age = input("Cu�l es su edad? ")
    x=int(age)
    space = " "
    print("Hola" + space + firstname + space + lastname + ", tienes" + space + age + space + "a�os y vives en" + space + location)
    if x > 1 and x <= 12:
        print("*** Usted es un ni�o")
    elif x > 12 and x <= 18:
        print("*** Usted es un adolescente")
    elif x > 18 and x <= 65:
        print("*** Usted es un adulto")
    else:
        print("*** Usted es un adulto mayor")
    salir = input("Desea salir? [S] o [N]")
    if salir == 'S':
        break
print ("Gracias")