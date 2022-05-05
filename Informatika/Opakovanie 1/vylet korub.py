import random
subor = open("studenti.txt","r",encoding = "UTF-8")
subor1= [x.replace("\n","") for x in subor]
chlapci= []
dievcata= []

for i in subor1:
    if i [-1]== "a":
        dievcata.append(i)
    else:
        chlapci.append(i)
dievcata.sort()
chlapci.sort()

print("Počet dievčat je:", len(dievcata))
print(dievcata)
print("Počet dievčat je:", len(chlapci))
print(chlapci)
print("zodpovedný za večerný program:",random.choice(chlapci), random.choice(dievcata))