print("Witaj w grze Bitwa Magów")
print("To gra w której walczysz za pomocą magi ze swoimi kolegami")
print("Miłej zabawy")
gracz1 = input("Gracz jeden podaj imie: ")
print("Witaj", gracz1)
gracz2 = input("Gracz dwa podaj imie: ")
print("Witaj", gracz2)
ZycieGracza1 = 50
ZycieGracza2 = 50
print("Runda 1", gracz1, "zaczyna") # Runda 1 garcz 1
ZaklecieGracz1Runda1 = input("Wybierz zaklęcie: Ognista kula - 10, Piorun Zeusa - 25, Leczenie - +5: ")
if ZaklecieGracz1Runda1 == "Ognista kula":
    ZycieGracza2 -= 10
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda1 == "Piorun Zeusa":
    ZycieGracza2 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda1 == "Leczenie":
    ZycieGracza1 += 5
    ZycieGracza2 -= 5
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Zły wybór")
print("Runda 1 kolej na gracza",gracz2)
ZaklecieGracz2Runda1 = input("Wybierz zaklęcie: Cienie nocy - 10, Kula Chaosu - 25, Leczenie - +5: ")
if ZaklecieGracz2Runda1 == "Cienie nocy":
    ZycieGracza1 -= 10
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda1 == "Kula chaosu":
    ZycieGracza1 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda1 == "Leczenie":
    ZycieGracza2 += 5
    ZycieGracza1 -= 5
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Zły wybór")
print("Pora na kolejną runde")
print("Runda 2",gracz1,"zaczyna")
ZaklecieGracz1Runda2 = input("Wybierz zaklęcie: Fala mrozu - 7, Ogien feniksa - 12, ")