# 3. Ülesanne
# Anneli 05.12.24

nimi= "Anneli" # sõne, string, str
vanus = 20 #int, integer, täisarv
keskmine_hinne = 4.5 #komaarv, float
print(nimi+", "+str(vanus)+" aastat vana ja keskmine_hinne on "+str(keskmine_hinne))

#lause vormindamine lünkadega
print(f"{nimi}, {vanus} aastat vana ja keskmine hinne om {keskmine_hinne}")

#3.7 kolmnurk
külje_pikkus =100
nurk = 120

turtle.speed(0) #reguleeri 1-9
turtle.penup()
turtle.goto(-500,200)
turtle.pendown()
turtle.forward(200) #fd, pikslites
turtle.left(120) #lt, rt
turtle.forward(200) #fd, pikslites
turtle.left(120) #lt, rt
turtle.forward(200) #fd, pikslites
turtle.left(120) #lt, rt



Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
Kasutades Turtle’i, joonista kõrvuti 3 värvilist kolmnurka, mis kasutab loodud muutujaid
Iga kolmnurk on järgmisest 1,5 korda eemal
Testi: muuda külje pikkust ning kolmnurgad on kenasti teineteisest eemal