'''
NOTA: Estos comentarios no tienen acentos
Lo han contratado en un hospital. Usted debe construir una aplicacion.
Esta aplicacion debe informar las personas que ingresan asi:
ninos hasta 18 anios
adulto hasta 65 anios
adulto mayor mayor de 65 anios
'''

n = int(input("cuantas personas ingresan al hospital: "))
for i in range(n):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    if edad < 18:
        print("El paciente es un nino")
    elif edad < 65:
        print("El paciente es un adulto")
    else:
        print("El paciente es un adulto mayor")

    


