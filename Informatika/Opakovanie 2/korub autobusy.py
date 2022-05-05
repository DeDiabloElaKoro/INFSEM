with open("bus_vytazenost.txt", "r",encoding = "UTF-8") as file:
    riadky = file.readlines()

max_kapacita = int(riadky[0])
obsadenost_v_autobuse  = 0
stanice = []
obsadenie = []

for station_info in riadky[1:]:
    nastupujuci, vystupujuci, nazov_stanice = station_info.split(maxsplit=2)
    prichod = int(nastupujuci)
    odchod = int(vystupujuci)
    nazvy = str(nazov_stanice)
    stanice.append(nazvy.strip())
    obsadenost_v_autobuse += prichod
    obsadenost_v_autobuse -= odchod
    obsadenie.append(obsadenost_v_autobuse)
    if obsadenost_v_autobuse > max_kapacita:
        print("Autobus prekročil kapacitu na zástávke ",(nazov_stanice),end="")


print(f"Maximálna kapacita autobusu je {max_kapacita}")
print(f"Autobus zastavil na konečnej zastávke s počtom cestujúcich {obsadenost_v_autobuse}")
print("Počet staníc je ",len(stanice))
print("Maximálne prekročenie kapacity bolo o",max(obsadenie)-50)
print("Názvy staníc : ",','.join(map(str, stanice)))