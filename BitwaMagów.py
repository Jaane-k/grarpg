print("Witaj w grze Bitwa Magów")
print("To gra w której walczysz za pomocą magi ze swoimi kolegami")
print("Miłej zabawy")
gracz1 = input("Gracz jeden podaj imie: ")
print("Witaj", gracz1)
gracz2 = input("Gracz dwa podaj imie: ")
print("Witaj", gracz2)
ZycieGracza1 = 100
ZycieGracza2 = 100
print("Runda 1", gracz1, "zaczyna") # Runda 1 gracz 1
ZaklecieGracz1Runda1 = input("!!! ZAPISZ NUMEREM !!! Wybierz zaklęcie: 1 = Ognista kula - 20, 2 = Piorun Zeusa - 25, 3 = Kradzież życia - +15: ")
if ZaklecieGracz1Runda1 == "1":
    ZycieGracza2 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda1 == "2":
    ZycieGracza2 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda1 == "3":
    ZycieGracza1 += 15
    ZycieGracza2 -= 15
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Zły wybór, Tracisz ture")
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
print("Runda 1 kolej na gracza",gracz2) # Runda 1 gracz 2
ZaklecieGracz2Runda1 = input("!!! ZAPISZ NUMEREM !!! Wybierz zaklęcie: 1 = Cienie nocy - 20, 2 = Kula Chaosu - 25, 3 = Kradzierz życia - +15: ")
if ZaklecieGracz2Runda1 == "1":
    ZycieGracza1 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda1 == "2":
    ZycieGracza1 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda1 == "3":
    ZycieGracza2 += 15
    ZycieGracza1 -= 15
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Zły wybór, Tracisz ture")
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
print("Pora na runde 2")  # Runda 2 garcz 1
print("Powodzenia")
print("Runda 2",gracz1,"zaczyna")
ZaklecieGracz1Runda2 = input("!!! ZAPISZ NUMEREM !!! Wybierz zaklęcie: 1 = Fala mrozu - 20, 2 = Ogien feniksa - 25, 3 = Wir wody - 20, 4 = Kradzież życia - +15: ")
if ZaklecieGracz1Runda2 == "1":
    ZycieGracza2 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda2 == "2":
    ZycieGracza2 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda2 == "3":
    ZycieGracza2 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda2 == "4":
    ZycieGracza1 += 15
    ZycieGracza2 -= 15
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Zły wybór, Tracisz ture")
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
print("Runda 2 kolej na gracza",gracz2) # Runda 2 garcz 2
ZaklecieGracz2Runda2 = input("!!! ZAPISZ NUMEREM !!!  Wybierz zalęcie: 1 = Elektryczna strzała - 25, 2 Ognisty widelec - 20, 3 = Deszcz kamieni - 20, 4 = Kradzież życia - +15: ")
if ZaklecieGracz2Runda2 == "1":
    ZycieGracza1 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda2 == "2":
    ZycieGracza1 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda2 == "3":
    ZycieGracza1 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda2 == "4":
    ZycieGracza1 += 15
    ZycieGracza2 -= 15
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Zły wybór, Tracisz ture")
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
print("Czas na runde 3")
print("Będzie ostro uważaj na przeciwnika")
print("Powodzenia")
print("Zaczyna", gracz1) # Runda 3 garcz 1
ZaklecieGracz1Runda3 = input("!!! ZAPISZ NUMEREM !!!  Wybierz zalęcie: 1 =  Smoczy oddech - 20, 2 = Szpony ciemności - 25, 3 = Aura Natury - 20, 4 = Kradzież życia - +15: ") 
if ZaklecieGracz1Runda3 == "1":
    ZycieGracza2 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda3 == "2":
    ZycieGracza2 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda3 == "3":
    ZycieGracza2 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda3 == "4":
    ZycieGracza1 += 15
    ZycieGracza2 -= 15
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Zły wybór, Tracisz ture")
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
print("Runda 3 kolej na gracza", gracz2)
ZaklecieGracz2Runda3 = input("!!! ZAPISZ NUMEREM !!!  Wybierz zalęcie: 1 =  Astralna eksplozja - 20, 2 = Szpony smoka - 20, 3 = Aura Śmierci - 25, 4 = Kradzież życia - +15: ")
if ZaklecieGracz2Runda3 == "1":
    ZycieGracza1 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda3 == "2":
    ZycieGracza1 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda3 == "3":
    ZycieGracza1 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda3 == "4":
    ZycieGracza2 += 15
    ZycieGracza1 -= 15
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else: 
    print("Zły wybór, Tracisz ture")
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
print("Czas na runde 4")
print("Powodzenia")
print("Runda 4 zaczyna",gracz1)
ZaklecieGracz1Runda4 = input("!!! ZAPISZ NUMER !!! Wybierz zaklęcie: 1 = Mroźne ostrze - 25, 2 = Wiatr chaosu - 25, 3 = Wściekłość wulkanu - 20, 4 = Elektryczna eksplozja - 20, 5 = Kradzież życia - +15: ")
if ZaklecieGracz1Runda4 == "1":
    ZycieGracza2 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda4 == "2":
    ZycieGracza2 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda4 == "3":
    ZycieGracza2 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda4 == "4":
    ZycieGracza2 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz1Runda4 == "5":
    ZycieGracza2 += 15
    ZycieGracza1 -= 15
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Zły wybór, Tracisz ture")
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
ZaklecieGracz2Runda4 = input("!!! ZAPISZ NUMER !!! Wybierz zaklęcie: 1 = Anielski strumień - 20, 2 = Szkarłatny deszcz - 20, 3 = Strzały cieni - 25, 4 = Krwawe ostrza - 20, 5 = Kradzież życia - +15: ")
if ZaklecieGracz2Runda4 == "1":
    ZycieGracza1 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda4 == "2":
    ZycieGracza1 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda4 == "3":
    ZycieGracza1 -= 25
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda4 == "4":
    ZycieGracza1 -= 20
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
elif ZaklecieGracz2Runda4 == "5":
    ZycieGracza2 += 15
    ZycieGracza1 -= 15
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Zły wybór, Tacisz ture")
    print("Życie gracza",gracz1,"to",ZycieGracza1)
    print("Życie gracza",gracz2,"to",ZycieGracza2)
print("Czas na runde 5")
x = input("Czy chcesz kontynuować gre? Jeśli tak to napisz 1 jeśli nie 2: ")
if x == "1":
    ZaklecieGracz1Runda5 = input("!!! ZAPISZ NUMER !!! Wybierz zaklęcie: 1 = Kosmiczny Wyrzut - 25, 2 = Esencja wrzącej nocy - 50, 3 = Chaosowe szepty - 20, 4 = Burza kwiatów - 25, 5 = Kradzież życia - +15: ")
    if ZaklecieGracz1Runda5 == "1":
        ZycieGracza2 -= 25
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    elif ZaklecieGracz1Runda5 == "2":
        ZycieGracza2 -= 50
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    elif ZaklecieGracz1Runda5 == "3":
        ZycieGracza2 -= 20
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    elif ZaklecieGracz1Runda5 == "4":
        ZycieGracza2 -= 25
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    elif ZaklecieGracz1Runda5 == "5":
        ZycieGracza2 += 15
        ZycieGracza1 -= 15
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    else:
        print("Zły wybór, Tacisz ture")
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    print("Kolej gracza", gracz2)
    ZaklecieGracz2Runda5 = input("!!! ZAPISZ NUMER !!! Wybierz zaklęcie: 1 = Taniec wiatru - 25, 2 = Smocza energia chaosu - 50, 3 = Blask anioła - 20, 4 = Burza Smoka - 25, 5 = Kradzież życia - +15: ")
    if ZaklecieGracz2Runda5 == "1":
        ZycieGracza1 -= 25
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    elif ZaklecieGracz2Runda5 == "2":
        ZycieGracza1 -= 50
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    elif ZaklecieGracz2Runda5 == "3":
        ZycieGracza1 -= 20
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    elif ZaklecieGracz2Runda5 == "4":
        ZycieGracza1 -= 25
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    elif ZaklecieGracz2Runda5 == "5":
        ZycieGracza2 += 15
        ZycieGracza1 -= 15
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
    else:
        print("Zły wybór, Tacisz ture")
        print("Życie gracza",gracz1,"to",ZycieGracza1)
        print("Życie gracza",gracz2,"to",ZycieGracza2)
else:
    print("Pa")

if ZycieGracza1 > ZycieGracza2:
    print("Gratulacje graczu",gracz1,"jesteś prawdziwym mistrzem tej gry")
elif ZycieGracza2 < ZycieGracza1:
    print("Gratulacje graczu",gracz2,"jesteś prawdziwym mistrzem tej gry")
else:
    print("Remis!")
