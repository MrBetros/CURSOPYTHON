rango = int(input("Coloca un numero: "));

if rango < 0 and rango > -100:
    for rango in range(-101, 0):
        if rango % 2 != 0:
            print(rango)
elif rango > 0 and rango < 101:
    for rango in range(0, 101):
        if rango % 2 ==0:
            print(rango)
else:
    print("No valido.");


