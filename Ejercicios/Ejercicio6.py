from math import sqrt

print("Calculemos el valor de x con la Formula General.");

a = float(input("Inserta valor de a: "));
b = float(input("Inserta valor de b: "));
c = float(input("Inserta valor de c: "));

x1 = (-b+sqrt((b**2)-(4*a*c)))/(2*a);
x2 = (-b-sqrt((b**2)-(4*a*c)))/(2*a);

print("El valor de x1 es: " + str(x1));
print("El valor de x2 es: " + str(x2));