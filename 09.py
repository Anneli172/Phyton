# Ülessanne 09

# Genereeri ja kuva arvud arvud 1-20
# Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
for i in range(1,21):
    print(i, end=" ")
print()
import random
for i in range(1,21):
    print(f"{i}. ", end=" ")
    print(random.randint(1,99))
numbrid = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud = []
for nr in numbrid:
    if nr%2==0:
        paaris.append(nr)
    else:
        paaritud.append(nr)

print(paaris)
print(paaritud)

for i in range(1,43):
    if i%3==0 and i%5==0:
        print(f"{i} TIKTAK")
    elif i%5==0:
        print(f"{i} TAK")
    elif i%3==0:
        print(f"{i} TIK")
    else:
        print(i)

for i in range(1,6):     # tegin kolmnurga
    print(" "* i, end="")
    print("*" * (6-i))

# 13

ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]
ranges = []
#print(ev_data[0][0])

for autod in ev_data:
    print(f"{autod[0]:30} {autod[1]:5} {autod[2]:7} ")
    if autod[1].isnumeric():
        ranges.append(int(autod[1]))

print(f"Keskmine ulatus: {sum(ranges)/len(ranges)}")
for autod in ev_data:
    if autod[1].isnumeric():
        if int (autod[1]) > 300:
            print(autod[0])
            



    #for i in autod:
       # print(i)

    import turtle
    # joonistan esimese ruudu
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
        

    import turtle
    
    for _ in range(4):
        
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90) 
        turtle.forward(50)
        turtle.right(90)
        turtle.right(100)
        turtle.setheading(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)

        turtle.done()
        


        


    

    

    


    

