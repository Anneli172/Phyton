import json

with open('books.json', 'r', encoding='utf-8') as file:
    books = json.load(file)
    otsitav_aasta = int(input("Sisesta aasta, mille raamatut otsid:"))
    if not any(book['published_year'] == otsitav_aasta for book in books):
        print(f"Ei leitud raamatut {otsitav_aasta}.")

    # Iga raamatu andmete väljastamine:
    for book in books:
        if book['published_year'] ==otsitav_aasta:
            title = book['title']
            author = book['author']
            published_year = book['published_year']
            copies_availlable = book['copies_available']

            print(f"Pealkiri: {title}")
            print(f"Autor:{author}")
            print(f"Avaldamisaasta: {published_year}")
            print(f"Saada olevad koopiad:{copies_availlable}")
            print("-"*40) # Visuaalne eraldaja

