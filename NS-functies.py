def standaardprijs(afstandKM):

    if afstandKM < 0:
        KMprijs = 0
    elif afstandKM <= 50:
        KMprijs = afstandKM * 80
    else:
        KMprijs = 1500 + 60 * (afstandKM - 50)
    return KMprijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    KMprijs = standaardprijs(afstandKM)
    if weekendrit and (leeftijd < 12 or leeftijd >= 65):
        KMprijs = KMprijs * 65 / 100
    elif weekendrit == False and (leeftijd < 12 or leeftijd >= 65):
        KMprijs = KMprijs * 70 / 100
    elif weekendrit:
        KMprijs = KMprijs * 60 / 100
    KMprijs_cent = int(KMprijs % 100)
    print(str(int(KMprijs / 100)), "euro en", str(KMprijs_cent), "cent voor een afgelegde afstand van", str(afstandKM), "km")


def ns_test():
    #leeftijd 11; variaties:
    print("\nTest met leeftijd 11")
    ritprijs(11, True, 31)
    ritprijs(11, False, 31)
    ritprijs(11, True, -10)
    ritprijs(11, False, -10)
    ritprijs(11, True, 70)
    ritprijs(11, False, 70)
    #leeftijd 12; variaties:
    print("\nTest met leeftijd 12")
    ritprijs(12, True, 42)
    ritprijs(12, False, 42)
    ritprijs(12, True, -96)
    ritprijs(12, False, -96)
    ritprijs(12, True, 80)
    ritprijs(12, False, 80)
    #leeftijd 64; variaties:
    print("\nTest met leeftijd 64")
    ritprijs(64, True, 45)
    ritprijs(64, False, 45)
    ritprijs(64, True, -1)
    ritprijs(64, False, -1)
    ritprijs(64, True, 60)
    ritprijs(64, False, 60)
    #leeftijd 65; variaties:
    print("\nTest met leeftijd 65")
    ritprijs(65, True, 18)
    ritprijs(65, False, 18)
    ritprijs(65, True, -990)
    ritprijs(65, False, -990)
    ritprijs(65, True, 98)
    ritprijs(65, False, 98)


keuze = int(input("Standaardtestprogramma(1)/zelf informatie invullen(2): "))
while True:
    if keuze == 1:
        ns_test()
        break
    elif keuze == 2:
        leeftijd = int(input("Hoe oud bent u: "))
        weekendrit = input("Is het een weekendrit (Ja/Nee): ")
        if weekendrit == "Ja":
            weekendrit = True
        elif weekendrit == "Nee":
            weekendrit = False
        else:
            print("Geef of 'Ja' of 'Nee' aan. Hoofdletters zijn belangrijk!")
            continue
        afstandKM = int(input("Hoeveel kilometer reist u: "))
        ritprijs(leeftijd, weekendrit, afstandKM)
        break
    else:
        print("Voer een geldig getal in.")
        break
