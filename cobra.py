#Nome:Victor de Araújo
import turtle
import time
import random

segs=[]
atraso=0.1
#Placar
Pontos=0
Recorde=0
#Tela
T=turtle.Screen()
T.title("COBRA KAI")
T.bgcolor("black")
T.bgpic("snake.png")
T.setup(width=600,height=600)
T.tracer(0)

#Cabeça da Cobra
cab=turtle.Turtle()
cab.speed(0)
cab.shape("circle")
cab.color("green")
cab.penup()
cab.goto(0,0)
cab.direction= "stop"

#Comida
comida= turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)


#caneta
caneta= turtle.Turtle()
caneta.speed(0)
caneta.shape("square")
caneta.color("yellow")
caneta.penup()
caneta.hideturtle()
caneta.goto(0,260)
caneta.write("PONTOS: 0  RECORDE: 0",align="center",font=("Courier",20,"normal"))

#funções
def go_up():
    if cab.direction!= "down":
      cab.direction= "up"
def go_down():
    if cab.direction!= "up":
      cab.direction= "down"
def go_left():
    if cab.direction!= "right":
      cab.direction= "left"
def go_right():
    if cab.direction!= "left":
      cab.direction= "right"
def move():
    if cab.direction== "up":
      y=cab.ycor()
      cab.sety(y+20)
    if cab.direction== "down":
      y=cab.ycor()
      cab.sety(y-20)
    if cab.direction== "left":
      x=cab.xcor()
      #ligações com as teclas
      cab.setx(x-20)
    if cab.direction== "right":
      x=cab.xcor()
      cab.setx(x+20)

T.listen()
T.onkeypress(go_up, "Up")
T.onkeypress(go_down, "Down")
T.onkeypress(go_left, "Left")
T.onkeypress(go_right, "Right")

#loop do Jogo
while True:
    T.update()
    #verificação de colisão com a borda
    if cab.xcor()>280 or cab.xcor()<-280 or cab.ycor()>280 or cab.ycor()<-280:
      time.sleep(1)
      cab.goto(0,0)
      cab.direction= "stop"
      #segmentos ocultos
      for seg in segs:
        seg.goto(1000,1000)
        #limpa os segmentos
        segs.clear()
        #redefinição dos pontos
        Pontos=0
        #redefinição de atraso
        atraso=0.1
        caneta.clear()
        caneta.write("PONTOS: {}  RECORDE: {}".format(Pontos, Recorde),align="center",font=("Courier",20,"normal"))
    #verificação de colisão com a comida
    if cab.distance(comida)<20:
      x=random.randint(-280,280)
      y=random.randint(-280,280)
      comida.goto(x,y)
      #adicona novos segmentos
      novoseg=turtle.Turtle()
      novoseg.speed(0)
      novoseg.shape("circle")
      novoseg.color("green")
      novoseg.penup()
      segs.append(novoseg)
      #encurtar o atraso
      atraso-=0.001
      #Aumetar a pontuação
      Pontos+=10
      if Pontos>Recorde:
        Recorde=Pontos
      caneta.clear()
      caneta.write("PONTOS: {}  RECORDE: {}".format(Pontos, Recorde),align="center",font=("Courier",20,"normal"))
    #movendo os segmentos na orden inversa
    for indice in range(len(segs)-1,0,-1):
      x=segs[indice-1].xcor()
      y=segs[indice-1].ycor()
      segs[indice].goto(x,y)
    #movendo o segmento zero para direção da cabeça
    if len(segs)>0:
      x=cab.xcor()
      y=cab.ycor()
      segs[0].goto(x,y)
    move()
    #verificação da colisão entre a cabeça e corpo
    for seg in segs:
      if seg.distance(cab)<20:
        time.sleep(1)
        cab.goto(0,0)
        cab.direction= "stop"
        #segmentos ocultos
        for seg in segs:
          seg.goto(1000,1000)
          #limpar segmentos
          segs.clear()
          #redifinição dos pontos
          Pontos=0
          #redifinição de atraso
          atraso=0.1
          #Atualização dos pontos
          caneta.clear()
          caneta.write("PONTOS: {}  RECORDE: {}".format(Pontos,Recorde),align="center",font=("Courier",20,"normal"))
    time.sleep(atraso)
T.mainloop()
