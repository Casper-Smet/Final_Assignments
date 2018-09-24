def standaardprijs(afstandKM):

    if afstandKM < 0:
        KMprijs = 0

    elif afstandKM <= 50:
        KMprijs = afstandKM * 80
    else:
        KMprijs = 15 + 60 * (afstandKM - 50)
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
    print(str(int(KMprijs / 100)), " euro en ", str(KMprijs_cent), " cent")


ritprijs(11, True, 31)
ritprijs(14, False, 420)