import turtle

# Loo turtle objekt
#t = turtle.Turtle()
külje_pikkus = int(input("Sisesta ruudu küljepikkus: "))
# Joonista ruut
for _ in range(2):
    for _ in range(4):
        turtle.forward(külje_pikkus)  # Liigu edasi 100 ühikut
        turtle.left(90)      # Pööra vasakule 90 kraadi

 
    
    turtle.penup()  # Tõsta pliiats üles, et mitte joonistada
    turtle.goto(külje_pikkus/2,külje_pikkus/2)  # Liigu natuke edasi, et ruudud ei kattuks
    turtle.pendown()  # Langeta pliiats tagasi


# Lõpeta
turtle.done()


