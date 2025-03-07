# Lisa võimalus, et ma saan sinu kuvatud andmetest otsida midagi ehk kasutad input'i ja if-lauset. 
# Valesti otsimisel kuvatakse ilus veateade.

import json

with open('comments.json', 'r', encoding='utf-8') as file:
    comments = json.load(file)["comments"]
    autor = input("Sisesta postitaja nimi:") 
    leitud_kommentaarid = [comment for comment in comments if comment.get('user', {}).get('fullName') == autor]
    
    if not leitud_kommentaarid:
        print(f"Ei leitud postitajat {autor}.")
    else:
        for comment in leitud_kommentaarid:
            if "body" in comment:
                # Kuvame kommentaari info
                print("--------Kommentaar-----")
                print(f"Kommentaari ID: {comment['id']}")
                print(f"Kommentaari sisu: {comment['body']}")
                print(f"Like'ide arv: {comment['likes']}")
                print(f"Postitaja nimi: {comment['user']['fullName']}")
                print(f"Postitaja kasutajanimi: {comment['user']['username']}")
                print(f"Postitaja ID: {comment['user']['id']}")
                print(f"Postitaja postituse ID: {comment['postId']}")
