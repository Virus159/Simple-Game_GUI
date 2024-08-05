from turtle import *
import math
import random

screen = Screen()
myPen = Turtle()

screen.title("Turtle Game")
myPen.speed(10)

screen.bgcolor("#77E4C8")
myPen.shape("square")
myPen.shapesize(0.7)
myPen.pensize(3)
myPen.penup()
myPen.goto(-250, -250)
myPen.pendown()
myPen.pencolor("#00224D")

for i in range(4):
    myPen.fd(500)
    myPen.lt(90)
myPen.hideturtle()

player = Turtle()
player.penup()
player.home()
player.shape("classic")
player.color("#0E46A3")
player.speed(0)
speedo = 1

# Create a list to store enemies
enemies = []

# Create enemies and add them to the list
enemy_shapes = ["circle", "square", "triangle"]
enemy_colors = ["violet", "red", "blue"]
enemy_positions = [(0, -55), (0, 55), (0, 75)]

for shape, color, position in zip(enemy_shapes, enemy_colors, enemy_positions):
    enemy = Turtle()
    enemy.penup()
    enemy.goto(position)
    enemy.shape(shape)
    enemy.shapesize(4)
    enemy.shapesize(.8)
    enemy.color(color)
    enemy.speed(0)
    enemies.append(enemy)

def turn_left():
    player.lt(90)

def turn_right():
    player.rt(90)

def run():
    global speedo
    speedo += 1

def slowed():
    global speedo
    speedo -= 1

score = 0
t = Turtle()
t.hideturtle()

def move():
    global score
    player.fd(speedo)
    screen.ontimer(move, 20)
    if player.xcor() < -240 or player.xcor() > 240:
        player.lt(180)
    if player.ycor() < -240 or player.ycor() > 240:
        player.lt(180)
    
    for enemy in enemies:
        d = math.dist((player.xcor(), player.ycor()), (enemy.xcor(), enemy.ycor()))
        if d < 20:
            enemy.setpos(random.randint(-240, 240), random.randint(-240, 240))
            score += 1
            t.penup()
            t.hideturtle()
            t.goto(-210, 210)
            score_string = f'Score: {score}'
            t.clear()
            t.write(score_string, font=("inter", 16))

def move_enemies():
    for enemy in enemies:
        enemy.fd(3)
        if enemy.xcor() > 240 or enemy.xcor() < -240:
            enemy.lt(180)
        if enemy.ycor() > 240 or enemy.ycor() < -240:
            enemy.lt(180)
    screen.ontimer(move_enemies, 20)

screen.listen()
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(run, "Up")
screen.onkeypress(slowed, "Down")

move()
move_enemies()

done()
