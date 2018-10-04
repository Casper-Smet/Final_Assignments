def toon_aantal_kluizen_vrij():
    global aantal_kluizen
    print("er zijn nog", aantal_kluizen, "kluizen vrij.", end="\n\n\n")
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
        if aantal_kluizen < 12:
            file_appender.write("\n{};{}".format(kluizen_totaal[0], code))
        else:
            file_appender.write("{};{}".format(kluizen_totaal[0], code))
        file_appender.close()
        print("Je krijgt kluisje nummer: {} \nje passcode is: {}\n\n\n".format(kluizen_totaal[0], code))
    else:
        print("Sorry! Er zijn 0 kluisjes beschikbaar\n\n\n")
        return


def kluis_openen():
    global file_lines
    global split_lines
    kluis_nummer = str(input("Voer kluisnummer in: "))
    kluis_code = str(input("Voer uw code in: "))
    while True:
        kluis_check = False
        for i in range(len(file_lines)):
            split_lines = file_lines[i].strip()
            split_lines = split_lines.split(";")
            if kluis_nummer == split_lines[0]:
                if kluis_code == split_lines[1]:
                    print("U heeft toegang tot uw kluisje\n\n\n")
                    kluis_check = True
                    #debug print("regel49")
                    break
        if not kluis_check:
            print("Dit wachtwoord of kluisnummer is incorrect. \n\n\n")
        file_reader.close()
        break


def kluis_teruggeven():
    global file_lines
    global split_lines
    kluis_nummer = str(input("Voer kluisnummer in: "))
    kluis_code = str(input("Voer uw code in: "))
    while True:
        kluis_check = False
        for i in range(len(file_lines)):
            split_lines = file_lines[i].strip()
            split_lines = split_lines.split(";")
            if kluis_nummer == split_lines[0]:
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
                            # debug: print(recombined_lines)
                            file_writer.close()
                            kluis_check = True
                    break
        if not kluis_check:
            print("Dit wachtwoord of kluisnummer is incorrect. \n\n\n")
            #debug print("REGEL 90")
        file_reader.close()
        file_appender.close()
        break


while True:
    file_appender = open(r"kluizen.txt", "a")
    file_reader = open(r"kluizen.txt", "r")
    file_lines = file_reader.readlines()
    aantal_kluizen = 12 - len(file_lines)
    try:
        print("="*46)
        print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
        print("2: Ik wil een nieuwe kluis")
        print("3: Ik wil even iets uit mijn kluis halen")
        print("4: Ik geef mijn kluis terug")
        print("5: Help, haal me uit deze loop!")
        print("="*46)
        menu_keuze = 0
        menu_keuze = int(input())
    except ValueError:
        print("Voer een geldige waarde in.")
    if menu_keuze > 5 or menu_keuze < 1:
        print("Voer een geldige waarde in")
    elif menu_keuze == 1:
        toon_aantal_kluizen_vrij()
    elif menu_keuze == 2:
        nieuw_kluis()
    elif menu_keuze == 3:
        kluis_openen()
    elif menu_keuze == 4:
        kluis_teruggeven()
    elif menu_keuze == 5:
        print("Fijne dag")
        break
