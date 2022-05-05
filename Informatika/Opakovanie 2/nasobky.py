federacia=""

try:
    od= int(input("Zadaj od:"))
    do= int(input("Zadaj do:"))
    if od >30 or do>30:
        print("Zadal si príliš veľkú hodnotu")
    else:
        pr=od
        turbo=((do+1)-od)*4+4
        print("    ",end="")
        for i in range(od,do+1):
            print(f"{i:4}",end="")
        print()
        print("-"*turbo)
        for z in range(od,do+1):
            print(f"{z} -",end="")
            federacia+=str(z)+" - "
            for i in range(od, do+1):
                cislo= pr*i
                print(f"{cislo:4}",end="" )
                pocet=len(str(cislo))*" "
                federacia+=pocet+str(cislo)
            pr+=1
            print("")




except ValueError:
    print("Zadal si nečíselnú hodnotu")


