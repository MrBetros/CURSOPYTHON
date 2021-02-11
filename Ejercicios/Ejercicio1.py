cal1 = input("Escribe tu primer calificacion: ");
cal2 = input("Escribe tu segunda calificacion: ");
cal3 = input("Escribe tu tercer calificacion: ");

suma = int(cal1) + int(cal2) + int(cal3);

promedio = suma / 3;

print("Tu promedio es:" + str(promedio));

if (promedio >= 6):
    print("Aprobado");
elif (promedio < 6):
    print("Reprobado");

