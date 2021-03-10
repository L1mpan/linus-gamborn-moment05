from functions import *         # importar functions så att de går att kalla här i filen där programmet körs
read_file()                     # kallar på funktionen read_file vid start av koden, vilket kollar om det finns någon transaktion i filen konto.txt
                                # ifall det inte skulle finnas något i filen så printas 1000 ut som grundläggande transaktion
#Programmet
while True:                                                # while loopen för programmet
    meny = (
        "\n##########################"                     # meny
        "\n# Lilla banken"                                 # -
        "\n# Ditt saldo: {} kr"                            # -
        "\n##########################"                     # -
        "\n1. Visa transaktioner"                          # -
        "\n2. Gör en insättning"                           # -
        "\n3. Göt ett uttag"                               # -
        "\n0. Avsluta programmet"                          # -
        "\nGör ditt val: ").format(balance())              # meny
    val = validate_int(meny, "Felaktig inmatning")         # kollar så att man inte matar in ett decimaltal, negativt tal eller string.

    if val == 0:                                           # avbryter programmet om man valde 0 i menyn
        break

    elif val == 1:
        line = 0
        saldo = 0
        head = ("\nAlla Transaktioner:"
                "\n{:>3}. {:>12} {:>12}"
                "\n---------------------------").format("Nr", "Händelse", "Saldo")
                
        print(head)                             # denna delen kommer att printa ut 'head' som består utav 3 strings

        for t in transaktioner:                 
            line += 1                           # kommer att räkna vilket nummer transaktionen har
            saldo += t                          # kommer att tilldela den transaktionen som precis gjordes till variabeln 'saldo'
            print("{:>2}. {:>9} kr {:>9} kr".format(line, t, saldo))    #prinar line, transaktionen, saldot

    elif val == 2:
        deposit = validate_int("Ange hur mycket pengar du vill sätta in: ", "Felaktigt belopp") # frågar användaren om ett värde de vill sätta in, om användaren matar in ett ogiltigt värde så går den tillbaka till start menyn
        if deposit > 0:                                                                         # ifall värdet är över 0 kommer transaktionen att skickas till konto.txt
            transaktioner.append(deposit)                                                       # kommer appenda då man gör en transaktion
            add_transaction(transaktioner, True)                                                # kallar på funktionen 'add_transaction' som i slutet kommer att skriva till filen 'konto.txt'
        else:                                                                                   
            print("En insättning måste vara större än 0.")                                      # felmeddelande

    elif val == 3:
        withdraw = validate_int("Ange hur mycket pengar du vill ta ut: ", "Felaktigt belopp")   # frågar användaren om ett värde de vill ta ut, om användaren matar in ett ogiltigt värde så går den tillbaka till start menyn
        if withdraw <= balance() and withdraw >= 0:                                             # kollar så att man inte kan ta ut mer pengar än vad som finns och så att man matar in 0 eller ett negativt tal
            transaktioner.append(-withdraw)                                                     # kommer appenda då man gör en transaktion
            add_transaction(transaktioner, True)                                                # kallar på funktionen 'add_transaction' som i slutet kommer att skriva till filen 'konto.txt'
        elif withdraw < 0:
            print("Ett uttagande måste vara större än 0.")                                      # felmeddelande
        else:
            print("Uttaget får inte vara större än saldot.")                                    # felmeddelande

    else:
        print("felaktigt val!")                                                                 # felmeddelande


print("Tack för ditt besök, välkommen åter")                                                    # printas då while loopen stoppar, vilket är då man väljer 0 i menyn