# Definir una funcion
# Tarea a ejecutar (argumentos o parametros) puede revolver o retornar un valor.

def Saludo():
    print("Funcion en ejecucion...")

Saludo()

########################################

def Sumar(a, b):
    return a + b

suma = Sumar(1, 2)
print(suma)

#########################################

def CompararDosNumeros(x, y):
    if x > y:
        print(f"{x} es mayor a {y}");
    elif x < y:
        print(f"{x} es menor a {y}");
    else x = y:
        print(f"{x} es igual a {y}");

CompararDosNumeros(1, 7);

##########################################