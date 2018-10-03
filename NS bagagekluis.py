def toon_aantal_kluizen_vrij():
    global aantal_kluizen
    print(aantal_kluizen, end="\n\n\n")
    file_reader.close()


def nieuw_kluis():
    global aantal_kluizen
    global file_reader
    global file_appender
    global file_lines
    global split_lines
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
        file_appender.write("\n{};{}".format(kluizen_totaal[0], code))
        file_appender.close()
        print("Je krijgt kluisje nummer: {} \nje passcode is: {}".format(kluizen_totaal[0], code))
    else:
        print("Sorry! Er zijn 0 kluisjes beschikbaar")
        return

def kluis_openen():
    global file_lines
    global split_lines
    kluis_nummer = str(input("Voer kluisnummer in: "))
    while True:
        for i in range(len(file_lines)):
            split_lines = file_lines[i].strip()
            split_lines = split_lines.split(";")
            if kluis_nummer == split_lines[0]:
                kluis_code = str(input("Voer uw code in: "))
                if kluis_code == split_lines[1]:
                    print("U heeft toegang tot uw kluisje\n\n\n")
                    break
                else:
                    print("Dit wachtwoord of kluisnummer is incorrect. regel 46")
                    break
            else:
                print("Dit wachtwoord of kluisnummer is incorrect. regel 48\n\n\n")
                break
        file_reader.close()
        break


def kluis_teruggeven():
    global file_lines
    global split_lines
    kluis_nummer = str(input("Voer kluisnummer in: "))
    while True:
        for i in range(len(file_lines)):
            split_lines = file_lines[i].strip()
            split_lines = split_lines.split(";")
            if kluis_nummer == split_lines[0]:
                kluis_code = str(input("Voer uw code in: "))
                if kluis_code == split_lines[1]:
                    print("Uw kluisje is vrijgegeven.\n\n\n")
                    for i in range(len(file_lines)):
                        split_lines = file_lines[i].strip()
                        split_lines = split_lines.split(";")
                        if kluis_nummer != split_lines[0]:
                            file_writer = open(r"kluizen.txt", "w")
                            if i > 1:
                                recombined_lines += str("\n" + split_lines[0] + ";" + split_lines[1])
                            else:
                                recombined_lines = str(split_lines[0] + ";" + split_lines[1])
                            file_writer.write(recombined_lines)
                            print(recombined_lines )
                    break
                else:
                    print("Dit wachtwoord of kluisnummer is incorrect. regel 70")
            else:
                print("Dit wachtwoord of kluisnummer is incorrect. regel 72\n\n\n")

        file_reader.close()
        file_appender.close()
        #file_writer.close()
        break






while True:
    file_reader = open(r"kluizen.txt", "r")
    file_appender = open(r"kluizen.txt", "a")
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
        kluis_openen()
        break
    elif menu_keuze == 4:
        kluis_teruggeven()
