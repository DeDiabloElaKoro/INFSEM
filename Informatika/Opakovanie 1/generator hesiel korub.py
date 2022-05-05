import random

def generuj_heslo(male,velke,cislo,znaky):
    male_p ="qwertzuiopasdfghjklyxcvbnm"
    velke_p ="QWERTZUIOPASDFGHJKLYXCVBNM"
    cislo_p ="0123456789"
    znaky_p= "+-*?:_-@#"
    znaky_heslo=""
    for i in range(male):
        znaky_heslo += random.choice(male_p)
    for i in range(velke):
        znaky_heslo += random.choice(velke_p)
    for f in range(cislo):
        znaky_heslo += random.choice(cislo_p)
    for f in range(znaky):
        znaky_heslo += random.choice(znaky_p)
    heslo = ""
    while len(znaky_heslo) > 0:
        i = random.randrange(len(znaky_heslo))
        heslo += znaky_heslo[i]
        znaky_heslo = znaky_heslo[:i] + znaky_heslo[i+1:]
    return heslo

m= int(input("Zadaj počet malých písmen"))
v= int(input("Zadaj počet veľkých písmen"))
c= int(input("Zadaj počet čísel"))
z= int(input("Zadaj počet znakov"))

for i in range(5):
    print(generuj_heslo(m,v,c,z))

