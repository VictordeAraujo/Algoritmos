#Jogo Pong
#Nome:Victor de Araújo
from turtle import Turtle, Screen
from random import randint, choice

bolaspeed = 10
jogadorspeed = 50

cursor_size = 20
jogador_height = 100
jogador_width = 20

court_width = 1000
court_height = 600

FONT=("Arial", 44, "normal")

def draw_borda():
    borda.pensize(3)
    borda.penup()
    borda.setposition(-court_width/2, court_height/2)
    borda.pendown()
    borda.forward(court_width)
    borda.penup()
    borda.sety(-court_height/2)
    borda.pendown()
    borda.backward(court_width)

def filet():
    borda.penup()
    borda.pensize(1)
    borda.setposition(0,-court_height/2)
    borda.setheading(90)
    borda.pendown()

    for _ in range(court_height//50):
        borda.forward(50/2+1)
        borda.penup()
        borda.forward(50/2+1)
        borda.pendown()

def up1():
    y = jogador1.ycor()
    y += jogadorspeed
    if y < court_height/2 - jogador_height/2:
        jogador1.sety(y)

def down1():
    y = jogador1.ycor()
    y -= jogadorspeed
    if y > jogador_height/2 - court_height/2:
        jogador1.sety(y)

def up2():
    y = jogador2.ycor()
    y += jogadorspeed
    if y < court_height/2 - jogador_height/2:
        jogador2.sety(y)

def down2():
    y = jogador2.ycor()
    y -= jogadorspeed
    if y > jogador_height/2 - court_height/2:
        jogador2.sety(y)

def reset_bola():
    bola.setposition(0, 0)
    bola.setheading(choice([0, 180]) + randint(-60, 60))

def distance(t1, t2):
    my_distance = t1.distance(t2)

    if my_distance < jogador_height/2:
        t2.setheading(180 - t2.heading())
        t2.forward(bolaspeed)

def move():
    global placar1, placar2
    bola.forward(bolaspeed)
    x,y= bola.position()
    if x>court_width/2+cursor_size:
        placar1+=1
        p1.undo()
        p1.write(placar1, font=FONT)
        reset_bola()
        if placar1==3:
          print(placar1)
    elif x<cursor_size-court_width/2:
        placar2+=1
        p2.undo()
        p2.write(placar2, font=FONT)
        reset_bola()
        if placar2==3:
          print(placar2)
    elif y > court_height/2 - cursor_size or y < cursor_size - court_height/2:
        bola.setheading(-bola.heading())
    else:
        distance(jogador1,bola)
        distance(jogador2,bola)
    screen.ontimer(move, 20)

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1.0, height=1.0)

borda = Turtle(visible=False)
borda.speed('fastest')
borda.color("white")

draw_borda()
filet()

bola = Turtle("circle")
bola.color("white")
bola.penup()
bola.speed("fastest")

reset_bola()

jogador1 = Turtle("square")
jogador1.turtlesize(jogador_height / cursor_size, jogador_width / cursor_size)
jogador1.color("blue")
jogador1.penup()
jogador1.setx(cursor_size - court_width/2)
jogador1.speed("fastest")

jogador2 = Turtle("square")
jogador2.shapesize(jogador_height / cursor_size, jogador_width / cursor_size)
jogador2.color("white")
jogador2.penup()
jogador2.setx(court_width/2 + cursor_size)
jogador2.speed("fastest")

placar1= 0
p1 = Turtle(visible=False)
p1.speed("fastest")
p1.color("blue")
p1.penup()
p1.setposition(-court_width/4, court_height/3)
p1.write(placar1, font=FONT)

placar2= 0
p2 = Turtle(visible=False)
p2.speed("fastest")
p2.color("white")
p2.penup()
p2.setposition(court_width/4, court_height/3)
p2.write(placar2, font=FONT)

screen.onkey(up1, "q")
screen.onkey(down1, "a")

screen.onkey(up2, "Up")
screen.onkey(down2, "Down")

screen.onkey(reset_bola, "r")

screen.listen()

move()
screen.mainloop()
