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
print("El resultado de la suma es: " + str(suma));
print("El resultado de la resta es: " + str(resta));
print("El resultado de la multiplicacion es: " + str(multiplicacion));
print("El resultado de la division es: " + str(division));
print("El resultado de la potencia1 es: " + str(potencia1));
print("El resultado de la potencia2 es: " + str(potencia2));
print("El resultado de la raiz cuadrada es: " + str(raizcuadrada));
print("El resultado de la raiz cubica es: " + str(raizcubica));
print("El resultado del residuo es: " + str(residuo));
# Nos dice que tipo de dato dinamico estamos manejando
print(type(suma));
print(type(resta));
print(type(multiplicacion));
print(type(division));
print(type(potencia1));
print(type(potencia2));
print(type(raizcuadrada));
print(type(raizcubica));
print(type(residuo));