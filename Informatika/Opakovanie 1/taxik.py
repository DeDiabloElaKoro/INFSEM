subor = open("taxik.txt","a",encoding="UTF-8")
n=1
spolukm = 0
spolucena = 0
while n != 0:
        n = int(input("Zadaj počet prejdených km:"))
        if n < 10  and n  > 0:
            cena = n*0.5
        elif n > 11 and n < 20:
            cena = n*0.45
        elif n >21 and n < 30:
            cena = n*0.4
        elif n >31:
            cena = n*0.35
        spolukm += n
        spolucena += cena
        if n == 0:
            print("najazdené :",spolukm,"cena:",spolucena)
        else:
            print("Cena za", n ,"km je" ,cena,"€")
            subor.write(str(n)+"              ")
            subor.write(str(cena)+"\n")


