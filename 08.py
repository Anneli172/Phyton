# Ülessanne 07
# 19.12.2024
# Anneli Tikerber

nimi = ["Jyri Pootsman", "Mari Jyrgens", "ans Juuli","Maali band"]
# for i in nimi:
# 		print(i)

for i in range(4):
    print (f"{i+1}. {nimi[i]}")
valik = int(input("Vali lugu(1-5):"))
print(f"Mängin: {nimi[valik-1]}")