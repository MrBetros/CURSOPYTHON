dias = int(input("¿Cuantos dias trabajaste?: "));
pagoxd = 250;
pagob = dias * pagoxd;
ivat = pagob * float(.16);
sub = pagob + ivat;
ivar = ivat * (2/3);
ISRr = pagob * float(.10);
pagon = (float(pagob) + float(ivat)) - (float(ivar) + float(ISRr));
print("Su pago bruto es de: " + str(pagob));
print("El IVA transladado es de: " + str(ivat));
print("Subtotal: " + str(sub));
print("El IVA retenido es de: " + str(ivar));
print("El ISR retenido es de: " + str(ISRr));
print("Su pago neto es de: " + str(pagon));