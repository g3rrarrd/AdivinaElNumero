from Game import management

class main:
    mana = management.management()

    try:
        mana.generate_number()
        numero = int(input("Adivina el numero del 1 al 50: \n"))
        if numero < 1 or numero > 50:
            print("Fuera del rango")
        else:
            mana.play(numero)

        while True:
            try:
                numero = input("\nQuiere seguir jugando? \nType x for exit: ")
                if(numero == "x"):
                    print("\nEl numero era: %d" % mana.get_number())
                    print("Hasta pronto\n")
                    exit()
                else:
                    if 1< int(numero) > 50:
                        print("Fuera del rango")
                    else:
                        if mana.play(int(numero)) == True:
                            exit()
            except ValueError as v:
                print("Valor numerico no insertado")
    except ValueError as v:
                print("Valor numerico no insertado")
