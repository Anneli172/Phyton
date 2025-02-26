# PANGAKONTO
# Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt. Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone:
# deposiit (raha lisamine)
# väljavõte (raha eemaldamine)
# Tagastage peale igat toimingut konto jääk .
# Funtsiooni parameetrid:
# algne_saldo: algse saldo väärtus
# toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote')
# summa: summa, mida soovitakse lisada või eemaldada

def konto_haldur(algsaldo, toiming, summa):

    if toiming =="deposiit":
        algsaldo += summa
    elif toiming =="valjavote":
        if summa <= algsaldo:
            algsaldo -= summa
        else:
         print("Ei ole piisavalt raha kontol.")
        
    else:
        print("Makse ei õnnestunud.")
    return algsaldo
   
saldo = 100
print("Algsaldo:", saldo)
toiming = input("Vali toiming(deposiit/valjavote):").lower()
summa = float(input("Sisesta summa:"))

saldo = konto_haldur(saldo, toiming, summa)
print(f"Uus saldo pärast {toiming}: {saldo}")

toiming = input("Vali järgmine toiming (deposiit/valjavote): ").lower()
summa = float(input("Sisesta summa: "))

saldo = konto_haldur(saldo, toiming, summa)
print(f"Uus saldo pärast {toiming}: {saldo}")

# saldo = konto_haldur(saldo, "valjavote", 20)
# print("Uus saldo pärast väljavõtet:", saldo)

# saldo = konto_haldur(saldo, "valjavote", 150)
# print("Uus saldo peale raha liikumist:", saldo)