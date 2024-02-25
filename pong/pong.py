# Importamos el módulo turtle para la interfaz gráfica y os para interactuar con el sistema operativo
import turtle as t
import os

# Inicializamos las puntuaciones de los jugadores
playerAscore=0
playerBscore=0

# Creamos la ventana del juego
window=t.Screen()
window.title("The pong game")  # Título de la ventana
window.bgcolor("green")  # Color de fondo
window.setup(width=800,height=600)  # Dimensiones de la ventana
window.tracer(0)  # Desactiva las actualizaciones de la ventana

# Creamos la paleta izquierda
leftpaddle=t.Turtle()
leftpaddle.speed(0)  # Velocidad de animación (0 es la más rápida)
leftpaddle.shape("square")  # Forma de la paleta
leftpaddle.color("white")  # Color de la paleta
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)  # Tamaño de la paleta
leftpaddle.penup()  # Desactiva el dibujo de la línea de seguimiento
leftpaddle.goto(-350,0)  # Posición inicial de la paleta

# Creamos la paleta derecha con las mismas características pero en una posición diferente
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

# Creamos la bola
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2  # Dirección inicial de la bola en el eje x
ballydirection=0.2  # Dirección inicial de la bola en el eje y

# Creamos el marcador
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()  # Oculta el objeto "turtle", sólo queremos el texto
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',24,'normal'))  # Escribe el texto inicial

# Definimos las funciones para mover las paletas
def leftpaddleup():
  y=leftpaddle.ycor()
  y=y+35
  leftpaddle.sety(y)

def leftpaddledown():
  y=leftpaddle.ycor()
  y=y-35
  leftpaddle.sety(y)

def rightpaddleup():
  y=rightpaddle.ycor()
  y=y+35
  rightpaddle.sety(y)

def rightpaddledown():
  y=rightpaddle.ycor()
  y=y-35
  rightpaddle.sety(y)

# Asociamos las funciones de movimiento con las teclas correspondientes
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

# Bucle principal del juego
while True:
  window.update()  # Actualiza la ventana

  # Mueve la bola
  ball.setx(ball.xcor()+ballxdirection)
  ball.sety(ball.ycor()+ballydirection)

  # Comprueba si la bola ha chocado con el borde superior o inferior y cambia su dirección
  if ball.ycor()>290:
    ball.sety(290)
    ballydirection=ballydirection*-1
  if ball.ycor()<-290:
    ball.sety(-290)
    ballydirection=ballydirection*-1

  # Comprueba si la bola ha chocado con el borde derecho y cambia su dirección
  # También actualiza la puntuación del jugador A y reproduce un sonido
  if ball.xcor() > 390:
    ball.goto(0,0)
    ballxdirection = ballxdirection * -1
    playerAscore = playerAscore + 1
    pen.clear()
    pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
    os.system("afplay wallhit.wav&")

  # Hace lo mismo para el borde izquierdo y el jugador B
  if(ball.xcor()) < -390: 
    ball.goto(0,0)
    ballxdirection = ballxdirection * -1
    playerBscore = playerBscore + 1
    pen.clear()
    pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
    os.system("afplay wallhit.wav&")

  # Comprueba si la bola ha chocado con la paleta derecha y cambia su dirección
  # También reproduce un sonido
  if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
    ball.setx(340)
    ballxdirection = ballxdirection * -1
    os.system("afplay paddle.wav&")

  # Hace lo mismo para la paleta izquierda
  if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
    ball.setx(-340)
    ballxdirection = ballxdirection * -1
    os.system("afplay paddle.wav&")