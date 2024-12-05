
# 01. ülessanne
# Anneli 05.12.24

# see impordib kilpkonna mooduli
import turtle

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

#süda
turtle.penup()
turtle.goto(-100,200)
turtle.pendown()
turtle.left(120)#lt, rt
turtle.fd(100)
turtle.circle(50,180)
turtle.right(90)
turtle.circle(50,180)
turtle.fd(100)


#lõpetab kilpkonna, et ei jookseks kokku
turtle.done()