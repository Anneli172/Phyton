# Lisa võimalus, et ma saan sinu kuvatud andmetest otsida midagi ehk kasutad input'i ja if-lauset. 
# Valesti otsimisel kuvatakse ilus veateade.
import json

with open('posts.json', 'r', encoding='utf-8') as file: # laen faili
    posts = json.load(file)

    postitused = input("Sisesta otsingusõna sisu leidmiseks:"). lower()
    otsitav_marksona = input("Sisesta otsitav märksõna:"). lower() # sisestan otsitava väikeste tähtedega
    meeldimised = input("Sisesta postitus millele on rohkem like kui dislike(jah/ei):")
    found = False # vale sisestus
    for post in posts['posts']:
            title = post['title']. lower()
            if postitused in title:
                if otsitav_marksona in post['tags']:
                     if meeldimised == 'jah' and post['reactions']['likes'] > post['reactions']['dislikes']: # kandilised sulud on loend
                        print(f"Postitus ID: {post['id']}")  # {} väärtus
                        print(f"Pealkiri: {post['title']}")
                        print(f"Sisu: {post['body']}")
                        print(f"Märksõnad: {', '.join(post['tags'])}") # kirje ',' kuvab postituse märksõnad ühes reas
                        print(f"Meeldimised: {post['reactions']['likes']}")
                        print(f"Mittemeeldimised: {post['reactions']['dislikes']}")
                        print(f"Vaated: {post['views']}")
                        print("-" * 40)  # visuaalne eraldaja
                        found = True # õige sisestus
             
    if not found: # veateade
        print(f"Otsitav sõna '{postitused and otsitav_marksona}' ei leidnud postitust, proovige uuesti.")
    else:
        print(f"Otsitav sõna '{postitused and otsitav_marksona}' leiti ja postitused on kuvatud.")   