
# print("Tere, maailm!")

# # 1.2 Aasta liblikas

# aasta = 2020
# liblikas = "teelehe-mosaiikliblikas"
# lause_keskosa = ". aasta liblikas on "
# lause = str(aasta) + lause_keskosa + liblikas
# print(lause)

# 1.3 Pilved
# Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi pilvedeks. Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel, alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis
# küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
# väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
# väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
# Kasutaja peab saama sisestada pilvede kõrgust nii täisarvuna kui ka ujukomaarvuna, nt 7.5.

# korgus = float(input("Sisesta pilvede kõrgus: "))
# if korgus > 6:
#     print("Ülemised")                   
# elif korgus >= 2 and korgus <= 6:
#     print("Keskmised")
# else:
#     print("Alumised")

    

# 1.4 Bussid
# Testige oma programmi muuhulgas järgmiste algandmetega:
# inimeste arv: 60, kohtade arv: 40;
# inimeste arv: 80, kohtade arv: 40;
# inimeste arv: 20, kohtade arv: 40;
# inimeste arv: 40, kohtade arv: 40.

import math
inim = 90
koht = 40

jaak = inim%koht
if jaak>0:
    busside_arv = (inim//koht)+1
    
else:
    busside_arv = inim // koht
if jaak == 0:
    jaak = koht

print(f"Busside arv: {busside_arv}")
print(f"Viimases bussis on inimesi: {jaak}")

