grados = input("Escribe la Inicial de la Escala (Mayus): ");

if (grados == "C"):
    gradosc = input("Coloca los grados Celsius: ");

    ke = float(gradosc) + float(273.15);
    fah = (float(gradosc) * float(1.8)) + 32;

    print("Grados Celsius: " + str(gradosc));
    print("Grados Kelvin: " + str(ke));
    print("Grados Fahrenheit: " + str(fah));
elif (grados == "F"):
    gradosf = input("Coloca los grados Fahrenheit: ");

    cel = (float(gradosf) - float(32)) / float(1.8);
    kel = (float(gradosf) - float(32)) * (float(5) / float(9)) + float(273.15);

    print("Grados Celsius: " + str(cel));
    print("Grados Kelvin: " + str(kel));
    print("Grados Fahrenheit: " + str(gradosf));
elif (grados == "K"):
    gradosk = input("Coloca los grados Kelvin: ");

    cels = float(gradosk) - float(273.15);
    fahr = (float(gradosk) - float(273.15)) * (float(9) / float(5)) + float(32);

    print("Grados Celsius: " + str(cels));
    print("Grados Kelvin: " + str(gradosk));
    print("Grados Fahrenheit: " + str(fahr));

