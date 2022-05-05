cislo= int(input("Zadaj prirodzené číslo v desiatkovej sústave:"))
bajt= int(input("Zadaj počet baijtov:"))

def decimal(cislo):
    zvysok=" "
    while cislo>0:
        c_cislo=cislo/2
        c1_cislo=cislo%2
        zvysok=str(int(c1_cislo))+zvysok
        cislo=c_cislo
        if len(zvysok)%9 ==0:
            zvysok=" " + zvysok
        if cislo<1:
            cislo=0
    while len(zvysok)<=bajt*9:
        zvysok="0"+ zvysok
        if len(zvysok)%9 ==0:
            zvysok=" " + zvysok

    print(zvysok)
decimal(cislo)
