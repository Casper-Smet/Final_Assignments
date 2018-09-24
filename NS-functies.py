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
        KMprijs = KMprijs * 0.65
    elif weekendrit == False and (leeftijd < 12 or leeftijd >= 65):
        KMprijs = KMprijs * 0.7
    elif weekendrit:
        KMprijs = KMprijs * 0.6
    print(str(KMprijs) + " cent")


ritprijs(11, True, 30)