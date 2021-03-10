from variables import *

#Funktioner
def balance(): #Skapar funktionen 'balance' som kommer att till
    saldo = 0
    for t in transaktioner:
        saldo += t
    return saldo

def validate_int(output, error_mess):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

def print_transaktioner():
    line = 0
    balance = 0
    head = ("\nAlla Transaktioner:"
            "\n{:>3}. {:>12} {:>12}"
            "\n---------------------------").format("Nr", "Händelse", "Saldo")
    print(head)
    for t in transaktioner:
        line += 1
        balance += t
        print("{:>2}. {:>9} kr {:>9} kr".format(line, t, balance))

def check_file_exists():
    try:
        with open(filename, "a"):
            print("Filen 'konto' skapades")

        with open(filename, "b") as f:
            f.write("{}\n".format(1000))
    except:
        return

def read_file():
    check_file_exists()

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))

def add_transaction(transaktioner, toFile = False):
    if toFile:
        write_to_file(transaktioner)

def write_to_file(transaktioner):
    with open(filename, "a") as f:
        f.write("{}\n".format(transaktioner))