# Tipos De Datos
print("Escribe tu Nombre: ");
#input nos permite hacer que el usuario coloque datos y esos sean los que se muestren al final
NombrePersona = str(input());
print("Escribe tu Edad: ");
Edad = input();
print("Escribe tu Sexo: ");
Sexo = str(input());
print("Escribe tu Telefono: ");
Telefono = input();
print("Escribe tu Peso: ");
Peso = str(input());
print("¿Te gusta dormir?: ");
LeGustaDormir = str(input());
#str nos sirve para castear el dato colocado
print("Nombre: " + NombrePersona);
print("Edad: " + str(Edad));
print("Sexo: " + Sexo);
print("Telefono: " + Telefono);
print("Peso: " + str(Peso));
print("Le Gusta Dormir: " + str(LeGustaDormir));
print("\n");
print(type(NombrePersona));
print(type(Edad));
print(type(Peso));


