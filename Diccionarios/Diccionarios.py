#Respetar sintaxis
diccionario = { "Nombres": "Mario Alberto", "Correo Electronico": "zeroline1998@gmail.com", 
"Telefono": 5513387008, "Apellidos": "García Rodríguez", 
"Direccion": { "Calle": "Excursionistas Everest", "Numero": "M-229 L-2280" } };

print(diccionario["Nombres"]);
print(diccionario["Apellidos"]);
print(diccionario["Direccion"]);
print(diccionario["Correo Electronico"]);
print(diccionario["Telefono"]);

print("Claves(Keys):", diccionario.keys());
print("Valores(Values):", diccionario.values());