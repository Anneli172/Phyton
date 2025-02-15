mpalgad = 0

with open("palgad.txt") as fail:
    sisu = fail.readlines()
    for i in sisu:
        #print(i,end="")
       tykeldus = (i.split(","))
       print(tykeldus[3])
       if tykeldus[3]=="Mees":
            mpalgad+=float(tykeldus[6])
    print(f"Meeste palgad: {mpalgad:.2f}") # Meeste palgad kokku liidetud
    

