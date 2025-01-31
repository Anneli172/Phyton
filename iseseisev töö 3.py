# fail = open("rebased.txt" , encoding="UTF-8")
# vastuvõetud =[]

# for rida in fail:
#    # print(rida, end="")
#     vastuvõetud.append(int(rida))


# fail.close()

# # aasta = 9
# # print(vastuvõetud[aasta-1])

# # aasta = input("Lisa aasta 2011-2019: ")
# print(vastuvõetud[int(aasta[3])-1])

# 3.3 Sissetulekud

# fail = open("konto.txt", encoding="UTF-8")


# for kirje in fail:

#     if float(kirje) > 0:
#         print(float(kirje), end="\n")

# fail.close()

# 3-4 Jukebox


# Ada tahab valida plaadiautomaadist laulu ja uurib, milliseid laule masin mängib. Muusikapalad on kirjas failis, kus iga laul on eraldi real.
# Programmi testimiseks kasutatakse järgmisi faile, mida võite salvestada või koostada ise mõne tekstiredaktoriga (nt Notepad):

# musa = "edm"
# fail = open(f"kaustanimi/{musa}.txt", encoding="UTF-8")

muusika = "edm.txt"
fail = open(muusika, encoding="UTF-8")

nr = 1
#Näita kõiki lugusid
for pala in fail:
    print(str(nr) + ". " + pala, end="")
    nr += 1

#Kuva valitud lugu
print()
valik = int(input("Vali lugu: "))
fail.seek(0)
#fail = open(muusika, encoding="UTF-8")
mangin = 1
for pala in fail:
    if valik == mangin:
        print(pala, end="")
    mangin += 1
fail.close()

