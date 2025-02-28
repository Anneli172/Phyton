import json

with open('carts.json', 'r', encoding='utf-8') as file:
    title =json.load(file)
    toote_nimi = input("Sisesta toote nimi:").lower()
    for cart in title['carts']:
            # Läbime kõik tooted igas ostukorvis
        for product in cart['products']:
                    # Otsing, kas toote nimi on sarnane
                if 'title' in product and 'id' in product and 'price' in product:
                    if toote_nimi in product["title"].lower():
                     found = True
                     print(f"Toote nimi: {product['title']}")
                     print(f"Toote kood: {product['id']}")
                     print(f"Hind: {product['price']}")
                     print(f"Allahindlus: {product['discountPercentage']}")
                     print(f"Hind peale allahindlust: {product['discountedTotal']}")
                     print(f"Saada olev kogus: {product['quantity']}")
                     print(f"Toote pilt: {product['thumbnail']}")
                     print("-" * 40)

        if not found:
            print(f"Toodet nimega'{title}' ei leitud.")
        


