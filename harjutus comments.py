# Lisa võimalus, et ma saan sinu kuvatud andmetest otsida midagi ehk kasutad input'i ja if-lauset. 
# Valesti otsimisel kuvatakse ilus veateade.

import json

with open('comments.json', 'r', encoding='utf-8') as file:

     comments = json.load(file)["comments"]
     for comment in comments:
        if "body" in comment:

         if "username" in comment:
            
    
            print("--------Kommentaar-----")
        print (comment["body"])
        print (comment["id"])
        print (comment["likes"])
            