def toon_aantal_kluizen_vrij():
    global aantal_kluizen
    print(aantal_kluizen, end="\n\n\n")
    file_reader.close()


def nieuw_kluis():
    global aantal_kluizen
    global file_reader
    global file_writer
    global file_lines
    code_check = False
    if aantal_kluizen > 0:
        kluizen_totaal = list(range(1, 13))
        for i in range(len(file_lines)):
            split_lines = file_lines[i].strip()
            split_lines = split_lines.split(";")
            if int(split_lines[0]) in kluizen_totaal:
                kluizen_totaal.remove(int(split_lines[0]))
        print("Je krijgt kluisnummer {}".format(kluizen_totaal[0]))
        while not code_check:
            code = str(input("Voer hier uw nieuwe minimaal 4-character lange code in: "))
            if len(code) >= 4:
                code_check = True
        file_reader.close()
        file_writer.write("\n{};{}".format(kluizen_totaal[0], code))
        file_writer.close()
        print("Je krijgt kluisje nummer: {} \n je passcode is: {}".format(kluizen_totaal[0], code))


def kluis_openen():
    return


def kluis_teruggeven():
    return


while True:
    file_reader = open(r"kluizen.txt", "r")
    file_writer = open(r"kluizen.txt", "a")
    file_lines = file_reader.readlines()
    aantal_kluizen = 12 - len(file_lines)

    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")
    menu_keuze = int(input())
    if menu_keuze == 1:
        toon_aantal_kluizen_vrij()
        break
    elif menu_keuze == 2:
        nieuw_kluis()
        break
    elif menu_keuze == 3:
        print("Je hebt drie gekozen")
    elif menu_keuze == 4:
        print("Je hebt 4 gekozen")
