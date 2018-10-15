def inlezen_beginstation(stations):
    beginstation_input = str(input("Wat is je beginstation?\n"))
    while beginstation_input not in stations or beginstation_input == 'Maastricht':
        beginstation_input = str(input("Deze trein komt niet in {}. \n"
                                       "Wat is je beginstation?\n".format(beginstation_input)))
    return beginstation_input


def inlezen_eindstation(stations, beginstation):
    eindstation_input = str(input("Wat is je eindstation?\n"))
    while eindstation_input not in stations or not stations.index(eindstation_input) > stations.index(beginstation):
        eindstation_input = str(input("Deze trein komt niet in {}.\n"
                                      "Wat is je eindstation?\n".format(eindstation_input)))
    return eindstation_input


def omroepen_reis(stations, beginstation, eindstation):
    begin_index = stations.index(beginstation) + 1
    eind_index = stations.index(eindstation) + 1
    afstand = eind_index - begin_index
    prijs = afstand * 5
    print("\nHet beginstation {} is het {}e station in het traject.\n"
          "Het eindstation {} is het {}e station in het traject.\n"
          "De afstand bedraagt {} station(s).\n"
          "De prijs van het kaartje is {} euro.\n\n"
          "Jij stapt in de trein in {}".format(beginstation, begin_index,
                                                          eindstation, eind_index,
                                                          afstand, prijs, beginstation))
    for i in range(afstand-1):
        print(" - {}".format(stations[i+begin_index]))
    print("Jij stapt uit in: {}".format(eindstation))


stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam",
            "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel",
            "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven", "Weert",
            "Roermond", "Sittard", "Maastricht"]


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
