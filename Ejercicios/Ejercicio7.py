nivela = float(input("Coloque el nivel del agua: "));

if (nivela < 0):
    print("Fuga en la Cisterna");
elif (nivela == 0):
    print("Endender Bomba de Agua.");
elif (nivela <= 1.99):
    print("Acelerar Bomba de Agua.");
elif (nivela <= 3.99):
    print("Bomba Trabajando.");
elif (nivela <= 5.99):
    print("Desacelerar Bomba.");
elif (nivela == 6):
    print("Apagar Bomba.");
elif (nivela > 6):
    print("Desbordamiento de Agua en Cisterna");