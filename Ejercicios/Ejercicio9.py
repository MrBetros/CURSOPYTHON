dias = float(input("Dias trabajados: "));
horas = input("¿Trabajo horas extras? ");
nomina = (dias * 250) ;
prestaciones = nomina * float(.10);
nominaff = nomina - prestaciones;
if horas == 'si':
    extra = float(input("¿Cuantas horas extras trabajaste? "))
    final = extra * 31.25  
    nominaf = ((dias * 250) + float(final)) - float(prestaciones);
    print("Su nomina final es de: " + str(nominaf))
else:
    print("Su nomina es de: " + str(nominaff));
