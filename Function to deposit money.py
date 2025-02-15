# Defineeri funktsioon, mis haldab deposiite ja väljavõtteid
def konto_haldur(saldo, toiming, summa):
    # Kontrolli, kas tehing on deposiit
    if toiming == "deposiit":
        saldo += summa  # Lisa deposiidi summa kontole
    # Kontrolli, kas tehing on väljavõte ja kas piisab rahast kontol
    elif toiming == "valjavote" and summa <= saldo:
        saldo -= summa  # Vähenda väljavõtu summa kontolt
    else:
        # Kui tehinguks on väljavõte, aga raha on vähe, prindi veateade
        print("Tehing ei õnnestunud.")  # Raha ei piisanud
    return saldo  # Tagasta uuendatud saldo

# Algne saldo
saldo = 200
print(f"Algsaldo: {saldo}")  # Prindi algne saldo

# Tsükkel, mis küsib, kas kasutaja tahab veel tehingut teha
while True:
    # Küsib kasutajalt, millist tehingut teha (deposiit või väljavõte)
    toiming = input("Vali tehing (deposiit/valjavote): ").lower()  # Muudab sisendi väikeseks, et oleks ühtne

    # Kui sisestatud tehing on õige, tee vastav tehing
    if toiming in ["deposiit", "valjavote"]:
        # Küsib kasutajalt, kui palju raha teha
        summa = float(input("Kui palju raha teha? "))  # Muudab sisendi arvuks
        saldo = konto_haldur(saldo, toiming, summa)  # Kutsume välja funktsiooni ja uuendame saldot
        print(f"Uus saldo: {saldo}")  # Prindi uus saldo pärast tehingut
    else:
        # Kui sisestatud tehing on vale, teavitame kasutajat
        print("Vale sisend.")  # Vale sisend (ei ole deposiit ega väljavõte)

    # Küsi kasutajalt, kas ta tahab teha veel tehingu
    if input("Kas tahad teha veel tehingu? (jah/ei): ").lower() != "jah":
        # Kui kasutaja ei soovi jätkata, lõpeb tsükkel ja täname kasutajat
        print("Tänan, et kasutasite meie teenuseid!")  # Tänan kasutajat teenuse kasutamise eest
        break  # Lõpeta tsükkel ja lõpeta programm
