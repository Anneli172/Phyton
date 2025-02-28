# Lisa võimalus, et ma saan sinu kuvatud andmetest otsida midagi ehk kasutad input'i ja if-lauset. 
# Valesti otsimisel kuvatakse ilus veateade.

import json

# laadin JSON faili
with open('carts.json', 'r', encoding='utf-8') as file:
    tooted = json.load(file) # muutuja millele väärtustakase kogu faili sisu
# küsime mida otsida
    pealkiri = input("Sisesta toote pealkiri, mida otsida: ").lower()  # Otsingusõna, muudetakse väiketähtedeks
    tootekood = input("Sisesta tootekood:")
# saab väärtuse mille sisestan
# Muutujad, et hoida otsingutulemusi
# Soovin hinnavahemiku otsida
try:
    min_hind = float(input("Sisesta minimaalne hind:"))
    max_hind = float(input("Sisesta max hind:"))
except:
    print("Vigane sisend! Sisesta hind numbrina.")
    exit()

    found = False  # kas toode leiti või mitte

# läbime kõik ostukorvid
for cart in tooted['carts']:
    for product in cart['products']:
        title = product['title'].lower()  # muudetakse pealkiri väiketähtedeks
        hind = product['price']
        tootekood = product['id']
        if pealkiri in title and min_hind <=hind <= max_hind:  # kui otsingusõna leidub pealkirjas
        
            print(f"Toode: {product['title']}")
            print(f"Tootekood: {product['id']}")
            print(f"Hind: {product['price']} EUR")
            print(f"Kogus: {product['quantity']}")
            print(f"Allahindlus: {product['discountPercentage']}%")
            print(f"Allahindlusega hind: {product['discountedTotal']} EUR")
            print(f"Garantiiteave:{product['warrantyInformation']}")
            print("Tarneinfo: {product['shippingInformation]}")
            print(f"Saadavus: {product['availabilityStatus']}")
            print(f"Thumbnail: {product['thumbnail']}")
            print("-" * 40)  # visuaalne eraldaja
            found = True

# kui toode ei leitud, kuvame veateate
        if not found:
            print("Toode ei leitud. Palun kontrollige, kas olete õigesti kirjutanud või proovige uuesti.")
