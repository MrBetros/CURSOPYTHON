num = int(input("Ingrese numero entero: "));
suma = 0
contador = 0

if num > 0:
    suma = suma + num
    contador += 1

while num > 0:
    try:
        num = int(input("Ingresa un numero entero:"))
        if num > 0:
            suma += num
            contador = contador + 1
    except:
        print("Dato invalido")

promedio = suma / contador  
print("Su promedio es: " + str(promedio));