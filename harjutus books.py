import json

with open('books.json', 'r', encoding='utf-8') as file:
    books = json.load(file)
    # Iga raamatu andmete väljastamine:
    for book in books:
        title = book['title']
        author = book['author']
        published_year = book['published_year']
        copies_availlable = book['copies_available']

        print(f"Pealkiri: {title}")
        print(f"Autor:{author}")
        print(f"Avaldamisaasta: {published_year}")
        print(f"saada olevad koopiad:{copies_availlable}")
        print("-"*40) # Visuaalne eraldaja

        