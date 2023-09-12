from turtle import *

v = 90 #скорость черепашки
step = 15 #шаг

t = Turtle() #создание объекта черепаха
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(v)

def draw(x, y): #функция обработчик события “перетаскивание” черепахи
  t.goto(x, y)

def move(x, y): #функция обработчик события клик на экран
  t.penup()
  t.goto(x, y)
  t.pendown()

def setRed(): #функция обработчик события нажатия клавиши, изменение цвета
    t.color('red')
ф
def setBlue():
    t.color('blue')

def setGreen():
    t.color('green')

def setYellow():
    t.color('yellow')

def setViolet():
    t.color('violet')

def setPink():
    t.color('pink')
    
def setOrange():
    t.color('orange')

def setBlack():
    t.color('black')


def stepUp(): #функция обработчик события нажатия клавиши, движение вверх
    t.goto(t.xcor(), t.ycor() + step)

def stepDown():
    t.goto(t.xcor(), t.ycor() - step)

def stepRight():
    t.goto(t.xcor() + step, t.ycor())

def stepLeft():
    t.goto(t.xcor() - step, t.ycor())

def startFill():
    t.begin_fill()
def endFill():
    t.end_fill()


t.ondrag(draw)   # подписка на событие перетаскивание черепахи
scr = t.getscreen()   # создание объекта “экран”, по которому перемещается черепаха
scr.onscreenclick(move)# подписка на событие “клик по экрану”
scr.onkey(setRed,'r') 
scr.onkey(setBlue, 'b')# подписка на событие “нажатие клавиши”, изменение цвета 
scr.onkey(setGreen, 'g')
scr.onkey(setOrange, 'o')
scr.onkey(setViolet, 'v')
scr.onkey(setBlack, 'l')
scr.onkey(setPink, 'p')
scr.onkey(setYellow, 'y')
scr.onkey(stepUp,'Up')
scr.onkey(stepDown, 'Down') # подписка на событие “нажатие клавиши”, движение вверх
scr.onkey(stepRight, 'Right')
scr.onkey(stepLeft, 'Left')
scr.onkey(startFill, 'e')
scr.onkey(endFill, 't')

scr.listen() # Команда “слушать клавиатуру”, без нее события клавиатуры не будут работать 
