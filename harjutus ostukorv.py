import json

with open('carts.json', 'r', encoding='utf-8') as file:
    andmed = json.load(file)

def otsi_toode(otsingusõna):
    leitud = False
    print(f"Otsin: apple{otsingusõna}")
    
    for ostukorv in andmed["carts"]:
        print(f"Kontrollin ostukorvi ID: {ostukorv['id']}")
        for toode in ostukorv["products"]:
            if otsingusõna.lower() in toode["title"].lower():
                leitud = True
                print("-" * 50)
                print(f"Leitud vaste ostukorvis {ostukorv['id']}:")
                print(f"Toode: {toode['title']}")
                print(f"Hind: ${toode['price']:.2f}")
                print(f"Kogus: {toode['quantity']}")
                print(f"Kokku: ${toode['total']:.2f}")
                print(f"Allahindlus: {toode['discountPercentage']}%")
                print(f"Allahinnatud kokku: ${toode['discountedTotal']:.2f}")
                print("-" * 50)
    
    if not leitud:
        print("+" * 50)
        print("Vabandust! Ei leitud ühtegi toodet, mis vastaks '{otsingusõna}'.")
        print("Palun proovi uuesti mõne teise otsingusõnaga.")
        print("Soovitused:")
        print("- Kontrolli õigekirja")
        print("- Veendu, et toode on ostukorvis olemas")
        print("+" * 50)

# Põhiprogramm
while True:
    otsingu_sisend = input("Sisesta toote nimi otsimiseks (või 'välju' lõpetamiseks): ")
    
    if otsingu_sisend.lower() == 'välju':
        print("Nägemist!")
        break
    
    if otsingu_sisend.strip() == "":
        print("Viga: Palun sisesta otsingusõna!")
        continue
    
    otsi_toode(otsingu_sisend)