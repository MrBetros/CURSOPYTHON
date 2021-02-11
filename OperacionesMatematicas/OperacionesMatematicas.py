# Entradas de Datos
print("Escribe un numero: ");
num1 = input();
num2 = input("Escribe el siguiente numero: ");
# Operaciones Matematicas
# Suma
suma = float(num1) + float(num2);
# Resta
resta = float(num2) - float(num1);
# Multiplicacion
multiplicacion = float(num1) * float(num2);
# Division
division = float(num1) / float(num2);
# Potencia
potencia1 = float(num1) ** float(num2);
potencia2 = pow(float(num1), float(num2));
# Raiz
raizcuadrada = pow(float(num1), float(1/2));
raizcubica = pow(float(num2), float(1/3));
# Residuo o Moudulo
residuo = float(num1) % float(num2);
# Salida de Datos
print(suma);
print(resta);
print(multiplicacion);
print(division);
print(potencia1);
print(potencia2);
print(raizcuadrada);
print(raizcubica);
print(residuo);
# Nos dice que tipo de dato dinamico estamos manejando
print(type(suma));
